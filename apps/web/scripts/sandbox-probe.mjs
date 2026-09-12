// Trusted curriculum-only feasibility probe. Never pass learner code to this script.
import { Sandbox } from "@vercel/sandbox";
import { execFileSync } from "node:child_process";
import { mkdir, writeFile, readFile } from "node:fs/promises";
import { fileURLToPath } from "node:url";

const root = fileURLToPath(new URL("../../../", import.meta.url));
const revision = execFileSync("git", ["rev-parse", "HEAD"], {
    cwd: root,
    encoding: "utf8",
}).trim();
const started = Date.now();
const report = { revision, sdk: "3.2.1", measurements: [], passed: false };
let sandbox;
async function run(label, cmd, args, options = {}) {
    const start = Date.now();
    const result = await sandbox.runCommand({ cmd, args, ...options });
    const stdout = await result.stdout();
    const stderr = await result.stderr();
    report.measurements.push({
        label,
        milliseconds: Date.now() - start,
        exitCode: result.exitCode,
        stdout,
        stderr,
    });
    console.log(`${label}: exit ${result.exitCode} (${Date.now() - start}ms)`);
    if (result.exitCode !== 0)
        throw new Error(`${label} failed: ${stderr || stdout}`);
    return stdout;
}
try {
    sandbox = await Sandbox.create({
        runtime: "node22",
        persistent: false,
        timeout: 900_000,
        resources: { vcpus: 1 },
        source: {
            type: "git",
            url: "https://github.com/lucasbellesi/learn-programming-languages-with-examples.git",
            revision,
        },
    });
    report.creationMilliseconds = Date.now() - started;
    await run(
        "system toolchains",
        "dnf",
        [
            "install",
            "-y",
            "gcc-c++",
            "java-21-amazon-corretto-devel",
            "python3.12",
            "tar",
            "gzip",
        ],
        { sudo: true },
    );
    await run(
        "Go 1.22.12",
        "sh",
        [
            "-ec",
            "curl -fsSL https://go.dev/dl/go1.22.12.linux-amd64.tar.gz -o /tmp/go.tar.gz; tar -C /usr/local -xzf /tmp/go.tar.gz; rm /tmp/go.tar.gz; ln -s /usr/local/go/bin/go /usr/local/bin/go",
        ],
        { sudo: true },
    );
    await run(
        ".NET 8",
        "sh",
        [
            "-ec",
            "curl -fsSL https://dot.net/v1/dotnet-install.sh -o /tmp/dotnet-install.sh; sh /tmp/dotnet-install.sh --channel 8.0 --install-dir /usr/local/dotnet; ln -s /usr/local/dotnet/dotnet /usr/local/bin/dotnet; rm /tmp/dotnet-install.sh",
        ],
        { sudo: true },
    );
    await run("TypeScript dependencies", "npm", ["ci"]);
    await run("versions", "sh", [
        "-ec",
        "g++ --version; dotnet --version; go version; java -version; python3.12 --version; node --version; npx --no-install tsc --version",
    ]);
    for (const language of [
        "cpp",
        "csharp",
        "go",
        "java",
        "python",
        "typescript",
    ]) {
        await run(`${language} sample contracts`, "python3.12", [
            "scripts/automation.py",
            "check-exercise",
            "--language",
            language,
            "--level",
            "01-foundations",
            "--module",
            "types-and-io",
            "--exercise",
            "01",
            "--solution",
        ]);
    }
    await sandbox.updateNetworkPolicy("deny-all");
    await run("network denied", "sh", [
        "-ec",
        "if curl -fsS --max-time 3 https://example.com >/dev/null 2>&1; then exit 1; fi",
    ]);
    if (process.argv.includes("--snapshot")) {
        await run(
            "trusted supervisor directory",
            "sh",
            [
                "-ec",
                "mkdir -p /opt/learn; cp -a /vercel/sandbox /opt/curriculum; chown -R root:root /opt/curriculum /opt/learn; chmod -R a+rX /opt/curriculum; chmod 755 /opt/learn",
            ],
            { sudo: true },
        );
        await sandbox.writeFiles([
            {
                path: "/tmp/runner.py",
                content: await readFile(
                    new URL("./sandbox-runner.py", import.meta.url),
                ),
            },
        ]);
        await run(
            "install supervisor",
            "install",
            [
                "-o",
                "root",
                "-g",
                "root",
                "-m",
                "500",
                "/tmp/runner.py",
                "/opt/learn/runner.py",
            ],
            { sudo: true },
        );
        const snapshot = await sandbox.snapshot({ expiration: 0 });
        report.snapshotId = snapshot.snapshotId;
        report.snapshotBytes = snapshot.sizeBytes;
        if (snapshot.sizeBytes > 12 * 1024 ** 3)
            throw new Error("Snapshot exceeds the free beta storage budget");
        console.log(
            `Snapshot: ${snapshot.snapshotId} (${snapshot.sizeBytes} bytes)`,
        );
        sandbox = undefined;
    }
    report.passed = true;
} catch (error) {
    report.error = error.message;
    console.error(error.message);
    process.exitCode = 1;
} finally {
    if (sandbox) await sandbox.stop();
    report.totalMilliseconds = Date.now() - started;
    const reportDir = fileURLToPath(new URL("../build/", import.meta.url));
    await mkdir(reportDir, { recursive: true });
    await writeFile(
        `${reportDir}/sandbox-feasibility.json`,
        JSON.stringify(report, null, 2) + "\n",
    );
}
