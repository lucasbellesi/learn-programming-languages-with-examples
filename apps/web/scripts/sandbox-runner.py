"""Root-owned supervisor: compile/run as nobody, grade using the canonical oracle.

Installed in a trusted snapshot, never accepted from a web request. Its JSON
output is read from a root-owned file through the SDK filesystem API.
"""

import json
import os
import resource
import re
import shutil
import signal
import stat
import subprocess
import sys
import tempfile
import time
from pathlib import Path

sys.path.insert(0, "/opt/curriculum/scripts")
from automation_core.ops import AutomationError, assert_output_contract  # noqa: E402

LIMIT = 65536
START = time.monotonic()
ENV = {
    "PATH": (
        "/usr/local/bin:/usr/bin:/bin:/usr/local/go/bin:"
        "/usr/local/dotnet:/vercel/runtimes/node22/bin"
    ),
    "DOTNET_ROOT": "/usr/local/dotnet",
    "DOTNET_CLI_TELEMETRY_OPTOUT": "1",
    "DOTNET_SKIP_FIRST_TIME_EXPERIENCE": "1",
    "DOTNET_NOLOGO": "1",
    "DOTNET_PROCESSOR_COUNT": "1",
    "LANG": "C.UTF-8",
    "LC_ALL": "C.UTF-8",
    "GOTOOLCHAIN": "local",
    "GOPROXY": "off",
}


def execute(command, cwd, stdin="", seconds=3, compile_step=False):
    remaining = 53 - (time.monotonic() - START)
    if remaining <= 0:
        return {"stdout": "", "stderr": "", "exitCode": -1, "message": "Time limit exceeded"}
    with tempfile.TemporaryFile() as stdout, tempfile.TemporaryFile() as stderr:
        env = {**ENV, "HOME": str(cwd), "TMPDIR": str(cwd), "DOTNET_CLI_HOME": str(cwd)}

        # Compile under a separate limit so compiler artifacts may exceed 64 KiB.
        def child():
            os.setsid()
            resource.setrlimit(resource.RLIMIT_CORE, (0, 0))
            resource.setrlimit(resource.RLIMIT_NPROC, (128, 128))
            resource.setrlimit(resource.RLIMIT_NOFILE, (1024, 1024))
            # .NET creates large memory-mapped backing files. Bound files
            # separately from console output, which the parent monitors below.
            # .NET reserves a very large anonymous memfd for executable memory;
            # RLIMIT_FSIZE also applies to memfd, so it cannot be used for .NET.
            # The outer microVM bounds storage; console bytes are always capped.
            if command[0] != "dotnet":
                cap = 256 * 1024 * 1024 if compile_step else 64 * 1024 * 1024
                resource.setrlimit(resource.RLIMIT_FSIZE, (cap, cap))
            cpu = 30 if compile_step else 3
            resource.setrlimit(resource.RLIMIT_CPU, (cpu, cpu))

        # PID 1 owns each case's descendants: exiting kills even double-forked
        # processes. A fresh network namespace has no external interfaces.
        isolated = [
            "unshare",
            "--mount-proc",
            "--pid",
            "--fork",
            "--kill-child=KILL",
            "--net",
            "--",
            "setpriv",
            "--reuid=65534",
            "--regid=65534",
            "--clear-groups",
            "--no-new-privs",
            "--",
            *command,
        ]
        process = subprocess.Popen(
            isolated,
            cwd=cwd,
            env=env,
            stdin=subprocess.PIPE,
            stdout=stdout,
            stderr=stderr,
            preexec_fn=child,
        )
        message = ""
        try:
            deadline = time.monotonic() + min(seconds, remaining)
            first = True
            while True:
                try:
                    process.communicate(stdin.encode() if first else None, timeout=0.05)
                    break
                except subprocess.TimeoutExpired:
                    first = False
                    if stdout.tell() + stderr.tell() > LIMIT:
                        message = "Output limit exceeded"
                        break
                    if time.monotonic() > deadline:
                        message = "Time limit exceeded"
                        break
        finally:
            try:
                os.killpg(process.pid, signal.SIGKILL)
            except ProcessLookupError:
                pass
            process.wait()
        stdout.seek(0)
        stderr.seek(0)
        out, err = stdout.read(LIMIT + 1), stderr.read(LIMIT + 1)
        if len(out) + len(err) > LIMIT:
            message = "Output limit exceeded"
        if process.returncode == -signal.SIGXFSZ:
            message = "File size limit exceeded"
        return {
            "stdout": out[:LIMIT].decode(errors="replace"),
            "stderr": err[: max(0, LIMIT - len(out))].decode(errors="replace"),
            "exitCode": process.returncode,
            "message": message,
        }


def own(path):
    for file in [path, *path.rglob("*")]:
        if not file.is_symlink():
            os.chown(file, 65534, 65534)


def main():
    request = json.loads(Path("/opt/learn/request.json").read_text())
    language = request["language"]
    filename = {
        "cpp": "main.cpp",
        "csharp": "Program.cs",
        "go": "main.go",
        "java": "Main.java",
        "python": "main.py",
        "typescript": "main.ts",
    }[language]
    if language == "java":
        filename = request.get("filename", "Main.java")
        if not re.fullmatch(r"[A-Za-z][A-Za-z0-9_]*\.java", filename):
            raise ValueError("Invalid Java entrypoint")
    with tempfile.TemporaryDirectory(prefix="learn-") as directory:
        base = Path(directory)
        # The root-owned container prevents the learner replacing case paths.
        base.chmod(0o755)
        build = base / "compile"
        build.mkdir()
        (build / filename).write_text(request["code"])
        for support in request.get("support", []):
            if not re.fullmatch(r"[A-Za-z0-9_-]+\.(h|hpp)", support["name"]):
                raise ValueError("Invalid support file")
            (build / support["name"]).write_text(support["source"])
        (build / "NuGet.Config").write_text(
            "<configuration><packageSources><clear /></packageSources></configuration>"
        )
        (build / "program.csproj").write_text(
            '<Project Sdk="Microsoft.NET.Sdk"><PropertyGroup><OutputType>Exe</OutputType>'
            "<TargetFramework>net8.0</TargetFramework><ImplicitUsings>disable</ImplicitUsings>"
            "<Nullable>disable</Nullable><UseAppHost>false</UseAppHost></PropertyGroup></Project>"
        )
        builds = {
            "cpp": [
                "g++",
                "-std=c++17",
                "-Wall",
                "-Wextra",
                "-pedantic",
                "main.cpp",
                "-o",
                "program",
            ],
            "csharp": [
                "dotnet",
                "build",
                "program.csproj",
                "--nologo",
                "--verbosity",
                "quiet",
                "-o",
                "out",
            ],
            "go": ["go", "build", "-o", "program", "main.go"],
            "java": ["javac", filename],
            "typescript": [
                "/opt/curriculum/node_modules/.bin/tsc",
                "main.ts",
                "--module",
                "commonjs",
                "--target",
                "ES2022",
                "--strict",
                "--skipLibCheck",
                "--typeRoots",
                "/opt/curriculum/node_modules/@types",
                "--types",
                "node",
            ],
        }
        runs = {
            "cpp": ["./program"],
            "csharp": ["dotnet", "out/program.dll"],
            "go": ["./program"],
            "java": ["java", filename[:-5]],
            "python": ["python3.12", "main.py"],
            "typescript": ["node", "main.js"],
        }
        own(build)
        if language in builds:
            compiled = execute(builds[language], build, seconds=30, compile_step=True)
            if compiled["exitCode"] != 0 or compiled["message"]:
                return {
                    "status": "limit" if compiled["message"] else "compile_error",
                    "compilation": compiled["stdout"] + compiled["stderr"],
                    "message": compiled["message"],
                }
        # Copy only runtime artifacts, excluding compiler caches and diagnostic
        # sockets. The root-owned artifact tree cannot be poisoned by a case.
        artifacts = base / "artifacts"
        artifacts.mkdir()
        patterns = {
            "cpp": ["program"],
            "go": ["program"],
            "python": ["main.py"],
            "java": ["*.class"],
            "typescript": ["main.js"],
            "csharp": ["out/*"],
        }
        for pattern in patterns[language]:
            for source in build.glob(pattern):
                if not stat.S_ISREG(source.lstat().st_mode):
                    raise ValueError("Unexpected compiler artifact")
                target = artifacts / source.relative_to(build)
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(source, target)
                target.chmod(0o555 if source.stat().st_mode & 0o111 else 0o444)
        cases = (
            request["cases"]
            if request["mode"] == "check"
            else [{"name": "Your run", "input_lines": None}]
        )
        results = []
        previous = None
        for index, case in enumerate(cases):
            text = "\n".join(case.get("input_lines") or []) + (
                "\n" if case.get("input_lines") is not None else ""
            )
            if request["mode"] == "run":
                text = request.get("stdin", "")
            if case.get("shared_execution") and previous and previous[0] == text:
                actual = previous[1]
            else:
                work = base / f"case-{index}"
                shutil.copytree(artifacts, work, symlinks=False)
                own(work)
                actual = execute(runs[language], work, text)
                previous = (text, actual)
            passed = actual["exitCode"] == 0 and not actual["message"]
            message = actual["message"]
            if passed and request["mode"] == "check":
                try:
                    assert_output_contract(actual["stdout"], case, case["name"])
                except AutomationError as error:
                    passed = False
                    message = str(error)
            expected = case.get("required_stdout_equals") or json.dumps(
                {k: v for k, v in case.items() if "stdout" in k}, ensure_ascii=False
            )
            results.append(
                {
                    "name": case["name"],
                    "input": text,
                    "expected": expected
                    if request["mode"] == "check"
                    else "Free run: no expected output",
                    "stdout": actual["stdout"],
                    "stderr": actual["stderr"],
                    "passed": passed,
                    "message": message,
                }
            )
        return {
            "status": "passed" if all(r["passed"] for r in results) else "failed",
            "cases": results,
        }


if __name__ == "__main__":
    os.umask(0o077)
    try:
        result = main()
    except Exception:
        result = {
            "status": "unavailable",
            "message": "The execution environment failed. Please retry later.",
        }
    # Root-owned output is retrieved through the filesystem API, never stdout
    # logging. Learner stdout, stdin, and diagnostics stay out of service logs.
    output = Path("/opt/learn/result.json")
    output.write_text(json.dumps(result, ensure_ascii=True))
    # Grant the SDK service user read-only access, never the learner's group.
    os.chown(output, 0, os.stat("/vercel/sandbox").st_gid)
    output.chmod(0o640)
