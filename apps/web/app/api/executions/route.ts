import { z } from "zod";
import { Sandbox } from "@vercel/sandbox";
import { catalog } from "@/lib/catalog";
import {
    admin,
    digest,
    executionConfigured,
    identity,
    json,
    sameOrigin,
} from "@/lib/server";
import { finish, type Execution } from "@/lib/executions";
export const maxDuration = 60;
const schema = z.object({
    activityId: z.string().max(200),
    revision: z.string(),
    code: z.string().refine((v) => Buffer.byteLength(v) <= 65536),
    stdin: z.string().refine((v) => Buffer.byteLength(v) <= 16384),
    mode: z.enum(["run", "check"]),
    key: z.string().uuid(),
});
export async function POST(request: Request) {
    let sandbox: Sandbox | undefined;
    let row: Execution | undefined;
    try {
        sameOrigin(request);
        if (!executionConfigured())
            return json(
                {
                    message:
                        "Execution is unavailable. You can still edit and download.",
                },
                503,
            );
        const text = await request.text();
        if (Buffer.byteLength(text) > 100000)
            return json({ message: "Request too large" }, 413);
        const data = schema.parse(JSON.parse(text));
        const activity = catalog.activities[data.activityId];
        if (
            !activity?.enabled ||
            data.revision !== catalog.revision ||
            (data.mode === "check" && activity.kind !== "exercise")
        )
            return json(
                {
                    message:
                        "Activity unavailable or content changed. Reload before running.",
                },
                400,
            );
        const owner = await identity(request);
        const db = admin();
        const { data: reservation, error } = await db.rpc("reserve_execution", {
            p_identity: owner.id,
            p_user_id: owner.userId,
            p_ip: owner.ip,
            p_key: data.key,
            p_hash: digest(JSON.stringify(data)),
            p_activity: activity.id,
            p_revision: data.revision,
            p_mode: data.mode,
        });
        if (error) return json({ message: error.message }, 429);
        row = reservation.execution;
        if (!reservation.created)
            return json({
                id: row!.id,
                ...(row!.result ?? { status: row!.status }),
            });
        sandbox = await Sandbox.create({
            source: {
                type: "snapshot",
                snapshotId: process.env.SANDBOX_SNAPSHOT_ID!,
            },
            persistent: false,
            timeout: Math.max(
                1000,
                Math.min(55000, Date.parse(row!.expires_at) - Date.now()),
            ),
            resources: { vcpus: 1 },
            networkPolicy: "deny-all",
            ports: [],
        });
        let update = await db
            .from("executions")
            .update({ sandbox_id: sandbox.name })
            .eq("id", row!.id);
        if (update.error) throw update.error;
        await sandbox.writeFiles([
            {
                path: "/tmp/learn-request.json",
                mode: 0o600,
                content: Buffer.from(
                    JSON.stringify({
                        language: activity.language,
                        filename: activity.path.split("/").at(-1),
                        code: data.code,
                        stdin: data.stdin,
                        mode: data.mode,
                        cases: activity.cases,
                        support: activity.support ?? [],
                    }),
                ),
            },
        ]);
        const protect = await sandbox.runCommand({
            cmd: "install",
            args: [
                "-o",
                "root",
                "-g",
                "root",
                "-m",
                "600",
                "/tmp/learn-request.json",
                "/opt/learn/request.json",
            ],
            sudo: true,
        });
        if (protect.exitCode !== 0) throw Error("Cannot prepare execution");
        const command = await sandbox.runCommand({
            cmd: "python3.12",
            args: ["/opt/learn/runner.py"],
            sudo: true,
            detached: true,
        });
        update = await db
            .from("executions")
            .update({ command_id: command.cmdId, status: "running" })
            .eq("id", row!.id);
        if (update.error) throw update.error;
        return json({ id: row!.id, status: "running" }, 202);
    } catch (error) {
        console.error("execution_start_failed", {
            stage: row ? (sandbox ? "prepare" : "sandbox") : "admission",
            kind: error instanceof Error ? error.name : "unknown",
            originRejected:
                error instanceof Error &&
                error.message === "Invalid request origin",
        });
        if (sandbox) await sandbox.stop().catch(() => {});
        if (row)
            await finish(row, {
                status: "unavailable",
                message: "Execution could not start. Please try again later.",
            }).catch(() => {});
        return json(
            { message: "Execution could not start. Please try again later." },
            503,
        );
    }
}
