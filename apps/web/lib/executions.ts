import "server-only";
import { Sandbox } from "@vercel/sandbox";
import { admin } from "./server";
export type Execution = {
    id: string;
    identity: string;
    status: string;
    sandbox_id: string | null;
    command_id: string | null;
    expires_at: string;
    created_at: string;
    activity_id: string;
    result: Record<string, unknown> | null;
};
export async function finish(row: Execution, result: Record<string, unknown>) {
    const measured = {
        ...result,
        durationMs: Math.max(0, Date.now() - Date.parse(row.created_at)),
        language: row.activity_id.split("/")[0],
    };
    const { data, error } = await admin().rpc("finish_execution", {
        p_id: row.id,
        p_identity: row.identity,
        p_result: measured,
    });
    if (error) throw error;
    return { id: row.id, ...data };
}
export async function inspect(row: Execution, cancel = false) {
    if (!["starting", "compiling", "running"].includes(row.status))
        return { id: row.id, ...(row.result ?? { status: row.status }) };
    if (Date.now() > Date.parse(row.expires_at)) {
        if (row.sandbox_id)
            await Sandbox.get({ name: row.sandbox_id })
                .then((s) => s.stop())
                .catch(() => {});
        return finish(row, { status: "limit", message: "Execution expired" });
    }
    if (!row.sandbox_id) return { id: row.id, status: "starting" };
    const sandbox = await Sandbox.get({ name: row.sandbox_id });
    if (cancel) {
        await sandbox.stop();
        return finish(row, {
            status: cancel ? "cancelled" : "limit",
            message: cancel ? "Execution stopped" : "Execution expired",
        });
    }
    if (!row.command_id) return { id: row.id, status: "starting" };
    const command = await sandbox.getCommand(row.command_id);
    if (command.exitCode === null) {
        const signal = AbortSignal.timeout(1500);
        try {
            await command.wait({ signal });
        } catch (error) {
            if (signal.aborted) return { id: row.id, status: "running" };
            throw error;
        }
    }
    let result: Record<string, unknown>;
    try {
        const output =
            (
                await sandbox.readFileToBuffer({
                    path: "/opt/learn/result.json",
                })
            )?.toString("utf8") ?? "";
        if (Buffer.byteLength(output) > 2 * 1024 * 1024) throw Error();
        result = JSON.parse(output);
        if (
            ![
                "passed",
                "failed",
                "compile_error",
                "limit",
                "unavailable",
            ].includes(String(result.status))
        )
            throw Error();
    } catch {
        result = {
            status: "unavailable",
            message: "The execution environment could not return a result.",
        };
    }
    await sandbox.stop();
    return finish(row, result);
}
