import { Sandbox } from "@vercel/sandbox";
import { readFile, writeFile } from "node:fs/promises";
const box = await Sandbox.create({
    source: { type: "snapshot", snapshotId: process.env.SANDBOX_SNAPSHOT_ID },
    persistent: false,
    timeout: 120000,
    resources: { vcpus: 1 },
    networkPolicy: "deny-all",
});
try {
    await box.writeFiles([
        {
            path: "/tmp/runner.py",
            content: await readFile(
                new URL("./sandbox-runner.py", import.meta.url),
            ),
        },
    ]);
    const result = await box.runCommand({
        cmd: "install",
        args: [
            "-o",
            "root",
            "-g",
            "root",
            "-m",
            "500",
            "/tmp/runner.py",
            "/opt/learn/runner.py",
        ],
        sudo: true,
    });
    if (result.exitCode !== 0) throw Error("Supervisor install failed");
    const snapshot = await box.snapshot({ expiration: 0 });
    console.log(
        `Snapshot: ${snapshot.snapshotId} (${snapshot.sizeBytes} bytes)`,
    );
    const envPath = new URL("../.env.local", import.meta.url);
    const env = (await readFile(envPath, "utf8")).replace(
        /^SANDBOX_SNAPSHOT_ID=.*$/m,
        `SANDBOX_SNAPSHOT_ID=${snapshot.snapshotId}`,
    );
    await writeFile(envPath, env);
} finally {
    await box.stop().catch(() => {});
}
