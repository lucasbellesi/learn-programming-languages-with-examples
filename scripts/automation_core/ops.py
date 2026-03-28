from __future__ import annotations

import argparse
import os
import re
import shlex
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .manifest import Manifest, load_manifest


@dataclass(frozen=True)
class RepoContext:
    root: Path
    scripts_dir: Path
    manifest: Manifest

    @property
    def is_windows(self) -> bool:
        return os.name == "nt"


@dataclass(frozen=True)
class GppToolchain:
    mode: str
    command: str


class AutomationError(RuntimeError):
    pass


def main(argv: list[str] | None = None) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(line_buffering=True)
    parser = build_parser()
    args = parser.parse_args(argv)
    ctx = create_context()
    try:
        return args.func(ctx, args)
    except AutomationError as error:
        print(error)
        return 1


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Shared automation core for repository scripts.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_simple_command(subparsers, "build-all", handle_build_all)
    add_simple_command(subparsers, "check-readme-structure", handle_check_readme_structure)
    add_simple_command(subparsers, "check-module-completeness", handle_check_module_completeness)
    add_simple_command(
        subparsers, "check-checkpoint-completeness", handle_check_checkpoint_completeness
    )
    add_simple_command(subparsers, "check-doc-sync", handle_check_doc_sync)
    add_simple_command(subparsers, "lint", handle_lint)
    add_simple_command(subparsers, "smoke-languages", handle_smoke_languages)
    add_simple_command(subparsers, "verify-repo", handle_verify_repo)

    run_module = subparsers.add_parser("run-module")
    run_module.add_argument("--module-path", required=True)
    run_module.set_defaults(func=handle_run_module)
    return parser


def add_simple_command(
    subparsers: argparse._SubParsersAction[argparse.ArgumentParser],
    name: str,
    func: Any,
) -> None:
    parser = subparsers.add_parser(name)
    parser.set_defaults(func=func)


def create_context() -> RepoContext:
    scripts_dir = Path(__file__).resolve().parent.parent
    root = scripts_dir.parent
    manifest = load_manifest(scripts_dir)
    return RepoContext(root=root, scripts_dir=scripts_dir, manifest=manifest)


def handle_build_all(ctx: RepoContext, _: argparse.Namespace) -> int:
    build_all(ctx)
    return 0


def handle_check_readme_structure(ctx: RepoContext, _: argparse.Namespace) -> int:
    check_readme_structure(ctx)
    return 0


def handle_check_module_completeness(ctx: RepoContext, _: argparse.Namespace) -> int:
    check_module_completeness(ctx)
    return 0


def handle_check_checkpoint_completeness(ctx: RepoContext, _: argparse.Namespace) -> int:
    check_checkpoint_completeness(ctx)
    return 0


def handle_check_doc_sync(ctx: RepoContext, _: argparse.Namespace) -> int:
    check_doc_sync(ctx)
    return 0


def handle_smoke_languages(ctx: RepoContext, _: argparse.Namespace) -> int:
    smoke_languages(ctx)
    return 0


def handle_lint(ctx: RepoContext, _: argparse.Namespace) -> int:
    lint_repo(ctx)
    return 0


def handle_verify_repo(ctx: RepoContext, _: argparse.Namespace) -> int:
    verify_repo(ctx)
    return 0


def handle_run_module(ctx: RepoContext, args: argparse.Namespace) -> int:
    run_module(ctx, args.module_path)
    return 0


def repo_path(ctx: RepoContext, relative_path: str) -> Path:
    return ctx.root / Path(relative_path)


def ensure_text_file(path: Path) -> str:
    if not path.is_file():
        raise AutomationError(f"Missing file: {path}")
    return path.read_text(encoding="utf-8")


def markdown_heading_positions(path: Path, headings: list[str]) -> dict[str, int]:
    lines = path.read_text(encoding="utf-8").splitlines()
    positions: dict[str, int] = {}
    patterns = {
        heading: re.compile(rf"^[ ]{{0,3}}{re.escape(heading)}[ ]*$") for heading in headings
    }
    in_fence = False

    for index, raw_line in enumerate(lines, start=1):
        stripped = raw_line.lstrip()
        if re.match(r"^(```|~~~)", stripped):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        for heading, pattern in patterns.items():
            if heading not in positions and pattern.match(raw_line):
                positions[heading] = index

    return positions


def require_markdown_headings(path: Path, headings: list[str]) -> list[str]:
    positions = markdown_heading_positions(path, headings)
    missing = [heading for heading in headings if heading not in positions]
    if missing:
        return [f"{path}: missing -> {', '.join(missing)}"]

    failures: list[str] = []
    last = -1
    for heading in headings:
        current = positions[heading]
        if current < last:
            failures.append(f"{path}: required headings are out of order.")
            break
        last = current
    return failures


def find_python_command() -> str:
    if sys.executable:
        return sys.executable
    for name in ("python", "python3"):
        resolved = shutil.which(name)
        if resolved:
            return resolved
    raise AutomationError("Python was not found in PATH.")


def find_command(*candidates: str) -> str | None:
    for candidate in candidates:
        resolved = shutil.which(candidate)
        if resolved:
            return resolved
    return None


def find_clang_format(ctx: RepoContext) -> str:
    resolved = find_command("clang-format", "clang-format.exe")
    if resolved:
        return resolved

    if ctx.is_windows:
        windows_candidates = [
            Path(
                r"C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Tools\Llvm\bin"
                r"\clang-format.exe"
            ),
            Path(
                r"C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Tools\Llvm\x64\bin"
                r"\clang-format.exe"
            ),
            Path(r"C:\Program Files\CodeBlocks\MinGW\bin\clang-format.exe"),
        ]
        for candidate in windows_candidates:
            if candidate.exists():
                return str(candidate)

    raise AutomationError("Required command not found: clang-format")


def run_command(
    command: list[str],
    *,
    cwd: Path | None = None,
    input_text: str | None = None,
    quiet_stdout: bool = False,
    action: str | None = None,
    timeout_seconds: float | None = None,
) -> subprocess.CompletedProcess[str]:
    try:
        completed = subprocess.run(
            command,
            cwd=str(cwd) if cwd else None,
            input=input_text,
            text=True,
            stdout=subprocess.DEVNULL if quiet_stdout else None,
            stderr=None,
            check=False,
            timeout=timeout_seconds,
        )
    except FileNotFoundError as error:
        missing = command[0] if command else "command"
        raise AutomationError(f"Required command not found: {missing}") from error
    except subprocess.TimeoutExpired as error:
        if action:
            raise AutomationError(
                f"{action} timed out after {error.timeout:g} second(s)."
            ) from error
        raise AutomationError(
            f"Command timed out after {error.timeout:g} second(s): {' '.join(command)}"
        ) from error
    if completed.returncode != 0:
        if action:
            raise AutomationError(f"{action} failed with exit code {completed.returncode}.")
        raise AutomationError(
            f"Command failed with exit code {completed.returncode}: {' '.join(command)}"
        )
    return completed


def resolve_gpp_toolchain(ctx: RepoContext) -> GppToolchain:
    native_gpp = shutil.which("g++")
    if native_gpp:
        return GppToolchain(mode="native", command=native_gpp)

    if ctx.is_windows and shutil.which("wsl"):
        probe = subprocess.run(
            ["wsl", "bash", "-lc", "command -v g++ >/dev/null 2>&1"],
            stdout=subprocess.DEVNULL,
            stderr=None,
            check=False,
        )
        if probe.returncode == 0:
            print("Native g++ not found. Using WSL g++ fallback.")
            return GppToolchain(mode="wsl", command="wsl")
        raise AutomationError(
            "WSL fallback is not ready: unable to run g++ inside WSL.\n"
            "Install g++ in WSL, fix WSL access, or install native g++ on Windows."
        )

    raise AutomationError(
        "g++ was not found in PATH.\nInstall g++ (or use WSL on Windows) and try again."
    )


def to_wsl_path(path: Path) -> str:
    resolved = path.resolve()
    drive = resolved.drive.rstrip(":").lower()
    tail = resolved.as_posix()[2:]
    return f"/mnt/{drive}{tail}"


def cpp_compile_command(
    ctx: RepoContext, toolchain: GppToolchain, source: Path, output: Path
) -> list[str]:
    if toolchain.mode == "native":
        command = [
            toolchain.command,
            "-std=c++17",
            "-Wall",
            "-Wextra",
            "-pedantic",
        ]
        if not ctx.is_windows:
            command.append("-pthread")
        command.extend([str(source), "-o", str(output)])
        return command

    inner = [
        "g++",
        "-std=c++17",
        "-Wall",
        "-Wextra",
        "-pedantic",
        "-pthread",
        to_wsl_path(source),
        "-o",
        to_wsl_path(output),
    ]
    return ["wsl", "bash", "-lc", " ".join(shlex.quote(part) for part in inner)]


def compiled_binary_path(ctx: RepoContext, base_output: Path) -> Path:
    if ctx.is_windows and not base_output.exists() and base_output.with_suffix(".exe").exists():
        return base_output.with_suffix(".exe")
    return base_output


def remove_paths(base_dir: Path, relative_paths: list[str]) -> None:
    for relative in relative_paths:
        candidate = base_dir / relative
        if candidate.is_dir():
            shutil.rmtree(candidate, ignore_errors=True)
        elif candidate.exists():
            candidate.unlink(missing_ok=True)


def resolve_job_path(ctx: RepoContext, working_dir: Path, raw_path: str) -> Path:
    candidate = Path(raw_path)
    if candidate.is_absolute():
        return candidate
    if working_dir != ctx.root and (working_dir / candidate).exists():
        return working_dir / candidate
    return ctx.root / candidate


def enumerate_source_files(
    ctx: RepoContext,
    *,
    roots: list[str],
    extensions: list[str],
    exclude_dirs: list[str] | None = None,
) -> list[Path]:
    excluded = set(exclude_dirs or [])
    files: list[Path] = []

    for root in roots:
        root_path = repo_path(ctx, root)
        if not root_path.exists():
            continue

        for extension in extensions:
            for path in root_path.rglob(f"*{extension}"):
                if not path.is_file():
                    continue
                if excluded.intersection(path.parts):
                    continue
                files.append(path)

    return sorted(set(files))


def iter_module_directories(ctx: RepoContext) -> list[tuple[str, str, Path]]:
    directories: list[tuple[str, str, Path]] = []
    for language, config in ctx.manifest.languages.items():
        for level in config.get("module_levels", []):
            level_path = ctx.root / "languages" / language / level
            if not level_path.is_dir():
                continue
            for module_dir in sorted(
                (path for path in level_path.iterdir() if path.is_dir()), key=lambda path: path.name
            ):
                directories.append((language, level, module_dir))
    return directories


def check_readme_structure(ctx: RepoContext) -> None:
    readmes = [
        module_dir / "README.md"
        for _, _, module_dir in iter_module_directories(ctx)
        if (module_dir / "README.md").is_file()
    ]
    if not readmes:
        raise AutomationError("No module README files found for validation.")

    failures: list[str] = []
    for readme in readmes:
        failures.extend(require_markdown_headings(readme, ctx.manifest.required_readme_headings))

    if failures:
        print("README structure validation failed:")
        for failure in failures:
            print(f" - {failure}")
        raise AutomationError("README structure validation failed.")

    print(f"README structure validation passed for {len(readmes)} module files.")


def check_module_completeness(ctx: RepoContext) -> None:
    failures: list[str] = []
    module_count = 0

    for language, config in ctx.manifest.languages.items():
        extension = config["extension"]
        module_levels = config.get("module_levels", [])

        for level in module_levels:
            level_path = ctx.root / "languages" / language / level
            if not level_path.is_dir():
                continue

            expected_modules = list(ctx.manifest.module_order[level])
            actual_modules = sorted(path.name for path in level_path.iterdir() if path.is_dir())
            missing_modules = [name for name in expected_modules if name not in actual_modules]
            unexpected_modules = [name for name in actual_modules if name not in expected_modules]

            for module_name in missing_modules:
                failures.append(f"{level_path}: missing module directory {module_name}")
            for module_name in unexpected_modules:
                failures.append(f"{level_path}: unexpected module directory {module_name}")

            for module_name in actual_modules:
                module_dir = level_path / module_name
                module_count += 1

                readme_path = module_dir / "README.md"
                example_dir = module_dir / "example"
                exercises_dir = module_dir / "exercises"
                main_path = example_dir / f"main.{extension}"
                exercise01 = exercises_dir / f"01.{extension}"
                exercise02 = exercises_dir / f"02.{extension}"

                if not readme_path.is_file():
                    failures.append(f"{module_dir}: missing README.md")
                    continue
                if not example_dir.is_dir():
                    failures.append(f"{module_dir}: missing example/ directory")
                if not exercises_dir.is_dir():
                    failures.append(f"{module_dir}: missing exercises/ directory")
                if not main_path.is_file():
                    failures.append(f"{module_dir}: missing example/main.{extension}")
                if not exercise01.is_file():
                    failures.append(f"{module_dir}: missing exercises/01.{extension}")
                if not exercise02.is_file():
                    failures.append(f"{module_dir}: missing exercises/02.{extension}")

                heading_failures = require_markdown_headings(
                    readme_path, ctx.manifest.required_readme_headings
                )
                for failure in heading_failures:
                    suffix = failure.split(": ", 1)[1] if ": " in failure else failure
                    failures.append(f"{module_dir}: README {suffix}")

    if module_count == 0:
        raise AutomationError("No module directories found for completeness validation.")

    if failures:
        print("Module completeness validation failed:")
        for failure in failures:
            print(f" - {failure}")
        raise AutomationError("Module completeness validation failed.")

    print(f"Module completeness validation passed for {module_count} module directories.")


def check_checkpoint_completeness(ctx: RepoContext) -> None:
    failures: list[str] = []
    checkpoint_count = 0

    for language, config in ctx.manifest.languages.items():
        language_root = ctx.root / "languages" / language
        if not language_root.is_dir():
            continue

        for kind in ctx.manifest.checkpoint_kinds:
            kind_root = language_root / kind
            if not kind_root.is_dir():
                continue

            expected_levels = list(config.get("checkpoints", {}).get(kind, []))
            actual_levels = sorted(path.name for path in kind_root.iterdir() if path.is_dir())
            missing_levels = [name for name in expected_levels if name not in actual_levels]
            unexpected_levels = [name for name in actual_levels if name not in expected_levels]

            for level in missing_levels:
                failures.append(f"{kind_root}: missing checkpoint directory {level}")
            for level in unexpected_levels:
                failures.append(f"{kind_root}: unexpected checkpoint directory {level}")

            for checkpoint_name in actual_levels:
                checkpoint_dir = kind_root / checkpoint_name
                checkpoint_count += 1
                readme_path = checkpoint_dir / "README.md"

                if not readme_path.is_file():
                    failures.append(f"{checkpoint_dir}: missing README.md")

                checkpoint_main = config.get("checkpoint_main")
                if checkpoint_main and not (checkpoint_dir / checkpoint_main).is_file():
                    failures.append(f"{checkpoint_dir}: missing {checkpoint_main}")

                if language == "csharp" and not any(checkpoint_dir.glob("*.csproj")):
                    failures.append(f"{checkpoint_dir}: missing .csproj file")

    if checkpoint_count == 0:
        raise AutomationError("No checkpoint directories found for completeness validation.")

    if failures:
        print("Checkpoint completeness validation failed:")
        for failure in failures:
            print(f" - {failure}")
        raise AutomationError("Checkpoint completeness validation failed.")

    print(
        f"Checkpoint completeness validation passed for {checkpoint_count} checkpoint directories."
    )


def check_doc_sync(ctx: RepoContext) -> None:
    failures: list[str] = []

    root_readme_path = repo_path(ctx, ctx.manifest.docs["root_readme"])
    root_readme_text = ensure_text_file(root_readme_path)
    for marker in ctx.manifest.docs["root_readme_markers"]:
        if marker not in root_readme_text:
            failures.append(f"{root_readme_path}: missing marker -> {marker}")

    for language, config in ctx.manifest.languages.items():
        track_readme_path = repo_path(ctx, config["track_readme"])
        track_readme_text = ensure_text_file(track_readme_path)
        for marker in config.get("track_readme_markers", []):
            if marker not in track_readme_text:
                failures.append(f"{track_readme_path}: missing marker -> {marker}")

        status_row = config.get("root_status_row")
        if status_row and status_row not in root_readme_text:
            failures.append(f"{root_readme_path}: missing status row for {language}")

    parity_path = repo_path(ctx, ctx.manifest.docs["parity_matrix"]["path"])
    parity_text = ensure_text_file(parity_path)
    for marker in ctx.manifest.docs["parity_matrix"]["markers"]:
        if marker not in parity_text:
            failures.append(f"{parity_path}: missing marker -> {marker}")

    if failures:
        print("Documentation sync validation failed:")
        for failure in failures:
            print(f" - {failure}")
        raise AutomationError("Documentation sync validation failed.")

    print("Documentation sync validation passed.")


def lint_repo(ctx: RepoContext) -> None:
    lint_config = ctx.manifest.lint

    print("[1/4] C++ formatting check...")
    cpp_files = enumerate_source_files(
        ctx,
        roots=lint_config["cpp"]["roots"],
        extensions=lint_config["cpp"]["extensions"],
        exclude_dirs=lint_config["cpp"].get("exclude_dirs", []),
    )
    clang_format = find_clang_format(ctx)
    for source in cpp_files:
        run_command(
            [clang_format, "--dry-run", "--Werror", str(source)],
            action=f"C++ formatting check for {source}",
        )

    print("[2/4] Python lint and format check...")
    python_cmd = find_python_command()
    python_paths = [str(repo_path(ctx, path)) for path in lint_config["python"]["paths"]]
    run_command([python_cmd, "-m", "ruff", "check", *python_paths], action="Python lint check")
    run_command(
        [python_cmd, "-m", "ruff", "format", "--check", *python_paths], action="Python format check"
    )

    print("[3/4] Go formatting check...")
    gofmt = find_command("gofmt", "gofmt.exe")
    if not gofmt:
        raise AutomationError("Required command not found: gofmt")
    go_files = enumerate_source_files(
        ctx,
        roots=lint_config["go"]["roots"],
        extensions=lint_config["go"]["extensions"],
        exclude_dirs=lint_config["go"].get("exclude_dirs", []),
    )
    gofmt_result = subprocess.run(
        [gofmt, "-l", *[str(path) for path in go_files]],
        text=True,
        capture_output=True,
        check=False,
    )
    if gofmt_result.returncode != 0:
        raise AutomationError(
            f"Go formatting check failed with exit code {gofmt_result.returncode}."
        )
    if gofmt_result.stdout.strip():
        print(gofmt_result.stdout.strip())
        raise AutomationError("Go formatting check failed.")

    print("[4/4] C# formatting check...")
    csharp_files = enumerate_source_files(
        ctx,
        roots=lint_config["csharp"]["roots"],
        extensions=lint_config["csharp"]["extensions"],
        exclude_dirs=lint_config["csharp"].get("exclude_dirs", []),
    )
    tool_manifest = ctx.root / ".config" / "dotnet-tools.json"
    run_command(
        ["dotnet", "tool", "restore", "--tool-manifest", str(tool_manifest)],
        action="C# tool restore",
    )
    run_command(
        ["dotnet", "tool", "run", "csharpier", "check", *[str(path) for path in csharp_files]],
        action="C# formatting check",
    )

    print("Lint checks passed.")


def build_all(ctx: RepoContext) -> None:
    cpp_files = sorted((ctx.root / "languages" / "cpp").rglob("*.cpp"))
    if not cpp_files:
        print("No C++ files found under languages/cpp")
        return

    build_dir = ctx.root / "build"
    build_dir.mkdir(exist_ok=True)
    toolchain = resolve_gpp_toolchain(ctx)

    for index, source in enumerate(cpp_files):
        print(f"Compiling: {source}")
        output = build_dir / f"check_{index}"
        command = cpp_compile_command(ctx, toolchain, source, output)
        action = f"Compilation for {source}"
        if toolchain.mode == "wsl":
            action = f"Compilation via WSL for {source}"
        run_command(command, action=action)

    print(f"Compiled {len(cpp_files)} file(s) successfully.")


def run_module(ctx: RepoContext, module_path: str) -> None:
    normalized = module_path.replace("\\", "/")
    candidate = Path(normalized)
    full_module_path = candidate if candidate.is_absolute() else (ctx.root / candidate)

    if not full_module_path.is_dir():
        raise AutomationError(f"Module folder not found: {normalized}")

    example_file = full_module_path / "example" / "main.cpp"
    if not example_file.is_file():
        raise AutomationError(f"Missing example file: {normalized}/example/main.cpp")

    toolchain = resolve_gpp_toolchain(ctx)
    fd, temp_output = tempfile.mkstemp(prefix="run_module_")
    os.close(fd)
    output_path = Path(temp_output)
    output_path.unlink(missing_ok=True)

    print(f"Compiling example: {normalized}/example/main.cpp")
    try:
        command = cpp_compile_command(ctx, toolchain, example_file, output_path)
        action = f"Compilation for {normalized}/example/main.cpp"
        if toolchain.mode == "wsl":
            action = f"Compilation via WSL for {normalized}/example/main.cpp"
        run_command(command, action=action)

        print("Running example...")
        if toolchain.mode == "wsl":
            binary_command = ["wsl", "bash", "-lc", shlex.quote(to_wsl_path(output_path))]
            run_command(
                binary_command, action=f"Execution via WSL for {normalized}/example/main.cpp"
            )
        else:
            binary_path = compiled_binary_path(ctx, output_path)
            run_command([str(binary_path)], action=f"Execution for {normalized}/example/main.cpp")

        exercises_dir = full_module_path / "exercises"
        exercise_files = sorted(exercises_dir.glob("*.cpp")) if exercises_dir.is_dir() else []
        if exercise_files:
            print()
            print(f"Exercises in {normalized}/exercises:")
            for exercise in exercise_files:
                print(f"- {normalized}/exercises/{exercise.name}")
    finally:
        compiled_binary_path(ctx, output_path).unlink(missing_ok=True)
        output_path.unlink(missing_ok=True)


def xml_escape(value: str) -> str:
    return (
        value.replace("&", "&amp;").replace('"', "&quot;").replace("<", "&lt;").replace(">", "&gt;")
    )


def csharp_output_dll(project_path: Path) -> Path:
    return project_path.parent / "bin" / "Debug" / "net8.0" / f"{project_path.stem}.dll"


def build_csharp_exercises(ctx: RepoContext) -> None:
    exercise_files = sorted(
        path
        for path in (ctx.root / "languages" / "csharp").rglob("*.cs")
        if "exercises" in path.parts
    )
    with tempfile.TemporaryDirectory(prefix="csharp-exercise-smoke-") as temp_root:
        temp_root_path = Path(temp_root)
        for index, exercise_path in enumerate(exercise_files):
            print(f"  Building exercise smoke harness: {exercise_path.relative_to(ctx.root)}")
            project_dir = temp_root_path / f"exercise-{index}"
            project_dir.mkdir(parents=True, exist_ok=True)
            project_path = project_dir / "exercise-check.csproj"
            escaped_path = xml_escape(str(exercise_path.resolve()))
            project_path.write_text(
                "\n".join(
                    [
                        '<Project Sdk="Microsoft.NET.Sdk">',
                        "  <PropertyGroup>",
                        "    <OutputType>Exe</OutputType>",
                        "    <TargetFramework>net8.0</TargetFramework>",
                        "    <ImplicitUsings>disable</ImplicitUsings>",
                        "    <Nullable>disable</Nullable>",
                        "    <EnableDefaultCompileItems>false</EnableDefaultCompileItems>",
                        "  </PropertyGroup>",
                        "  <ItemGroup>",
                        f'    <Compile Include="{escaped_path}" Link="Program.cs" />',
                        "  </ItemGroup>",
                        "</Project>",
                        "",
                    ]
                ),
                encoding="utf-8",
            )
            run_command(
                [
                    "dotnet",
                    "build",
                    str(project_path),
                    "--nologo",
                    "--verbosity",
                    "quiet",
                    "-p:UseAppHost=false",
                ],
                quiet_stdout=True,
                action=f"C# exercise build for {exercise_path}",
                timeout_seconds=180,
            )


def smoke_runtime_job(
    ctx: RepoContext,
    job: dict[str, Any],
    *,
    command_builder: Any,
    label: str,
    timeout_seconds: float = 30,
) -> None:
    working_dir = repo_path(ctx, job["working_dir"]) if "working_dir" in job else ctx.root
    setup_files = job.get("setup_files", [])
    cleanup_paths = list(job.get("cleanup_paths", []))

    try:
        for file_spec in setup_files:
            target = working_dir / file_spec["path"]
            target.write_text("\n".join(file_spec["lines"]) + "\n", encoding="utf-8")

        input_text = None
        if "input_lines" in job:
            input_text = "\n".join(job["input_lines"]) + "\n"
        elif "input_file" in job:
            input_text = str((working_dir / job["input_file"]).resolve()) + "\n"

        run_command(
            command_builder(job, working_dir),
            cwd=working_dir,
            input_text=input_text,
            quiet_stdout=True,
            action=label,
            timeout_seconds=timeout_seconds,
        )

        for output_name in job.get("required_outputs", []):
            if not (working_dir / output_name).exists():
                raise AutomationError(f"{label} did not create {output_name}")
    finally:
        remove_paths(working_dir, cleanup_paths)


def smoke_languages(ctx: RepoContext) -> None:
    python_cmd = find_python_command()

    python_smoke = ctx.manifest.smoke["python"]
    print("[1/6] Python syntax check...")
    run_command(
        [
            python_cmd,
            "-m",
            "compileall",
            "-q",
            str(repo_path(ctx, python_smoke["compileall_path"])),
        ],
        action="Python syntax check",
    )

    print("[2/6] Python runtime smoke...")
    for program in python_smoke["example_paths"]:
        run_command(
            [python_cmd, str(repo_path(ctx, program))],
            quiet_stdout=True,
            action=f"Python runtime smoke for {program}",
        )
    for job in python_smoke["stdin_runs"]:
        smoke_runtime_job(
            ctx,
            job,
            command_builder=lambda current_job, working_dir: [
                python_cmd,
                str(resolve_job_path(ctx, working_dir, current_job["program"])),
            ],
            label=f"Python runtime smoke for {job.get('program', job.get('working_dir', 'job'))}",
        )

    go_smoke = ctx.manifest.smoke["go"]
    print("[3/6] Go compile check...")
    with tempfile.TemporaryDirectory(prefix="go-smoke-") as temp_root:
        temp_root_path = Path(temp_root)
        go_files = sorted(repo_path(ctx, go_smoke["build_glob_root"]).rglob("*.go"))
        for index, source in enumerate(go_files):
            run_command(
                ["go", "build", "-o", str(temp_root_path / f"go_build_{index}"), str(source)],
                action=f"Go build for {source}",
            )

    print("[4/6] Go runtime smoke...")
    for program in go_smoke["example_paths"]:
        run_command(
            ["go", "run", str(repo_path(ctx, program))],
            quiet_stdout=True,
            action=f"Go runtime smoke for {program}",
        )
    for job in go_smoke["stdin_runs"]:
        smoke_runtime_job(
            ctx,
            job,
            command_builder=lambda current_job, working_dir: [
                "go",
                "run",
                str(resolve_job_path(ctx, working_dir, current_job["program"])),
            ],
            label=f"Go runtime smoke for {job.get('program', job.get('working_dir', 'job'))}",
        )

    csharp_smoke = ctx.manifest.smoke["csharp"]
    print("[5/6] C# build check...")
    projects = sorted((ctx.root / "languages" / "csharp").rglob("*.csproj"))
    for project in projects:
        print(f"  Building {project.relative_to(ctx.root)}")
        run_command(
            [
                "dotnet",
                "build",
                str(project),
                "--nologo",
                "--verbosity",
                "quiet",
                "-p:UseAppHost=false",
            ],
            quiet_stdout=True,
            action=f"C# build for {project}",
            timeout_seconds=180,
        )
    build_csharp_exercises(ctx)

    print("[6/6] C# runtime smoke...")
    for project in csharp_smoke["example_projects"]:
        print(f"  Running {project}")
        project_path = repo_path(ctx, project)
        run_command(
            ["dotnet", str(csharp_output_dll(project_path))],
            quiet_stdout=True,
            action=f"C# runtime smoke for {project}",
            timeout_seconds=30,
        )
    for job in csharp_smoke["stdin_runs"]:
        print(f"  Running {job.get('project', job.get('working_dir', 'job'))}")
        smoke_runtime_job(
            ctx,
            job,
            command_builder=lambda current_job, working_dir: [
                "dotnet",
                str(csharp_output_dll(resolve_job_path(ctx, working_dir, current_job["project"]))),
            ],
            label=f"C# runtime smoke for {job.get('project', job.get('working_dir', 'job'))}",
            timeout_seconds=30,
        )

    print("Multi-language smoke checks passed.")


def verify_repo(ctx: RepoContext) -> None:
    python_cmd = find_python_command()

    print("[1/6] Checking markdown links...")
    run_command([python_cmd, str(ctx.scripts_dir / "check-links.py")], action="Markdown link check")

    print("[2/6] Checking README structure...")
    check_readme_structure(ctx)

    print("[3/6] Checking module completeness...")
    check_module_completeness(ctx)

    print("[4/6] Checking checkpoint completeness...")
    check_checkpoint_completeness(ctx)

    print("[5/6] Checking documentation sync...")
    check_doc_sync(ctx)

    print("[6/6] Compiling C++ files...")
    build_all(ctx)

    print("Repository verification completed successfully.")
