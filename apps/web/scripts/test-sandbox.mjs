// Explicit integration test; consumes the authenticated project's Sandbox quota.
import { Sandbox } from "@vercel/sandbox";
import { readFile, mkdir, writeFile } from "node:fs/promises";
const catalog = JSON.parse(
    await readFile(new URL("../generated/catalog.json", import.meta.url)),
);
const solutions = JSON.parse(
    await readFile(new URL("../generated/solutions.json", import.meta.url)),
);
const all = process.argv.includes("--all");
const activities = Object.values(catalog.activities).filter(
    (a) =>
        a.enabled &&
        (all || (a.kind === "exercise" && a.id.endsWith("/types-and-io/01"))),
);
const report = {
    snapshot: process.env.SANDBOX_SNAPSHOT_ID,
    tests: [],
    passed: true,
};
async function attempt(name, payload, expected = "passed") {
    const start = Date.now();
    let s;
    try {
        s = await Sandbox.create({
            source: {
                type: "snapshot",
                snapshotId: process.env.SANDBOX_SNAPSHOT_ID,
            },
            persistent: false,
            timeout: 55000,
            resources: { vcpus: 1 },
            networkPolicy: "deny-all",
        });
        await s.writeFiles([
            {
                path: "/tmp/request.json",
                content: Buffer.from(JSON.stringify(payload)),
            },
        ]);
        const protect = await s.runCommand({
            cmd: "install",
            args: [
                "-o",
                "root",
                "-g",
                "root",
                "-m",
                "600",
                "/tmp/request.json",
                "/opt/learn/request.json",
            ],
            sudo: true,
        });
        if (protect.exitCode !== 0) throw Error("Failed to install input");
        const command = await s.runCommand({
            cmd: "python3.12",
            args: ["/opt/learn/runner.py"],
            sudo: true,
            detached: true,
        });
        if (expected === "cancelled") {
            await s.stop();
            report.tests.push({
                name,
                status: "cancelled",
                milliseconds: Date.now() - start,
            });
            console.log(`${name}: cancelled`);
            return;
        }
        const done = await command.wait();
        const output =
            (
                await s.readFileToBuffer({ path: "/opt/learn/result.json" })
            )?.toString("utf8") ?? "";
        let result;
        try {
            result = JSON.parse(output);
        } catch {
            throw Error(
                `Invalid runner output: ${output} ${await done.stderr()}`,
            );
        }
        const passed = result.status === expected;
        report.tests.push({
            name,
            milliseconds: Date.now() - start,
            passed,
            result,
        });
        console.log(`${name}: ${result.status} (${Date.now() - start}ms)`);
        if (!passed) {
            report.passed = false;
            console.log(JSON.stringify(result));
        }
    } catch (error) {
        report.passed = false;
        report.tests.push({ name, error: error.message });
        console.log(`${name}: ${error.message}`);
    } finally {
        if (s) await s.stop().catch(() => {});
    }
}
const pending = [...activities];
async function worker() {
    while (pending.length && report.passed) {
        const a = pending.shift();
        await attempt(a.id, {
            language: a.language,
            filename: a.path.split("/").at(-1),
            code: a.kind === "example" ? a.source : solutions[a.id].source,
            mode: "check",
            cases: a.cases,
            support: a.support ?? [],
        });
    }
}
await Promise.all(Array.from({ length: all ? 2 : 1 }, () => worker()));
if (report.passed) {
    const python = { language: "python", mode: "run", stdin: "", cases: [] };
    await attempt(
        "infinite loop",
        { ...python, code: "while True: pass" },
        "failed",
    );
    await attempt(
        "output cap",
        { ...python, code: 'print("x" * 1000000)' },
        "failed",
    );
    await attempt(
        "compile error",
        {
            language: "cpp",
            mode: "run",
            code: "this is not C++;",
            stdin: "",
            cases: [],
        },
        "compile_error",
    );
    await attempt(
        "cancel",
        { ...python, code: "while True: pass" },
        "cancelled",
    );
    await attempt("unprivileged and no credentials", {
        ...python,
        code: 'import os\nassert os.getuid() == 65534\nassert not any(k.startswith(("VERCEL", "SUPABASE", "SESSION_SECRET")) for k in os.environ)\ntry:\n open("/opt/learn/request.json")\n raise RuntimeError("request readable")\nexcept PermissionError:\n pass\ntry:\n open("/opt/learn/runner.py", "w")\n raise RuntimeError("runner writable")\nexcept PermissionError:\n pass\nprint("isolated")',
    });
    await attempt("network blocked", {
        ...python,
        code: 'import socket\nsocket.setdefaulttimeout(1)\ntry:\n socket.create_connection(("1.1.1.1",443),1)\n raise RuntimeError("network open")\nexcept (OSError, TimeoutError):\n print("blocked")',
    });
    const a = activities.find(
        (a) => a.language === "python" && a.kind === "exercise",
    );
    await attempt(
        "incomplete starter",
        {
            language: a.language,
            filename: a.path.split("/").at(-1),
            code: a.source,
            mode: "check",
            cases: a.cases,
        },
        "failed",
    );
}
await mkdir(new URL("../build/", import.meta.url), { recursive: true });
await writeFile(
    new URL("../build/sandbox-tests.json", import.meta.url),
    JSON.stringify(report, null, 2) + "\n",
);
if (!report.passed) process.exitCode = 1;
