from __future__ import annotations

import argparse
import json
import os
import re
import shlex
import shutil
import subprocess
import sys
import tempfile
from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from time import perf_counter
from typing import Any

from .curriculum import CurriculumError, load_curriculum_outcomes, load_learning_checkpoints
from .guidance import GuidanceError, format_hint, load_exercise_guidance
from .links import check_markdown_links
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
    add_simple_command(subparsers, "clean-artifacts", handle_clean_artifacts)
    add_simple_command(subparsers, "check-links", handle_check_links)
    add_simple_command(subparsers, "check-readme-structure", handle_check_readme_structure)
    add_simple_command(subparsers, "check-module-completeness", handle_check_module_completeness)
    add_simple_command(
        subparsers, "check-checkpoint-completeness", handle_check_checkpoint_completeness
    )
    audit_education_quality_parser = subparsers.add_parser("audit-education-quality")
    audit_education_quality_parser.add_argument(
        "--fail-on-findings",
        action="store_true",
        help="Exit non-zero when the audit finds any learner-quality findings.",
    )
    audit_education_quality_parser.add_argument(
        "--fail-on-blocking-findings",
        action="store_true",
        help=(
            "Exit non-zero for blocking findings: boilerplate comments, missing output "
            "markers, or low comment ratio. Oversized files remain advisory."
        ),
    )
    audit_education_quality_parser.set_defaults(func=handle_audit_education_quality)
    check_example_output_contracts_parser = subparsers.add_parser("check-example-output-contracts")
    check_example_output_contracts_parser.add_argument(
        "--language",
        choices=["cpp", "csharp", "go", "java", "python", "typescript"],
        default=None,
    )
    check_example_output_contracts_parser.set_defaults(func=handle_check_example_output_contracts)
    check_exercise_output_contracts_parser = subparsers.add_parser(
        "check-exercise-output-contracts"
    )
    check_exercise_output_contracts_parser.add_argument(
        "--language",
        choices=["cpp", "csharp", "go", "java", "python", "typescript"],
        default=None,
        help="Run only one language track for exercise output contracts.",
    )
    check_exercise_output_contracts_parser.set_defaults(func=handle_check_exercise_output_contracts)
    check_exercise_parser = subparsers.add_parser(
        "check-exercise",
        help="Check one learner exercise submission against its configured cases.",
    )
    check_exercise_parser.add_argument(
        "--language",
        choices=["cpp", "csharp", "go", "java", "python", "typescript"],
        required=True,
    )
    check_exercise_parser.add_argument("--level", required=True)
    check_exercise_parser.add_argument("--module", required=True)
    check_exercise_parser.add_argument("--exercise", choices=["01", "02"], required=True)
    exercise_source_group = check_exercise_parser.add_mutually_exclusive_group()
    exercise_source_group.add_argument(
        "--submission",
        help="Repository-relative path to the source file to check instead of the starter.",
    )
    exercise_source_group.add_argument(
        "--solution",
        action="store_true",
        help="Check the reference solution instead of the starter.",
    )
    check_exercise_parser.set_defaults(func=handle_check_exercise)
    hint_exercise_parser = subparsers.add_parser(
        "hint-exercise",
        help="Show a graduated hint without revealing the reference solution.",
    )
    hint_exercise_parser.add_argument(
        "--language",
        choices=["cpp", "csharp", "go", "java", "python", "typescript"],
        required=True,
    )
    hint_exercise_parser.add_argument("--level", required=True)
    hint_exercise_parser.add_argument("--module", required=True)
    hint_exercise_parser.add_argument("--exercise", choices=["01", "02"], required=True)
    hint_exercise_parser.add_argument("--stage", type=int, choices=[1, 2, 3], required=True)
    hint_exercise_parser.set_defaults(func=handle_hint_exercise)
    add_simple_command(subparsers, "check-exercise-parity", handle_check_exercise_parity)
    add_simple_command(
        subparsers, "check-cross-language-parity", handle_check_cross_language_parity
    )
    add_simple_command(subparsers, "check-doc-sync", handle_check_doc_sync)
    add_simple_command(subparsers, "test-automation", handle_test_automation)
    add_simple_command(subparsers, "lint", handle_lint)
    add_simple_command(subparsers, "smoke-languages", handle_smoke_languages)
    add_simple_command(subparsers, "verify-repo", handle_verify_repo)

    doctor_parser = subparsers.add_parser(
        "doctor", help="Check the required toolchain for one language track."
    )
    doctor_parser.add_argument(
        "--language",
        choices=["cpp", "csharp", "go", "java", "python", "typescript"],
        required=True,
    )
    doctor_parser.set_defaults(func=handle_doctor)

    verify_language_parser = subparsers.add_parser(
        "verify-language", help="Validate one language track without repeating other tracks."
    )
    verify_language_parser.add_argument(
        "--language",
        choices=["cpp", "csharp", "go", "java", "python", "typescript"],
        required=True,
    )
    verify_language_parser.set_defaults(func=handle_verify_language)

    check_checkpoint_parser = subparsers.add_parser(
        "check-checkpoint", help="Check one project or assessment submission."
    )
    check_checkpoint_parser.add_argument(
        "--language",
        choices=["cpp", "csharp", "go", "java", "python", "typescript"],
        required=True,
    )
    check_checkpoint_parser.add_argument("--kind", choices=["project", "assessment"], required=True)
    check_checkpoint_parser.add_argument("--level", required=True)
    checkpoint_source_group = check_checkpoint_parser.add_mutually_exclusive_group()
    checkpoint_source_group.add_argument("--submission")
    checkpoint_source_group.add_argument("--solution", action="store_true")
    check_checkpoint_parser.set_defaults(func=handle_check_checkpoint)

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


def handle_clean_artifacts(ctx: RepoContext, _: argparse.Namespace) -> int:
    clean_artifacts(ctx)
    return 0


def handle_check_links(ctx: RepoContext, _: argparse.Namespace) -> int:
    check_links(ctx)
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


def handle_audit_education_quality(ctx: RepoContext, args: argparse.Namespace) -> int:
    audit_education_quality(
        ctx,
        fail_on_findings=args.fail_on_findings,
        fail_on_blocking_findings=args.fail_on_blocking_findings,
    )
    return 0


def handle_check_example_output_contracts(ctx: RepoContext, args: argparse.Namespace) -> int:
    check_example_output_contracts(ctx, language_filter=args.language)
    return 0


def handle_check_exercise_output_contracts(ctx: RepoContext, args: argparse.Namespace) -> int:
    check_exercise_output_contracts(ctx, language_filter=args.language)
    return 0


def handle_check_exercise(ctx: RepoContext, args: argparse.Namespace) -> int:
    check_learning_exercise(
        ctx,
        language=args.language,
        level=args.level,
        module=args.module,
        exercise_id=args.exercise,
        submission=args.submission,
        use_solution=args.solution,
    )
    return 0


def handle_hint_exercise(ctx: RepoContext, args: argparse.Namespace) -> int:
    show_exercise_hint(
        ctx,
        language=args.language,
        level=args.level,
        module=args.module,
        exercise_id=args.exercise,
        stage=args.stage,
    )
    return 0


def handle_check_exercise_parity(ctx: RepoContext, _: argparse.Namespace) -> int:
    check_exercise_parity(ctx)
    return 0


def handle_check_cross_language_parity(ctx: RepoContext, _: argparse.Namespace) -> int:
    check_cross_language_parity(ctx)
    return 0


def handle_check_doc_sync(ctx: RepoContext, _: argparse.Namespace) -> int:
    check_doc_sync(ctx)
    return 0


def handle_test_automation(ctx: RepoContext, _: argparse.Namespace) -> int:
    test_automation(ctx)
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


def handle_doctor(ctx: RepoContext, args: argparse.Namespace) -> int:
    doctor_language(ctx, args.language)
    return 0


def handle_verify_language(ctx: RepoContext, args: argparse.Namespace) -> int:
    verify_language(ctx, args.language)
    return 0


def handle_check_checkpoint(ctx: RepoContext, args: argparse.Namespace) -> int:
    check_learning_checkpoint(
        ctx,
        language=args.language,
        kind=args.kind,
        level=args.level,
        submission=args.submission,
        use_solution=args.solution,
    )
    return 0


def repo_path(ctx: RepoContext, relative_path: str) -> Path:
    return ctx.root / Path(relative_path)


def show_exercise_hint(
    ctx: RepoContext,
    *,
    language: str,
    level: str,
    module: str,
    exercise_id: str,
    stage: int,
) -> None:
    matches = [
        exercise
        for exercise in load_learning_exercises(ctx)
        if exercise.get("language") == language
        and exercise.get("level") == level
        and exercise.get("module") == module
        and exercise.get("exercise") == exercise_id
    ]
    label = f"{language}/{level}/{module}/{exercise_id}"
    if len(matches) != 1:
        raise AutomationError(f"Expected one configured exercise for hint: {label}")
    outcome_ids = matches[0].get("outcome_ids", [])
    if not isinstance(outcome_ids, list) or not all(isinstance(item, str) for item in outcome_ids):
        raise AutomationError(f"Invalid outcome ids for exercise hint: {label}")
    try:
        module_outcomes = load_curriculum_outcomes(ctx.scripts_dir).get(f"{level}/{module}")
        display_title = (
            module_outcomes.display_titles.get(language, module)
            if module_outcomes is not None
            else module
        )
        guidance = load_exercise_guidance(
            ctx.root,
            language=language,
            level=level,
            module=module,
            exercise_id=exercise_id,
            outcome_ids=tuple(outcome_ids),
        )
        print(f"Module: {display_title} ({module})")
        print(
            format_hint(
                guidance,
                language=language,
                level=level,
                module=module,
                stage=stage,
            )
        )
    except GuidanceError as error:
        raise AutomationError(str(error)) from error


def check_links(ctx: RepoContext) -> None:
    broken_links = check_markdown_links(ctx.root)
    if broken_links:
        print("Broken markdown links found:")
        for failure in broken_links:
            print(f" - {failure}")
        raise AutomationError("Markdown link validation failed.")

    print("No broken markdown links found.")


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


def markdown_sections(path: Path) -> list[tuple[str, int, int]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    sections: list[tuple[str, int, int]] = []
    in_fence = False
    current_heading: str | None = None
    current_start: int | None = None

    for index, raw_line in enumerate(lines, start=1):
        stripped = raw_line.lstrip()
        if re.match(r"^(```|~~~)", stripped):
            in_fence = not in_fence
            continue
        if in_fence:
            continue

        match = re.match(r"^(#{1,6})\s+(.+?)\s*$", raw_line)
        if not match:
            continue

        heading = f"{match.group(1)} {match.group(2)}"
        if current_heading is not None and current_start is not None:
            sections.append((current_heading, current_start, index - 1))
        current_heading = heading
        current_start = index

    if current_heading is not None and current_start is not None:
        sections.append((current_heading, current_start, len(lines)))

    return sections


def get_section_details(path: Path, heading: str) -> tuple[int, int, list[str]] | None:
    lines = path.read_text(encoding="utf-8").splitlines()
    for current_heading, start_line, end_line in markdown_sections(path):
        if current_heading == heading:
            body_end = min(end_line, len(lines))
            body = lines[start_line:body_end]
            return start_line, end_line, body
    return None


def validate_learning_metadata(
    path: Path,
    expected_fields: list[str],
    *,
    before_heading: str,
) -> list[str]:
    failures: list[str] = []
    sections = {heading: (start, end) for heading, start, end in markdown_sections(path)}
    metadata_heading = "## Learning Metadata"

    if metadata_heading not in sections:
        return [f"{path}: missing -> {metadata_heading}"]

    if before_heading not in sections:
        return [f"{path}: missing -> {before_heading}"]

    metadata_start = sections[metadata_heading][0]
    if metadata_start > sections[before_heading][0]:
        failures.append(f"{path}: {metadata_heading} must appear before {before_heading}.")

    details = get_section_details(path, metadata_heading)
    if details is None:
        failures.append(f"{path}: unable to read {metadata_heading} section.")
        return failures

    _, _, body_lines = details
    field_positions: dict[str, int] = {}
    for index, line in enumerate(body_lines):
        for field in expected_fields:
            if field not in field_positions and re.match(
                rf"^- {re.escape(field)}:\s+\S", line.strip()
            ):
                field_positions[field] = index

    missing_fields = [field for field in expected_fields if field not in field_positions]
    if missing_fields:
        failures.append(f"{path}: {metadata_heading} missing fields -> {', '.join(missing_fields)}")
        return failures

    last_position = -1
    for field in expected_fields:
        position = field_positions[field]
        if position < last_position:
            failures.append(f"{path}: {metadata_heading} fields are out of order.")
            break
        last_position = position

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


def find_node_command() -> str:
    resolved = find_command("node", "node.exe")
    if resolved:
        return resolved
    raise AutomationError("Required command not found: node")


def find_npm_command() -> str:
    resolved = find_command("npm", "npm.cmd", "npm.exe")
    if resolved:
        return resolved
    raise AutomationError("Required command not found: npm")


def find_java_tool(tool: str, ctx: RepoContext | None = None) -> str:
    resolved = find_command(tool, f"{tool}.exe")
    if resolved:
        return resolved

    if ctx and ctx.is_windows:
        roots = [
            Path(r"C:\Program Files\Eclipse Adoptium"),
            Path(r"C:\Program Files\Java"),
        ]
        for root in roots:
            if not root.is_dir():
                continue
            matches = sorted(root.glob(f"**/bin/{tool}.exe"), reverse=True)
            if matches:
                return str(matches[0])

    raise AutomationError(f"Required command not found: {tool}")


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
    environment: dict[str, str] | None = None,
    quiet_stdout: bool = False,
    capture_stdout: bool = False,
    action: str | None = None,
    timeout_seconds: float | None = None,
) -> subprocess.CompletedProcess[str]:
    try:
        stdout_target: int | None = None
        if capture_stdout:
            stdout_target = subprocess.PIPE
        elif quiet_stdout:
            stdout_target = subprocess.DEVNULL

        completed = subprocess.run(
            command,
            cwd=str(cwd) if cwd else None,
            env={**os.environ, **environment} if environment else None,
            input=input_text,
            text=True,
            encoding="utf-8",
            errors="replace",
            stdout=stdout_target,
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


def ensure_typescript_tooling(ctx: RepoContext) -> str:
    find_node_command()
    npm = find_npm_command()
    tsc_candidates = [ctx.root / "node_modules" / ".bin" / "tsc"]
    prettier_candidates = [ctx.root / "node_modules" / ".bin" / "prettier"]

    if ctx.is_windows:
        tsc_candidates.append(ctx.root / "node_modules" / ".bin" / "tsc.cmd")
        prettier_candidates.append(ctx.root / "node_modules" / ".bin" / "prettier.cmd")

    tooling_ready = any(path.exists() for path in tsc_candidates) and any(
        path.exists() for path in prettier_candidates
    )
    if not tooling_ready:
        run_command(
            [npm, "ci", "--no-fund", "--no-audit"],
            cwd=ctx.root,
            quiet_stdout=True,
            action="TypeScript dependency restore",
            timeout_seconds=300,
        )

    return npm


def typescript_output_path(ctx: RepoContext, output_root: Path, source_path: Path) -> Path:
    track_root = ctx.root / "languages" / "typescript"
    relative = source_path.resolve().relative_to(track_root.resolve())
    return output_root / relative.with_suffix(".js")


def compile_typescript(
    ctx: RepoContext,
    *,
    out_dir: Path | None = None,
    no_emit: bool = False,
) -> None:
    npm = ensure_typescript_tooling(ctx)
    command = [
        npm,
        "exec",
        "--",
        "tsc",
        "--project",
        str(ctx.root / "languages" / "typescript" / "tsconfig.json"),
    ]
    if out_dir is not None:
        command.extend(["--outDir", str(out_dir)])
    if no_emit:
        command.append("--noEmit")
    run_command(
        command,
        cwd=ctx.root,
        quiet_stdout=True,
        action="TypeScript compilation",
        timeout_seconds=300,
    )


def remove_paths(base_dir: Path, relative_paths: list[str]) -> None:
    for relative in relative_paths:
        candidate = base_dir / relative
        if candidate.is_dir():
            shutil.rmtree(candidate, ignore_errors=True)
        elif candidate.exists():
            candidate.unlink(missing_ok=True)


def clean_artifacts(ctx: RepoContext) -> None:
    removed: list[Path] = []

    def remove_candidate(path: Path) -> None:
        resolved = path.resolve()
        try:
            resolved.relative_to(ctx.root.resolve())
        except ValueError as error:
            raise AutomationError(
                f"Refusing to remove path outside repository: {resolved}"
            ) from error

        if resolved.is_dir():
            shutil.rmtree(resolved)
            removed.append(resolved)
        elif resolved.exists():
            resolved.unlink()
            removed.append(resolved)

    direct_paths = [
        ctx.root / "build",
        ctx.root / ".ruff_cache",
        ctx.root / "compiled_files.txt",
        ctx.root / "compile_errors.txt",
        ctx.root / "core_assessment_report.txt",
    ]
    for direct_path in direct_paths:
        remove_candidate(direct_path)

    for pattern in (
        "*.class",
        "*.exe",
        "*.out",
        "*.o",
        "*.obj",
        "scores.txt",
        "report.txt",
        "core_assessment_report.txt",
    ):
        for path in ctx.root.rglob(pattern):
            if "node_modules" not in path.parts and ".git" not in path.parts:
                remove_candidate(path)

    for directory_name in ("bin", "obj", "__pycache__"):
        for path in ctx.root.rglob(directory_name):
            if path.is_dir() and "node_modules" not in path.parts and ".git" not in path.parts:
                remove_candidate(path)

    if removed:
        print(f"Removed {len(removed)} generated artifact path(s).")
    else:
        print("No generated artifact paths found.")


def resolve_job_path(ctx: RepoContext, working_dir: Path, raw_path: str) -> Path:
    candidate = Path(raw_path)
    if candidate.is_absolute():
        return candidate
    if working_dir != ctx.root and (working_dir / candidate).exists():
        return working_dir / candidate
    return ctx.root / candidate


def go_target_arguments(path: Path) -> list[str]:
    if path.is_dir():
        return [str(candidate) for candidate in sorted(path.glob("*.go"))]
    if path.suffix == ".go":
        companions = [
            candidate
            for candidate in sorted(path.parent.glob("*.go"))
            if candidate == path or not go_file_has_main(candidate)
        ]
        if len(companions) > 1:
            return [str(candidate) for candidate in companions]
    return [str(path)]


def go_file_has_main(path: Path) -> bool:
    return bool(re.search(r"(?m)^func\s+main\s*\(", path.read_text(encoding="utf-8")))


def go_directory_needs_package_build(directory: Path) -> bool:
    go_files = sorted(directory.glob("*.go"))
    if len(go_files) <= 1:
        return False

    if not any(path.name != "main.go" for path in go_files):
        return False

    main_function_count = 0
    for path in go_files:
        main_function_count += int(go_file_has_main(path))

    return main_function_count <= 1


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


def iter_example_code_files(ctx: RepoContext) -> list[Path]:
    files: list[Path] = []
    excluded_dirs = {"obj", "bin", "build"}
    extensions = {".cpp", ".cs", ".go", ".java", ".py", ".ts"}

    for path in (ctx.root / "languages").rglob("*"):
        if not path.is_file():
            continue
        if path.suffix not in extensions:
            continue
        if "example" not in path.parts:
            continue
        if excluded_dirs.intersection(path.parts):
            continue
        files.append(path)

    return sorted(set(files))


def expected_modules_for_language_level(ctx: RepoContext, language: str, level: str) -> list[str]:
    config = ctx.manifest.languages[language]
    module_overrides = config.get("module_overrides", {})
    if level in module_overrides:
        return list(module_overrides[level])
    return list(ctx.manifest.module_order[level])


def language_example_main(config: dict[str, Any]) -> str:
    return str(config.get("example_main", f"main.{config['extension']}"))


def language_exercise_file(config: dict[str, Any], exercise_id: str) -> str:
    exercise_files = config.get("exercise_files", {})
    return str(exercise_files.get(exercise_id, f"{exercise_id}.{config['extension']}"))


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
        failures.extend(
            validate_learning_metadata(
                readme,
                ctx.manifest.learning_metadata["module"],
                before_heading="## Quick Run",
            )
        )

    level_readmes: list[Path] = []
    for language, config in ctx.manifest.languages.items():
        for level in config.get("module_levels", []):
            readme = ctx.root / "languages" / language / level / "README.md"
            if readme.is_file():
                level_readmes.append(readme)

    for readme in level_readmes:
        failures.extend(
            require_markdown_headings(
                readme,
                ["## Learning Metadata", "## Module Order", "## Level Outcomes", "## Done When"],
            )
        )
        failures.extend(
            validate_learning_metadata(
                readme,
                ctx.manifest.learning_metadata["level"],
                before_heading="## Module Order",
            )
        )

    if failures:
        print("README structure validation failed:")
        for failure in failures:
            print(f" - {failure}")
        raise AutomationError("README structure validation failed.")

    print(
        "README structure validation passed for "
        f"{len(readmes)} module files and {len(level_readmes)} level files."
    )


def check_module_completeness(ctx: RepoContext) -> None:
    failures: list[str] = []
    module_count = 0

    for language, config in ctx.manifest.languages.items():
        module_levels = config.get("module_levels", [])
        example_main = language_example_main(config)
        exercise01_name = language_exercise_file(config, "01")
        exercise02_name = language_exercise_file(config, "02")

        for level in module_levels:
            level_path = ctx.root / "languages" / language / level
            if not level_path.is_dir():
                continue

            expected_modules = expected_modules_for_language_level(ctx, language, level)
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
                main_path = example_dir / example_main
                exercise01 = exercises_dir / exercise01_name
                exercise02 = exercises_dir / exercise02_name

                if not readme_path.is_file():
                    failures.append(f"{module_dir}: missing README.md")
                    continue
                if not example_dir.is_dir():
                    failures.append(f"{module_dir}: missing example/ directory")
                if not exercises_dir.is_dir():
                    failures.append(f"{module_dir}: missing exercises/ directory")
                if not main_path.is_file():
                    failures.append(f"{module_dir}: missing example/{example_main}")
                if not exercise01.is_file():
                    failures.append(f"{module_dir}: missing exercises/{exercise01_name}")
                if not exercise02.is_file():
                    failures.append(f"{module_dir}: missing exercises/{exercise02_name}")

                heading_failures = require_markdown_headings(
                    readme_path, ctx.manifest.required_readme_headings
                )
                for failure in heading_failures:
                    suffix = failure.split(": ", 1)[1] if ": " in failure else failure
                    failures.append(f"{module_dir}: README {suffix}")
                metadata_failures = validate_learning_metadata(
                    readme_path,
                    ctx.manifest.learning_metadata["module"],
                    before_heading="## Quick Run",
                )
                for failure in metadata_failures:
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
    try:
        configured_checkpoints = load_learning_checkpoints(ctx.scripts_dir)
        outcomes_by_module = load_curriculum_outcomes(ctx.scripts_dir)
    except CurriculumError as error:
        raise AutomationError(str(error)) from error
    configured_by_key: dict[tuple[str, str, str], dict[str, Any]] = {}
    for checkpoint in configured_checkpoints:
        key = (
            str(checkpoint.get("language")),
            str(checkpoint.get("kind")),
            str(checkpoint.get("level")),
        )
        if key in configured_by_key:
            failures.append(
                "scripts/learning_checkpoints.json: duplicate checkpoint -> " + "/".join(key)
            )
        configured_by_key[key] = checkpoint

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
                else:
                    metadata_failures = validate_learning_metadata(
                        readme_path,
                        ctx.manifest.learning_metadata["checkpoint"],
                        before_heading="## Quick Run",
                    )
                    for failure in metadata_failures:
                        suffix = failure.split(": ", 1)[1] if ": " in failure else failure
                        failures.append(f"{checkpoint_dir}: README {suffix}")

                checkpoint_main = config.get("checkpoint_main") or (
                    "main.cpp" if language == "cpp" else None
                )
                starter_dir = checkpoint_dir / "starter"
                solution_dir = checkpoint_dir / "solutions"
                for source_kind, source_dir in (
                    ("starter", starter_dir),
                    ("solution", solution_dir),
                ):
                    if not source_dir.is_dir():
                        failures.append(f"{checkpoint_dir}: missing {source_dir.name}/ directory")
                        continue
                    if checkpoint_main and not (source_dir / checkpoint_main).is_file():
                        failures.append(
                            f"{checkpoint_dir}: missing {source_dir.name}/{checkpoint_main}"
                        )
                    if language == "csharp" and not any(source_dir.glob("*.csproj")):
                        failures.append(
                            f"{checkpoint_dir}: missing {source_dir.name}/ .csproj file"
                        )

                singular_kind = "project" if kind == "projects" else "assessment"
                key = (language, singular_kind, checkpoint_name)
                checkpoint = configured_by_key.get(key)
                label = "/".join(key)
                if checkpoint is None:
                    failures.append(
                        f"scripts/learning_checkpoints.json: missing checkpoint -> {label}"
                    )
                    continue
                expected_starter = f"languages/{language}/{kind}/{checkpoint_name}/starter"
                expected_solution = f"languages/{language}/{kind}/{checkpoint_name}/solutions"
                if checkpoint.get("starter") != expected_starter:
                    failures.append(
                        f"scripts/learning_checkpoints.json: {label} starter must be "
                        f"{expected_starter}"
                    )
                if checkpoint.get("solution") != expected_solution:
                    failures.append(
                        f"scripts/learning_checkpoints.json: {label} solution must be "
                        f"{expected_solution}"
                    )
                if checkpoint.get("entrypoint") != checkpoint_main:
                    failures.append(
                        f"scripts/learning_checkpoints.json: {label} has wrong entrypoint"
                    )
                expected_outcomes = [
                    outcome_id
                    for module_key, module_outcomes in outcomes_by_module.items()
                    if module_key.startswith(f"{checkpoint_name}/")
                    for outcome_id in module_outcomes.ids
                ]
                outcome_ids = checkpoint.get("outcome_ids")
                if not isinstance(outcome_ids, list) or not 2 <= len(outcome_ids) <= 4:
                    failures.append(
                        f"scripts/learning_checkpoints.json: {label} needs 2 to 4 outcomes"
                    )
                elif not set(outcome_ids).issubset(set(expected_outcomes)):
                    failures.append(
                        "scripts/learning_checkpoints.json: "
                        f"{label} uses outcomes outside its level"
                    )
                if checkpoint.get("milestones") is not (kind == "projects"):
                    failures.append(
                        f"scripts/learning_checkpoints.json: {label} milestone policy mismatch"
                    )
                expected_starter_mode = "guided" if kind == "projects" else "independent"
                expected_route_role = "guided" if kind == "projects" else "both"
                if checkpoint.get("starter_mode") != expected_starter_mode:
                    failures.append(
                        "scripts/learning_checkpoints.json: "
                        f"{label} starter_mode must be {expected_starter_mode}"
                    )
                if checkpoint.get("route_role") != expected_route_role:
                    failures.append(
                        "scripts/learning_checkpoints.json: "
                        f"{label} route_role must be {expected_route_role}"
                    )
                cases = checkpoint.get("cases")
                if not isinstance(cases, list) or not cases:
                    failures.append(f"scripts/learning_checkpoints.json: no cases -> {label}")
                else:
                    if len(cases) < 3:
                        failures.append(
                            f"scripts/learning_checkpoints.json: fewer than three cases -> {label}"
                        )
                    case_names: set[str] = set()
                    covered_behaviors: set[str] = set()
                    for index, case in enumerate(cases, start=1):
                        if not isinstance(case, dict) or not isinstance(case.get("name"), str):
                            failures.append(
                                "scripts/learning_checkpoints.json: "
                                f"invalid case {index} -> {label}"
                            )
                            continue
                        case_name = case["name"]
                        if case_name in case_names:
                            failures.append(
                                f"scripts/learning_checkpoints.json: duplicate case name "
                                f"'{case_name}' -> {label}"
                            )
                        case_names.add(case_name)
                        covered_behaviors.update(
                            value for value in case.get("covers", []) if isinstance(value, str)
                        )
                        if case.get("oracle_solution") is True and not has_valid_oracle_waiver(
                            case
                        ):
                            failures.append(
                                "scripts/learning_checkpoints.json: oracle_solution requires "
                                f"oracle_waiver in case {index} -> {label}"
                            )
                        if not (
                            case.get("required_stdout_equals")
                            or case.get("required_stdout_contains")
                            or case.get("required_stdout_patterns")
                            or case.get("oracle_solution") is True
                        ):
                            failures.append(
                                "scripts/learning_checkpoints.json: "
                                f"case {index} has no assertions or oracle -> {label}"
                            )
                    for expected_behavior in ("normal", "boundary", "error", "state", "resources"):
                        if expected_behavior not in covered_behaviors:
                            failures.append(
                                "scripts/learning_checkpoints.json: missing "
                                f"'{expected_behavior}' coverage -> {label}"
                            )
                if readme_path.is_file() and isinstance(outcome_ids, list):
                    readme_text = readme_path.read_text(encoding="utf-8")
                    for outcome_id in outcome_ids:
                        if f"- `{outcome_id}`" not in readme_text:
                            failures.append(f"{readme_path}: missing outcome id -> {outcome_id}")

                if checkpoint_main:
                    starter_main = starter_dir / checkpoint_main
                    solution_main = solution_dir / checkpoint_main
                    if starter_main.is_file() and solution_main.is_file():
                        starter_text = starter_main.read_text(encoding="utf-8")
                        solution_text = solution_main.read_text(encoding="utf-8")
                        if starter_text == solution_text:
                            failures.append(f"{checkpoint_dir}: starter equals solution")
                        if has_template_narration(starter_text) or has_template_narration(
                            solution_text
                        ):
                            failures.append(f"{checkpoint_dir}: template narration remains")
                    if starter_main.is_file():
                        starter_text = starter_main.read_text(encoding="utf-8")
                        if "TODO" not in starter_text:
                            failures.append(f"{checkpoint_dir}: starter entrypoint has no TODO")
                        if kind == "projects" and has_generic_starter_prompt(starter_text):
                            failures.append(f"{checkpoint_dir}: project starter has a generic TODO")
                        if kind == "projects" and guided_todo_count(starter_text) < 3:
                            failures.append(
                                f"{checkpoint_dir}: guided project starter needs TODO 1, "
                                "TODO 2, and TODO 3"
                            )

    if checkpoint_count == 0:
        raise AutomationError("No checkpoint directories found for completeness validation.")

    if len(configured_by_key) != checkpoint_count:
        failures.append(
            "scripts/learning_checkpoints.json: expected "
            f"{checkpoint_count} checkpoints, found {len(configured_by_key)}"
        )

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

        for level in config.get("module_levels", []):
            level_readme_path = ctx.root / "languages" / language / level / "README.md"
            if not level_readme_path.is_file():
                failures.append(f"{level_readme_path}: missing README.md")
                continue
            failures.extend(
                validate_learning_metadata(
                    level_readme_path,
                    ctx.manifest.learning_metadata["level"],
                    before_heading="## Module Order",
                )
            )

    parity_path = repo_path(ctx, ctx.manifest.docs["parity_matrix"]["path"])
    parity_text = ensure_text_file(parity_path)
    for marker in ctx.manifest.docs["parity_matrix"]["markers"]:
        if marker not in parity_text:
            failures.append(f"{parity_path}: missing marker -> {marker}")

    concept_index_config = ctx.manifest.docs.get("concept_index")
    if concept_index_config:
        concept_index_path = repo_path(ctx, concept_index_config["path"])
        concept_index_text = ensure_text_file(concept_index_path)

        for marker in concept_index_config.get("markers", []):
            if marker not in concept_index_text:
                failures.append(f"{concept_index_path}: missing marker -> {marker}")

        for level, modules in ctx.manifest.module_order.items():
            for module in modules:
                row_marker = f"| {module} |"
                if row_marker not in concept_index_text:
                    failures.append(f"{concept_index_path}: missing concept row -> {module}")

                for language, config in ctx.manifest.languages.items():
                    if level not in config.get("module_levels", []):
                        continue
                    if module not in expected_modules_for_language_level(ctx, language, level):
                        continue

                    expected_path = f"languages/{language}/{level}/{module}/README.md"
                    if expected_path not in concept_index_text:
                        failures.append(
                            f"{concept_index_path}: missing module link -> {expected_path}"
                        )

        for kind in ctx.manifest.checkpoint_kinds:
            for language, config in ctx.manifest.languages.items():
                for level in config.get("checkpoints", {}).get(kind, []):
                    expected_path = f"languages/{language}/{kind}/{level}/README.md"
                    if expected_path not in concept_index_text:
                        failures.append(
                            f"{concept_index_path}: missing checkpoint link -> {expected_path}"
                        )

    if failures:
        print("Documentation sync validation failed:")
        for failure in failures:
            print(f" - {failure}")
        raise AutomationError("Documentation sync validation failed.")

    print("Documentation sync validation passed.")


def check_example_comments(ctx: RepoContext) -> None:
    example_files = iter_example_code_files(ctx)
    if not example_files:
        raise AutomationError("No example code files found for comment validation.")

    failures: list[str] = []
    for path in example_files:
        text = path.read_text(encoding="utf-8")
        comment_pattern = r"(?m)^\s*#" if path.suffix == ".py" else r"(?m)^\s*//"
        if not re.search(comment_pattern, text):
            failures.append(f"{path}: missing example comments")

    if failures:
        print("Example comment validation failed:")
        for failure in failures:
            print(f" - {failure}")
        raise AutomationError("Example comment validation failed.")

    print(f"Example comment validation passed for {len(example_files)} files.")


def module_example_main_files(ctx: RepoContext) -> list[tuple[str, str, str, Path]]:
    files: list[tuple[str, str, str, Path]] = []
    for language, level, module_dir in iter_module_directories(ctx):
        main_file = module_dir / "example" / language_example_main(ctx.manifest.languages[language])
        if not main_file.is_file():
            continue
        files.append((language, level, module_dir.name, main_file))
    return sorted(files, key=lambda item: (item[0], item[1], item[2]))


def percentile(values: list[int], fraction: float) -> float:
    if not values:
        return 0.0
    ordered = sorted(values)
    if len(ordered) == 1:
        return float(ordered[0])
    position = (len(ordered) - 1) * fraction
    lower = int(position)
    upper = min(lower + 1, len(ordered) - 1)
    weight = position - lower
    return ordered[lower] * (1.0 - weight) + ordered[upper] * weight


def output_pattern_for_file(path: Path) -> re.Pattern[str]:
    suffix = path.suffix
    if suffix == ".py":
        return re.compile(r"^\s*print\(", re.IGNORECASE)
    if suffix == ".go":
        return re.compile(r"\bfmt\.(Print|Printf|Println)\s*\(")
    if suffix == ".cs":
        return re.compile(r"\bConsole\.(Write|WriteLine)\s*\(")
    if suffix == ".cpp":
        return re.compile(r"\bcout\s*<<")
    if suffix == ".java":
        return re.compile(r"\bSystem\.out\.(print|printf|println)\s*\(")
    return re.compile(r"\bconsole\.(log|error|warn)\s*\(", re.IGNORECASE)


def comment_pattern_for_file(path: Path) -> re.Pattern[str]:
    return re.compile(r"^\s*#") if path.suffix == ".py" else re.compile(r"^\s*//")


GENERIC_STARTER_PATTERNS = (
    "implement the readme specification",
    "implement this exercise",
    "implement this checkpoint",
    "implement the requested task",
    "solve exercise 01 here",
    "solve exercise 02 here",
)

TEMPLATE_NARRATION_PATTERNS = (
    "exercise guide:",
    "define the reusable pieces first so",
    "run one deterministic scenario so",
    "run one direct scenario at the top level so",
    "build the sample state first, then",
    "helper setup for",
    "walk through one fixed scenario so",
    "prepare sample inputs that exercise the key",
    "report output values so learners can verify",
)


def has_generic_starter_prompt(text: str) -> bool:
    lowered = text.lower()
    return any(pattern in lowered for pattern in GENERIC_STARTER_PATTERNS)


def has_template_narration(text: str) -> bool:
    lowered = text.lower()
    return any(pattern in lowered for pattern in TEMPLATE_NARRATION_PATTERNS)


def guided_todo_count(text: str) -> int:
    return len(re.findall(r"\bTODO\s+[123]\s*:", text, re.IGNORECASE))


def has_valid_oracle_waiver(case: dict[str, Any]) -> bool:
    waiver = case.get("oracle_waiver")
    return isinstance(waiver, str) and bool(waiver.strip())


def education_debt_counts(ctx: RepoContext) -> dict[str, int]:
    exercises = load_learning_exercises(ctx)
    checkpoints = load_learning_checkpoints(ctx.scripts_dir)

    generic_exercise_starters = 0
    weak_guided_exercise_starters = 0
    exercise_oracle_cases = 0
    exercise_contracts_with_fewer_than_three_cases = 0
    exercise_shared_execution_facets = 0
    for exercise in exercises:
        starter = repo_path(ctx, str(exercise.get("starter", "")))
        text = starter.read_text(encoding="utf-8") if starter.is_file() else ""
        generic_exercise_starters += int(has_generic_starter_prompt(text))
        weak_guided_exercise_starters += int(guided_todo_count(text) < 3)
        cases = exercise.get("cases", [])
        exercise_contracts_with_fewer_than_three_cases += int(
            not isinstance(cases, list) or len(cases) < 3
        )
        exercise_shared_execution_facets += sum(
            int(case.get("shared_execution") is True) for case in cases if isinstance(case, dict)
        )
        exercise_oracle_cases += sum(
            int(case.get("oracle_solution") is True) for case in cases if isinstance(case, dict)
        )

    generic_project_starters = 0
    weak_guided_project_starters = 0
    checkpoint_oracle_cases = 0
    checkpoint_single_case_contracts = 0
    checkpoint_shared_execution_facets = 0
    for checkpoint in checkpoints:
        cases = checkpoint.get("cases", [])
        if isinstance(cases, list):
            checkpoint_single_case_contracts += int(len(cases) < 3)
            checkpoint_shared_execution_facets += sum(
                int(case.get("shared_execution") is True)
                for case in cases
                if isinstance(case, dict)
            )
            checkpoint_oracle_cases += sum(
                int(case.get("oracle_solution") is True) for case in cases if isinstance(case, dict)
            )
        if checkpoint.get("kind") != "project":
            continue
        starter = repo_path(ctx, str(checkpoint.get("starter", ""))) / str(
            checkpoint.get("entrypoint", "")
        )
        text = starter.read_text(encoding="utf-8") if starter.is_file() else ""
        generic_project_starters += int(has_generic_starter_prompt(text))
        weak_guided_project_starters += int(guided_todo_count(text) < 3)

    missing_cross_language_notes = 0
    for _language, _level, module_dir in iter_module_directories(ctx):
        readme = module_dir / "README.md"
        if not readme.is_file() or "## Cross-Language Notes" not in readme.read_text(
            encoding="utf-8"
        ):
            missing_cross_language_notes += 1

    return {
        "generic_exercise_starters": generic_exercise_starters,
        "weak_guided_exercise_starters": weak_guided_exercise_starters,
        "generic_project_starters": generic_project_starters,
        "weak_guided_project_starters": weak_guided_project_starters,
        "missing_cross_language_notes": missing_cross_language_notes,
        "exercise_oracle_cases": exercise_oracle_cases,
        "exercise_contracts_with_fewer_than_three_cases": (
            exercise_contracts_with_fewer_than_three_cases
        ),
        "exercise_shared_execution_facets": exercise_shared_execution_facets,
        "checkpoint_oracle_cases": checkpoint_oracle_cases,
        "checkpoint_contracts_with_fewer_than_three_cases": checkpoint_single_case_contracts,
        "checkpoint_shared_execution_facets": checkpoint_shared_execution_facets,
    }


def audit_education_quality(
    ctx: RepoContext,
    *,
    fail_on_findings: bool = False,
    fail_on_blocking_findings: bool = False,
) -> None:
    module_examples = module_example_main_files(ctx)
    if not module_examples:
        raise AutomationError("No module example main files were found for education audit.")

    waiver_path = ctx.scripts_dir / "education_quality_waivers.json"
    waiver_payload = json.loads(waiver_path.read_text(encoding="utf-8"))
    waivers = waiver_payload.get("waivers", {})
    if not isinstance(waivers, dict):
        raise AutomationError(f"{waiver_path}: expected a 'waivers' object.")

    boilerplate_patterns = [
        re.compile(r"Define the reusable pieces first so", re.IGNORECASE),
        re.compile(r"Run one deterministic scenario so", re.IGNORECASE),
        re.compile(r"Run one direct scenario at the top level so", re.IGNORECASE),
        re.compile(r"Build the sample state first, then", re.IGNORECASE),
        re.compile(
            r"Print the observed state here so learners can (connect|match)",
            re.IGNORECASE,
        ),
        re.compile(r"Why it matters:\s*practicing", re.IGNORECASE),
        re.compile(r"Helper setup for", re.IGNORECASE),
        re.compile(r"Walk through one fixed scenario so", re.IGNORECASE),
        re.compile(r"Prepare sample inputs that exercise the key", re.IGNORECASE),
        re.compile(r"Report output values so learners can verify", re.IGNORECASE),
    ]
    output_marker_pattern = re.compile(
        r"(print|output|report|expected|actual|verify|summary|observed)",
        re.IGNORECASE,
    )

    file_rows: list[dict[str, Any]] = []
    level_line_counts: dict[str, list[int]] = defaultdict(list)

    for language, level, module, path in module_examples:
        text = path.read_text(encoding="utf-8")
        lines = text.splitlines()
        non_blank_lines = [line for line in lines if line.strip()]
        comment_pattern = comment_pattern_for_file(path)
        output_pattern = output_pattern_for_file(path)

        comment_lines = [line for line in lines if comment_pattern.match(line)]
        has_output = any(output_pattern.search(line) for line in lines)
        has_output_marker = any(
            comment_pattern.match(line) and output_marker_pattern.search(line) for line in lines
        )
        boilerplate_hits = [
            line.strip()
            for line in lines
            if comment_pattern.match(line)
            and any(pattern.search(line) for pattern in boilerplate_patterns)
        ]

        non_blank_count = len(non_blank_lines)
        comment_count = len(comment_lines)
        comment_ratio = 0.0 if non_blank_count == 0 else comment_count / non_blank_count
        level_line_counts[level].append(non_blank_count)

        relative_path = str(path.relative_to(ctx.root)).replace("\\", "/")
        file_rows.append(
            {
                "path": relative_path,
                "language": language,
                "level": level,
                "module": module,
                "non_blank_lines": non_blank_count,
                "comment_lines": comment_count,
                "comment_ratio": round(comment_ratio, 3),
                "boilerplate_hits": boilerplate_hits,
                "boilerplate_hit_count": len(boilerplate_hits),
                "has_output_statements": has_output,
                "has_observable_output_marker": has_output_marker,
                "missing_observable_output_marker": bool(has_output and not has_output_marker),
                "size_waiver": waivers.get(relative_path),
            }
        )

    level_thresholds: dict[str, dict[str, float]] = {}
    for level, values in level_line_counts.items():
        median = percentile(values, 0.5)
        p75 = percentile(values, 0.75)
        oversized_threshold = max(p75 + 10.0, median * 1.35)
        level_thresholds[level] = {
            "median_non_blank_lines": round(median, 2),
            "p75_non_blank_lines": round(p75, 2),
            "oversized_threshold": round(oversized_threshold, 2),
        }

    oversized_count = 0
    waived_oversized_count = 0
    low_comment_ratio_count = 0
    missing_output_marker_count = 0
    boilerplate_file_count = 0

    for row in file_rows:
        threshold = level_thresholds[row["level"]]["oversized_threshold"]
        row["oversized_for_level"] = bool(row["non_blank_lines"] > threshold)
        if row["oversized_for_level"]:
            if row["size_waiver"]:
                waived_oversized_count += 1
            else:
                oversized_count += 1
        if row["comment_ratio"] < 0.12:
            low_comment_ratio_count += 1
        if row["missing_observable_output_marker"]:
            missing_output_marker_count += 1
        if row["boilerplate_hit_count"] > 0:
            boilerplate_file_count += 1

    timestamp = datetime.now(timezone.utc).isoformat(timespec="seconds")
    reports_dir = ctx.root / "build" / "reports"
    reports_dir.mkdir(parents=True, exist_ok=True)
    markdown_path = reports_dir / "education-quality-report.md"
    json_path = reports_dir / "education-quality-report.json"

    summary = {
        "generated_at_utc": timestamp,
        "total_files": len(file_rows),
        "files_with_boilerplate_hits": boilerplate_file_count,
        "files_missing_observable_output_marker": missing_output_marker_count,
        "files_low_comment_ratio": low_comment_ratio_count,
        "files_oversized_for_level": oversized_count,
        "files_oversized_with_waiver": waived_oversized_count,
        "low_comment_ratio_threshold": 0.12,
        "level_thresholds": level_thresholds,
    }

    baseline_path = ctx.scripts_dir / "education_quality_baseline.json"
    baseline = json.loads(baseline_path.read_text(encoding="utf-8"))
    allowed_debt = baseline.get("maximum_counts", {})
    current_debt = education_debt_counts(ctx)
    debt_regressions = [
        f"{name}: current {count} exceeds baseline {allowed_debt.get(name, 0)}"
        for name, count in current_debt.items()
        if count > allowed_debt.get(name, 0)
    ]
    summary["education_debt"] = current_debt
    summary["education_debt_baseline"] = allowed_debt

    json_path.write_text(
        json.dumps({"summary": summary, "files": file_rows}, indent=2),
        encoding="utf-8",
    )

    lines: list[str] = []
    lines.append("# Education Quality Audit Report")
    lines.append("")
    lines.append(f"Generated (UTC): {timestamp}")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append(f"- Total module example entry files: {summary['total_files']}")
    lines.append(f"- Files with boilerplate comment hits: {summary['files_with_boilerplate_hits']}")
    lines.append(
        "- Files missing observable output explanation markers: "
        f"{summary['files_missing_observable_output_marker']}"
    )
    lines.append(
        f"- Files below comment ratio threshold ({summary['low_comment_ratio_threshold']:.2f}): "
        f"{summary['files_low_comment_ratio']}"
    )
    lines.append(f"- Files oversized for level norms: {summary['files_oversized_for_level']}")
    lines.append(
        f"- Oversized files covered by an educational waiver: "
        f"{summary['files_oversized_with_waiver']}"
    )
    lines.append("- Educational debt (current / allowed):")
    for name, count in current_debt.items():
        lines.append(f"  - `{name}`: {count} / {allowed_debt.get(name, 0)}")
    lines.append("")
    lines.append("## Level Size Thresholds")
    lines.append("")
    lines.append("| Level | Median | P75 | Oversized Threshold |")
    lines.append("| --- | ---: | ---: | ---: |")
    for level in sorted(level_thresholds):
        values = level_thresholds[level]
        lines.append(
            f"| {level} | {values['median_non_blank_lines']:.2f} | "
            f"{values['p75_non_blank_lines']:.2f} | {values['oversized_threshold']:.2f} |"
        )
    lines.append("")
    lines.append("## Priority Findings")
    lines.append("")
    lines.append(
        "| Path | Comment Ratio | Boilerplate Hits | Missing Output Marker | Oversized | Waived |"
    )
    lines.append("| --- | ---: | ---: | ---: | ---: | ---: |")
    findings = [
        row
        for row in file_rows
        if row["boilerplate_hit_count"] > 0
        or row["missing_observable_output_marker"]
        or row["comment_ratio"] < 0.12
        or (row["oversized_for_level"] and not row["size_waiver"])
    ]
    blocking_findings = [
        row
        for row in file_rows
        if row["boilerplate_hit_count"] > 0
        or row["missing_observable_output_marker"]
        or row["comment_ratio"] < 0.12
    ]
    findings.sort(
        key=lambda row: (
            not row["missing_observable_output_marker"],
            row["comment_ratio"],
            -row["boilerplate_hit_count"],
            -row["non_blank_lines"],
        )
    )
    for row in findings[:80]:
        lines.append(
            f"| {row['path']} | {row['comment_ratio']:.3f} | {row['boilerplate_hit_count']} | "
            f"{'yes' if row['missing_observable_output_marker'] else 'no'} | "
            f"{'yes' if row['oversized_for_level'] else 'no'} | "
            f"{'yes' if row['size_waiver'] else 'no'} |"
        )
    if not findings:
        lines.append("| _No findings_ | - | - | - | - | - |")
    lines.append("")
    lines.append("## Output")
    lines.append("")
    lines.append(f"- JSON: `{json_path.relative_to(ctx.root).as_posix()}`")
    lines.append(f"- Markdown: `{markdown_path.relative_to(ctx.root).as_posix()}`")
    lines.append(
        "- This command is advisory by default. Use `--fail-on-blocking-findings` "
        "to fail on low-comment, missing-output-marker, or boilerplate findings. "
        "Use `--fail-on-findings` to make every finding fail."
    )
    lines.append("")

    markdown_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Education quality audit completed for {len(file_rows)} module examples.")
    print(f"Report (markdown): {markdown_path.relative_to(ctx.root).as_posix()}")
    print(f"Report (json): {json_path.relative_to(ctx.root).as_posix()}")

    if fail_on_findings and findings:
        raise AutomationError(
            "Education quality audit found "
            f"{len(findings)} file(s) with learner-quality findings. "
            f"See {markdown_path.relative_to(ctx.root).as_posix()}."
        )
    if debt_regressions:
        raise AutomationError("Education debt baseline regressed: " + "; ".join(debt_regressions))
    if fail_on_blocking_findings and blocking_findings:
        raise AutomationError(
            "Education quality audit found "
            f"{len(blocking_findings)} blocking learner-quality finding(s). "
            f"See {markdown_path.relative_to(ctx.root).as_posix()}."
        )


def lint_repo(ctx: RepoContext) -> None:
    lint_config = ctx.manifest.lint

    print("[1/6] C++ formatting check...")
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

    print("[2/6] Python lint and format check...")
    python_cmd = find_python_command()
    python_paths = [str(repo_path(ctx, path)) for path in lint_config["python"]["paths"]]
    run_command([python_cmd, "-m", "ruff", "check", *python_paths], action="Python lint check")
    run_command(
        [python_cmd, "-m", "ruff", "format", "--check", *python_paths], action="Python format check"
    )

    print("[3/6] Go formatting check...")
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

    print("[4/6] C# formatting check...")
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

    print("[5/6] TypeScript formatting and type check...")
    npm = ensure_typescript_tooling(ctx)
    prettier_patterns = [
        f"{root}/**/*{extension}"
        for root in lint_config["typescript"]["roots"]
        for extension in lint_config["typescript"]["extensions"]
    ]
    run_command(
        [npm, "exec", "--", "prettier", "--check", *prettier_patterns],
        cwd=ctx.root,
        action="TypeScript formatting check",
        timeout_seconds=300,
    )
    compile_typescript(ctx, no_emit=True)

    print("[6/6] Java source style check...")
    java_config = lint_config.get("java")
    if java_config:
        java_files = enumerate_source_files(
            ctx,
            roots=java_config["roots"],
            extensions=java_config["extensions"],
            exclude_dirs=java_config.get("exclude_dirs", []),
        )
        java_failures: list[str] = []
        for source in java_files:
            for line_number, line in enumerate(
                source.read_text(encoding="utf-8").splitlines(), start=1
            ):
                if "\t" in line:
                    java_failures.append(f"{source}:{line_number}: tab indentation")
                if line.rstrip() != line:
                    java_failures.append(f"{source}:{line_number}: trailing whitespace")
        if java_failures:
            print("Java source style check failed:")
            for failure in java_failures:
                print(f" - {failure}")
            raise AutomationError("Java source style check failed.")

    print("Lint checks passed.")


def build_all(ctx: RepoContext) -> None:
    cpp_files = sorted((ctx.root / "languages" / "cpp").rglob("*.cpp"))
    build_dir = ctx.root / "build"
    build_dir.mkdir(exist_ok=True)
    if cpp_files:
        toolchain = resolve_gpp_toolchain(ctx)
        for index, source in enumerate(cpp_files):
            print(f"Compiling: {source}")
            output = build_dir / f"check_{index}"
            command = cpp_compile_command(ctx, toolchain, source, output)
            action = f"Compilation for {source}"
            if toolchain.mode == "wsl":
                action = f"Compilation via WSL for {source}"
            run_command(command, action=action)
        print(f"Compiled {len(cpp_files)} C++ file(s) successfully.")
    else:
        print("No C++ files found under languages/cpp")

    typescript_root = ctx.root / "languages" / "typescript"
    if typescript_root.is_dir():
        ts_files = sorted(typescript_root.rglob("*.ts"))
        print("Compiling TypeScript files...")
        compile_typescript(ctx, out_dir=build_dir / "typescript")
        print(f"Compiled {len(ts_files)} TypeScript file(s) successfully.")

    java_root = ctx.root / "languages" / "java"
    if java_root.is_dir():
        java_files = sorted(java_root.rglob("*.java"))
        print("Compiling Java files...")
        java_build_root = build_dir / "java"
        for index, source in enumerate(java_files):
            compile_java_source(ctx, source, java_build_root / f"check_{index}")
        print(f"Compiled {len(java_files)} Java file(s) successfully.")


def build_verification_gaps(ctx: RepoContext) -> None:
    """Compile sources not already compiled by verify-repo contract phases."""

    build_dir = ctx.root / "build" / "verification-gaps"
    build_dir.mkdir(parents=True, exist_ok=True)

    cpp_root = ctx.root / "languages" / "cpp"
    cpp_gaps = [
        source
        for source in sorted(cpp_root.rglob("*.cpp"))
        if not (
            source.name == "main.cpp"
            and source.parent.name == "example"
            or "solutions" in source.parts
        )
    ]
    if cpp_gaps:
        toolchain = resolve_gpp_toolchain(ctx)
        for index, source in enumerate(cpp_gaps):
            output = build_dir / f"cpp_{index}"
            run_command(
                cpp_compile_command(ctx, toolchain, source, output),
                quiet_stdout=True,
                action=f"Verification-gap C++ compilation for {source}",
            )
        print(f"Compiled {len(cpp_gaps)} uncovered C++ starter/auxiliary file(s).")

    java_root = ctx.root / "languages" / "java"
    java_gaps = [
        source
        for source in sorted(java_root.rglob("*.java"))
        if not (
            source.name == "Main.java"
            and source.parent.name == "example"
            or "solutions" in source.parts
        )
    ]
    for index, source in enumerate(java_gaps):
        compile_java_source(ctx, source, build_dir / f"java_{index}")
    if java_gaps:
        print(f"Compiled {len(java_gaps)} uncovered Java starter/auxiliary file(s).")

    print("TypeScript has no verification gaps: its contract phases compile the complete tsconfig.")


def run_module(ctx: RepoContext, module_path: str) -> None:
    normalized = module_path.replace("\\", "/")
    candidate = Path(normalized)
    full_module_path = candidate if candidate.is_absolute() else (ctx.root / candidate)

    if not full_module_path.is_dir():
        raise AutomationError(f"Module folder not found: {normalized}")

    relative_module = full_module_path.resolve().relative_to(ctx.root.resolve())
    if len(relative_module.parts) < 3 or relative_module.parts[0] != "languages":
        raise AutomationError(f"Unsupported module path: {normalized}")

    language = relative_module.parts[1]

    if language == "cpp":
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
                run_command(
                    [str(binary_path)],
                    cwd=full_module_path,
                    action=f"Execution for {normalized}/example/main.cpp",
                )

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
        return

    if language == "typescript":
        example_file = full_module_path / "example" / "main.ts"
        if not example_file.is_file():
            raise AutomationError(f"Missing example file: {normalized}/example/main.ts")

        with tempfile.TemporaryDirectory(prefix="run_module_ts_") as temp_root:
            temp_root_path = Path(temp_root)
            print(f"Compiling example: {normalized}/example/main.ts")
            compile_typescript(ctx, out_dir=temp_root_path)
            print("Running example...")
            compiled_example = typescript_output_path(ctx, temp_root_path, example_file)
            run_command(
                [find_node_command(), str(compiled_example)],
                cwd=full_module_path,
                action=f"Execution for {normalized}/example/main.ts",
            )

        exercises_dir = full_module_path / "exercises"
        exercise_files = sorted(exercises_dir.glob("*.ts")) if exercises_dir.is_dir() else []
        if exercise_files:
            print()
            print(f"Exercises in {normalized}/exercises:")
            for exercise in exercise_files:
                print(f"- {normalized}/exercises/{exercise.name}")
        return

    if language == "java":
        example_file = full_module_path / "example" / "Main.java"
        if not example_file.is_file():
            raise AutomationError(f"Missing example file: {normalized}/example/Main.java")

        with tempfile.TemporaryDirectory(prefix="run_module_java_") as temp_root:
            temp_root_path = Path(temp_root)
            print(f"Compiling example: {normalized}/example/Main.java")
            compile_java_source(ctx, example_file, temp_root_path)
            print("Running example...")
            run_java_class(
                ctx,
                "Main",
                temp_root_path,
                cwd=full_module_path,
                action=f"Execution for {normalized}/example/Main.java",
            )

        exercises_dir = full_module_path / "exercises"
        exercise_files = sorted(exercises_dir.glob("*.java")) if exercises_dir.is_dir() else []
        if exercise_files:
            print()
            print(f"Exercises in {normalized}/exercises:")
            for exercise in exercise_files:
                print(f"- {normalized}/exercises/{exercise.name}")
        return

    if language == "python":
        example_file = full_module_path / "example" / "main.py"
        if not example_file.is_file():
            raise AutomationError(f"Missing example file: {normalized}/example/main.py")
        print("Running example...")
        run_command(
            [find_python_command(), str(example_file)],
            cwd=full_module_path,
            action=f"Execution for {normalized}/example/main.py",
        )
        print_module_exercises(full_module_path, normalized, "*.py")
        return

    if language == "go":
        example_file = full_module_path / "example" / "main.go"
        if not example_file.is_file():
            raise AutomationError(f"Missing example file: {normalized}/example/main.go")
        print("Running example...")
        run_command(
            ["go", "run", *go_target_arguments(example_file)],
            cwd=full_module_path,
            action=f"Execution for {normalized}/example/main.go",
        )
        print_module_exercises(full_module_path, normalized, "*.go")
        return

    if language == "csharp":
        example_dir = full_module_path / "example"
        main_file = example_dir / "main.cs"
        if not main_file.is_file():
            raise AutomationError(f"Missing example file: {normalized}/example/main.cs")
        projects = [
            project
            for project in sorted(example_dir.glob("*.csproj"))
            if 'Compile Include="main.cs"' in project.read_text(encoding="utf-8")
        ]
        if len(projects) != 1:
            raise AutomationError(
                f"Expected one C# project for {normalized}/example/main.cs; found {len(projects)}."
            )
        print(f"Building example: {projects[0].relative_to(ctx.root).as_posix()}")
        run_command(
            ["dotnet", "run", "--project", str(projects[0])],
            cwd=full_module_path,
            action=f"Execution for {normalized}/example/main.cs",
            timeout_seconds=180,
        )
        print_module_exercises(full_module_path, normalized, "*.cs")
        return

    raise AutomationError(f"run-module does not support language: {language}")


def print_module_exercises(module_path: Path, normalized: str, pattern: str) -> None:
    exercises_dir = module_path / "exercises"
    exercise_files = sorted(exercises_dir.glob(pattern)) if exercises_dir.is_dir() else []
    if not exercise_files:
        return
    print()
    print(f"Exercises in {normalized}/exercises:")
    for exercise in exercise_files:
        print(f"- {normalized}/exercises/{exercise.name}")


def doctor_language(ctx: RepoContext, language: str) -> None:
    commands: dict[str, list[list[str]]] = {
        "cpp": [[resolve_gpp_toolchain(ctx).command, "--version"]],
        "csharp": [["dotnet", "--version"]],
        "go": [["go", "version"]],
        "java": [
            [find_java_tool("javac", ctx), "-version"],
            [find_java_tool("java", ctx), "-version"],
        ],
        "python": [[find_python_command(), "--version"]],
        "typescript": [
            [find_node_command(), "--version"],
            [find_npm_command(), "exec", "--", "tsc", "--version"],
        ],
    }
    if language not in commands:
        raise AutomationError(f"Unsupported language: {language}")
    print(f"Checking {language} toolchain...")
    for command in commands[language]:
        run_command(
            command,
            cwd=ctx.root,
            action=f"{language} toolchain check ({Path(command[0]).name})",
            timeout_seconds=60,
        )
    print(f"{language} toolchain is ready.")


def compile_language(ctx: RepoContext, language: str) -> None:
    language_root = ctx.root / "languages" / language
    if language == "python":
        run_command(
            [find_python_command(), "-m", "compileall", "-q", str(language_root)],
            action="Python syntax check",
        )
        return
    if language == "typescript":
        compile_typescript(ctx, no_emit=True)
        return
    if language == "java":
        with tempfile.TemporaryDirectory(prefix="verify-java-") as temp_root:
            for index, source in enumerate(sorted(language_root.rglob("*.java"))):
                compile_java_source(ctx, source, Path(temp_root) / str(index))
        return
    if language == "cpp":
        toolchain = resolve_gpp_toolchain(ctx)
        with tempfile.TemporaryDirectory(prefix="verify-cpp-") as temp_root:
            for index, source in enumerate(sorted(language_root.rglob("*.cpp"))):
                output = Path(temp_root) / str(index)
                run_command(
                    cpp_compile_command(ctx, toolchain, source, output),
                    action=f"C++ compilation for {source}",
                    timeout_seconds=120,
                )
        return
    if language == "go":
        with tempfile.TemporaryDirectory(prefix="verify-go-") as temp_root:
            go_files = sorted(language_root.rglob("*.go"))
            package_dirs = sorted(
                path
                for path in {file_path.parent for file_path in go_files}
                if go_directory_needs_package_build(path)
            )
            package_dir_set = set(package_dirs)
            standalone_files = [
                path
                for path in go_files
                if path.parent not in package_dir_set and go_file_has_main(path)
            ]
            for index, package_dir in enumerate(package_dirs):
                run_command(
                    [
                        "go",
                        "build",
                        "-o",
                        str(Path(temp_root) / f"package-{index}"),
                        *go_target_arguments(package_dir),
                    ],
                    action=f"Go build for {package_dir}",
                )
            for index, source in enumerate(standalone_files):
                run_command(
                    [
                        "go",
                        "build",
                        "-o",
                        str(Path(temp_root) / f"source-{index}"),
                        *go_target_arguments(source),
                    ],
                    action=f"Go build for {source}",
                )
        return
    if language == "csharp":
        for project in sorted(language_root.rglob("*.csproj")):
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
                action=f"C# build for {project}",
                timeout_seconds=180,
            )
        build_csharp_exercises(ctx)
        return
    raise AutomationError(f"Unsupported language: {language}")


def verify_language(ctx: RepoContext, language: str) -> None:
    doctor_language(ctx, language)
    print(f"Compiling {language} track...")
    compile_language(ctx, language)
    print(f"Running {language} example contracts...")
    check_example_output_contracts(ctx, language_filter=language)
    print(f"Running {language} exercise contracts...")
    check_exercise_output_contracts(ctx, language_filter=language)
    print(f"Running {language} checkpoint contracts...")
    check_solution_checkpoint_contracts(ctx, language_filter=language)
    print(f"Language verification passed: {language}.")


def xml_escape(value: str) -> str:
    return (
        value.replace("&", "&amp;").replace('"', "&quot;").replace("<", "&lt;").replace(">", "&gt;")
    )


def csharp_output_dll(project_path: Path) -> Path:
    return project_path.parent / "bin" / "Debug" / "net8.0" / f"{project_path.stem}.dll"


def java_class_name(source_path: Path) -> str:
    return source_path.stem


def compile_java_source(ctx: RepoContext, source_path: Path, output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    run_command(
        [
            find_java_tool("javac", ctx),
            "-d",
            str(output_dir),
            "-sourcepath",
            str(source_path.parent),
            str(source_path),
        ],
        action=f"Java compilation for {source_path}",
        timeout_seconds=120,
    )


def run_java_class(
    ctx: RepoContext,
    class_name: str,
    class_dir: Path,
    *,
    cwd: Path | None = None,
    input_text: str | None = None,
    capture_stdout: bool = False,
    quiet_stdout: bool = False,
    action: str,
) -> subprocess.CompletedProcess[str]:
    return run_command(
        [find_java_tool("java", ctx), "-cp", str(class_dir), class_name],
        cwd=cwd,
        input_text=input_text,
        capture_stdout=capture_stdout,
        quiet_stdout=quiet_stdout,
        action=action,
        timeout_seconds=30,
    )


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


def assert_output_contract(output: str, job: dict[str, Any], label: str) -> None:
    capture = job.get("_capture_stdout")
    if callable(capture):
        capture(output)
    expected_output = job.get("required_stdout_equals", job.get("_required_stdout_equals"))
    if isinstance(expected_output, str):
        normalized_actual = normalize_oracle_output(output, job)
        normalized_expected = normalize_oracle_output(expected_output, job)
        if normalized_actual != normalized_expected:
            raise AutomationError(
                f"{label} did not match the exact output contract.\n"
                f"Expected:\n{expected_output}\nActual:\n{output}"
            )
    if job.get("oracle_solution") and not output.strip():
        raise AutomationError(f"{label} produced no output for an oracle-backed case.")
    for expected in job.get("required_stdout_contains", []):
        if expected not in output:
            raise AutomationError(
                f"{label} did not print expected text: {expected}\nActual output:\n{output}"
            )
    for pattern in job.get("required_stdout_patterns", []):
        if not re.search(pattern, output, re.MULTILINE):
            raise AutomationError(
                f"{label} did not match expected pattern: {pattern}\nActual output:\n{output}"
            )
    for forbidden in job.get("forbidden_stdout_contains", []):
        if forbidden in output:
            raise AutomationError(
                f"{label} printed forbidden text: {forbidden}\nActual output:\n{output}"
            )


def normalize_oracle_output(output: str, job: dict[str, Any]) -> str:
    normalized = output.replace("\r\n", "\n").strip()
    normalizers = job.get("oracle_normalizers", [])
    if "timings" in normalizers:
        timing_words = re.compile(
            r"tim(?:e|ing)|ticks?|elapsed|duration|milliseconds?|\b(?:ms|us|\u00b5s|ns)\b",
            re.I,
        )
        timing_value_with_unit = re.compile(
            r"\b\d+(?:\.\d+)?\s*(?:ms|us|\u00b5s|ns|s)\b", re.IGNORECASE
        )
        normalized_lines: list[str] = []
        for line in normalized.splitlines():
            if timing_words.search(line):
                normalized_lines.append(re.sub(r"\b\d+(?:\.\d+)?\b", "<timing>", line))
            else:
                normalized_lines.append(timing_value_with_unit.sub("<timing>", line))
        normalized = "\n".join(normalized_lines)
    if "unordered_lines" in normalizers:
        normalized = "\n".join(sorted(normalized.splitlines()))
    return normalized


def smoke_runtime_job(
    ctx: RepoContext,
    job: dict[str, Any],
    *,
    command_builder: Any,
    label: str,
    environment: dict[str, str] | None = None,
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

        capture_stdout = bool(
            job.get("required_stdout_contains")
            or job.get("required_stdout_patterns")
            or job.get("oracle_solution")
            or job.get("_capture_stdout")
            or job.get("required_stdout_equals")
            or job.get("_required_stdout_equals")
        )

        command = list(command_builder(job, working_dir))
        command.extend(str(argument) for argument in job.get("arguments", []))
        completed = run_command(
            command,
            cwd=working_dir,
            input_text=input_text,
            environment=environment,
            quiet_stdout=not capture_stdout,
            capture_stdout=capture_stdout,
            action=label,
            timeout_seconds=timeout_seconds,
        )

        if capture_stdout:
            assert_output_contract(completed.stdout or "", job, label)

        for output_name in job.get("required_outputs", []):
            if not (working_dir / output_name).exists():
                raise AutomationError(f"{label} did not create {output_name}")

        for output_spec in job.get("required_output_contains", []):
            output_path = working_dir / output_spec["path"]
            if not output_path.exists():
                raise AutomationError(f"{label} did not create {output_spec['path']}")

            output_text = output_path.read_text(encoding="utf-8")
            for expected in output_spec.get("contains", []):
                if expected not in output_text:
                    raise AutomationError(
                        f"{label} output {output_spec['path']} did not contain expected text: "
                        f"{expected}\nActual output:\n{output_text}"
                    )
    finally:
        remove_paths(working_dir, cleanup_paths)


def smoke_languages(ctx: RepoContext) -> None:
    python_cmd = find_python_command()

    python_smoke = ctx.manifest.smoke["python"]
    print("[1/10] Python syntax check...")
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

    print("[2/10] Python runtime smoke...")
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
    print("[3/10] Go compile check...")
    with tempfile.TemporaryDirectory(prefix="go-smoke-") as temp_root:
        temp_root_path = Path(temp_root)
        go_root = repo_path(ctx, go_smoke["build_glob_root"])
        package_dirs = sorted(
            path
            for path in {file_path.parent for file_path in go_root.rglob("*.go")}
            if go_directory_needs_package_build(path)
        )
        package_dir_set = set(package_dirs)
        standalone_files = sorted(
            path
            for path in go_root.rglob("*.go")
            if path.parent not in package_dir_set and go_file_has_main(path)
        )

        for index, package_dir in enumerate(package_dirs):
            run_command(
                [
                    "go",
                    "build",
                    "-o",
                    str(temp_root_path / f"go_build_pkg_{index}"),
                    *go_target_arguments(package_dir),
                ],
                action=f"Go build for {package_dir}",
            )

        for index, source in enumerate(standalone_files):
            run_command(
                [
                    "go",
                    "build",
                    "-o",
                    str(temp_root_path / f"go_build_file_{index}"),
                    *go_target_arguments(source),
                ],
                action=f"Go build for {source}",
            )

    print("[4/10] Go runtime smoke...")
    for program in go_smoke["example_paths"]:
        program_path = repo_path(ctx, program)
        run_command(
            ["go", "run", *go_target_arguments(program_path)],
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
                *go_target_arguments(resolve_job_path(ctx, working_dir, current_job["program"])),
            ],
            label=f"Go runtime smoke for {job.get('program', job.get('working_dir', 'job'))}",
        )

    typescript_smoke = ctx.manifest.smoke["typescript"]
    print("[5/10] TypeScript compile check...")
    node_cmd = find_node_command()
    with tempfile.TemporaryDirectory(prefix="ts-smoke-") as temp_root:
        temp_root_path = Path(temp_root)
        compile_typescript(ctx, out_dir=temp_root_path)

        print("[6/10] TypeScript runtime smoke...")
        for program in typescript_smoke["example_paths"]:
            source_path = repo_path(ctx, program)
            run_command(
                [node_cmd, str(typescript_output_path(ctx, temp_root_path, source_path))],
                quiet_stdout=True,
                action=f"TypeScript runtime smoke for {program}",
            )
        for job in typescript_smoke["stdin_runs"]:
            smoke_runtime_job(
                ctx,
                job,
                command_builder=lambda current_job, working_dir: [
                    node_cmd,
                    str(
                        typescript_output_path(
                            ctx,
                            temp_root_path,
                            resolve_job_path(ctx, working_dir, current_job["program"]),
                        )
                    ),
                ],
                label=(
                    f"TypeScript runtime smoke for "
                    f"{job.get('program', job.get('working_dir', 'job'))}"
                ),
            )

    csharp_smoke = ctx.manifest.smoke["csharp"]
    print("[7/10] C# build check...")
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

    print("[8/10] C# runtime smoke...")
    for project in csharp_smoke["example_projects"]:
        print(f"  Running {project}")
        project_path = repo_path(ctx, project)
        run_command(
            ["dotnet", str(csharp_output_dll(project_path))],
            environment={"DOTNET_SYSTEM_GLOBALIZATION_INVARIANT": "1"},
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
            environment={"DOTNET_SYSTEM_GLOBALIZATION_INVARIANT": "1"},
            timeout_seconds=30,
        )

    java_smoke = ctx.manifest.smoke.get("java")
    if java_smoke:
        print("[9/10] Java compile check...")
        with tempfile.TemporaryDirectory(prefix="java-smoke-") as temp_root:
            temp_root_path = Path(temp_root)
            java_root = repo_path(ctx, java_smoke["build_glob_root"])
            for index, source in enumerate(sorted(java_root.rglob("*.java"))):
                compile_java_source(ctx, source, temp_root_path / f"java_build_{index}")

            print("[10/10] Java runtime smoke...")
            for program in java_smoke["example_paths"]:
                source_path = repo_path(ctx, program)
                class_dir = temp_root_path / f"java_run_{len(program)}_{source_path.stem}"
                compile_java_source(ctx, source_path, class_dir)
                run_java_class(
                    ctx,
                    java_class_name(source_path),
                    class_dir,
                    cwd=source_path.parent.parent,
                    quiet_stdout=True,
                    action=f"Java runtime smoke for {program}",
                )
            for job in java_smoke.get("stdin_runs", []):
                source_path = repo_path(ctx, job["program"])
                class_dir = (
                    temp_root_path / f"java_stdin_{len(str(source_path))}_{source_path.stem}"
                )
                compile_java_source(ctx, source_path, class_dir)
                smoke_runtime_job(
                    ctx,
                    job,
                    command_builder=lambda current_job, working_dir, compiled_dir=class_dir: [
                        find_java_tool("java", ctx),
                        "-cp",
                        str(compiled_dir),
                        java_class_name(resolve_job_path(ctx, working_dir, current_job["program"])),
                    ],
                    label=f"Java runtime smoke for {job['program']}",
                )

    print("Multi-language smoke checks passed.")


def load_output_contracts(
    ctx: RepoContext, contracts_file: str, description: str
) -> dict[str, list[dict[str, Any]]]:
    contracts_path = ctx.scripts_dir / contracts_file
    if not contracts_path.is_file():
        raise AutomationError(f"Missing {description} output contracts file: {contracts_path}")

    payload = json.loads(contracts_path.read_text(encoding="utf-8"))
    languages = payload.get("languages")
    if not isinstance(languages, dict):
        raise AutomationError(
            f"{contracts_path}: expected top-level object with 'languages' mapping "
            f"for {description} contracts."
        )
    result: dict[str, list[dict[str, Any]]] = {}
    for language, jobs in languages.items():
        if not isinstance(jobs, list):
            raise AutomationError(
                f"{contracts_path}: language '{language}' must map to a list of jobs."
            )
        result[language] = [dict(job) for job in jobs]
    return result


def load_example_output_contracts(ctx: RepoContext) -> dict[str, list[dict[str, Any]]]:
    return load_output_contracts(ctx, "example_output_contracts.json", "example")


def load_exercise_output_contracts(ctx: RepoContext) -> dict[str, list[dict[str, Any]]]:
    contracts: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for exercise in load_learning_exercises(ctx):
        language = exercise.get("language")
        solution = exercise.get("solution")
        cases = exercise.get("cases")
        if not isinstance(language, str) or not isinstance(solution, str):
            raise AutomationError(
                "scripts/learning_exercises.json: exercise identity and solution are required."
            )
        if not isinstance(cases, list):
            raise AutomationError(
                "scripts/learning_exercises.json: every exercise must define cases."
            )
        for case in cases:
            if not isinstance(case, dict):
                raise AutomationError(
                    "scripts/learning_exercises.json: every exercise case must be an object."
                )
            job = dict(case)
            job["program"] = solution
            contracts[language].append(job)
    return dict(contracts)


def load_learning_exercises(ctx: RepoContext) -> list[dict[str, Any]]:
    exercises_path = ctx.scripts_dir / "learning_exercises.json"
    if not exercises_path.is_file():
        raise AutomationError(f"Missing learning exercises file: {exercises_path}")

    payload = json.loads(exercises_path.read_text(encoding="utf-8"))
    exercises = payload.get("exercises")
    if not isinstance(exercises, list):
        raise AutomationError(
            f"{exercises_path}: expected top-level object with an 'exercises' list."
        )
    case_sets = payload.get("case_sets", {})
    if not isinstance(case_sets, dict):
        raise AutomationError(f"{exercises_path}: 'case_sets' must be an object.")

    result: list[dict[str, Any]] = []
    for exercise in exercises:
        if not isinstance(exercise, dict):
            raise AutomationError(f"{exercises_path}: each exercise must be an object.")
        current = dict(exercise)
        case_set_name = current.get("case_set")
        if case_set_name is not None:
            cases = case_sets.get(case_set_name)
            if not isinstance(cases, list):
                raise AutomationError(
                    f"{exercises_path}: unknown or invalid case set '{case_set_name}'."
                )
            current["cases"] = cases
        result.append(current)
    return result


def check_learning_exercise(
    ctx: RepoContext,
    *,
    language: str,
    level: str,
    module: str,
    exercise_id: str,
    submission: str | None,
    use_solution: bool,
) -> None:
    matches = [
        exercise
        for exercise in load_learning_exercises(ctx)
        if exercise.get("language") == language
        and exercise.get("level") == level
        and exercise.get("module") == module
        and exercise.get("exercise") == exercise_id
    ]
    exercise_label = f"{language}/{level}/{module}/{exercise_id}"
    if not matches:
        raise AutomationError(f"No learner exercise is configured for {exercise_label}.")
    if len(matches) > 1:
        raise AutomationError(f"Duplicate learner exercise configuration for {exercise_label}.")

    exercise = matches[0]
    configured_path = exercise.get("solution" if use_solution else "starter")
    raw_submission = submission or configured_path
    if not isinstance(raw_submission, str) or not raw_submission:
        raise AutomationError(f"Missing source path configuration for {exercise_label}.")

    source_path = repo_path(ctx, raw_submission).resolve()
    try:
        source_path.relative_to(ctx.root.resolve())
    except ValueError as error:
        raise AutomationError(
            "Exercise submissions must be located inside the repository."
        ) from error
    if not source_path.is_file():
        raise AutomationError(f"Exercise submission does not exist: {source_path}")
    if language == "typescript":
        typescript_root = (ctx.root / "languages" / "typescript").resolve()
        try:
            source_path.relative_to(typescript_root)
        except ValueError as error:
            raise AutomationError(
                "TypeScript submissions must be located under languages/typescript "
                "so the track tsconfig can compile them."
            ) from error

    cases = exercise.get("cases")
    if not isinstance(cases, list) or not cases:
        raise AutomationError(f"No check cases are configured for {exercise_label}.")

    oracle_outputs: dict[int, str] = {}
    if not use_solution and any(case.get("oracle_solution") for case in cases):
        solution = exercise.get("solution")
        if not isinstance(solution, str):
            raise AutomationError(f"Missing reference solution for {exercise_label}.")
        oracle_jobs: list[dict[str, Any]] = []
        for index, case in enumerate(cases):
            if not case.get("oracle_solution"):
                continue
            oracle_job = dict(case)
            oracle_job["program"] = solution
            oracle_job["_capture_stdout"] = lambda output, case_index=index: (
                oracle_outputs.__setitem__(case_index, output)
            )
            oracle_jobs.append(oracle_job)
        check_exercise_output_contracts(
            ctx,
            language_filter=language,
            contracts_override={language: oracle_jobs},
            success_message=None,
        )

    program = source_path.relative_to(ctx.root.resolve()).as_posix()
    jobs: list[dict[str, Any]] = []
    for index, case in enumerate(cases):
        if not isinstance(case, dict):
            raise AutomationError(f"Invalid case {index + 1} for {exercise_label}.")
        job = dict(case)
        if job.get("oracle_solution") and not use_solution:
            forbidden = list(job.get("forbidden_stdout_contains", []))
            forbidden.append("TODO: implement this exercise")
            job["forbidden_stdout_contains"] = forbidden
            job["_required_stdout_equals"] = oracle_outputs[index]
        job["program"] = program
        jobs.append(job)

    source_kind = "reference solution" if use_solution else "submission"
    print(f"Checking {source_kind} for {exercise_label} ({len(jobs)} cases)...")
    check_exercise_output_contracts(
        ctx,
        language_filter=language,
        contracts_override={language: jobs},
        success_message=f"Exercise check passed for {exercise_label} ({len(jobs)} cases).",
    )


def check_learning_checkpoint(
    ctx: RepoContext,
    *,
    language: str,
    kind: str,
    level: str,
    submission: str | None,
    use_solution: bool,
) -> None:
    try:
        checkpoints = load_learning_checkpoints(ctx.scripts_dir)
    except CurriculumError as error:
        raise AutomationError(str(error)) from error
    matches = [
        checkpoint
        for checkpoint in checkpoints
        if checkpoint.get("language") == language
        and checkpoint.get("kind") == kind
        and checkpoint.get("level") == level
    ]
    label = f"{language}/{kind}/{level}"
    if not matches:
        raise AutomationError(f"No learner checkpoint is configured for {label}.")
    if len(matches) > 1:
        raise AutomationError(f"Duplicate learner checkpoint configuration for {label}.")

    checkpoint = matches[0]
    configured_root = checkpoint.get("solution" if use_solution else "starter")
    raw_root = submission or configured_root
    if not isinstance(raw_root, str) or not raw_root:
        raise AutomationError(f"Missing checkpoint path configuration for {label}.")
    source_root = repo_path(ctx, raw_root).resolve()
    try:
        source_root.relative_to(ctx.root.resolve())
    except ValueError as error:
        raise AutomationError(
            "Checkpoint submissions must be located inside the repository."
        ) from error
    if not source_root.is_dir():
        raise AutomationError(f"Checkpoint submission directory does not exist: {source_root}")

    entrypoint = checkpoint.get("entrypoint")
    if not isinstance(entrypoint, str) or not (source_root / entrypoint).is_file():
        raise AutomationError(
            f"Checkpoint entrypoint does not exist: {source_root / str(entrypoint)}"
        )
    cases = checkpoint.get("cases")
    if not isinstance(cases, list) or not cases:
        raise AutomationError(f"No check cases are configured for {label}.")

    relative_root = source_root.relative_to(ctx.root.resolve()).as_posix()
    jobs: list[dict[str, Any]] = []
    for index, case in enumerate(cases, start=1):
        if not isinstance(case, dict):
            raise AutomationError(f"Invalid case {index} for {label}.")
        job = dict(case)
        job["working_dir"] = relative_root
        if job.get("oracle_solution") and not use_solution:
            forbidden = list(job.get("forbidden_stdout_contains", []))
            forbidden.append("TODO: implement this checkpoint")
            job["forbidden_stdout_contains"] = forbidden
        job["program"] = f"{relative_root}/{entrypoint}"
        jobs.append(job)

    source_kind = "reference solution" if use_solution else "submission"
    print(f"Checking {source_kind} for {label} ({len(jobs)} cases)...")

    def run_checkpoint_jobs(
        current_root: Path,
        current_jobs: list[dict[str, Any]],
        phase: str,
    ) -> None:
        if language != "csharp":
            check_exercise_output_contracts(
                ctx,
                language_filter=language,
                contracts_override={language: current_jobs},
                success_message=None,
            )
            return

        project_file = checkpoint.get("project_file")
        if not isinstance(project_file, str) or not (current_root / project_file).is_file():
            raise AutomationError(f"C# checkpoint project does not exist in {current_root}.")
        project = current_root / project_file
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
            action=f"C# checkpoint {phase} build for {label}",
            timeout_seconds=180,
        )
        for job in current_jobs:
            smoke_runtime_job(
                ctx,
                job,
                command_builder=lambda _job, _working_dir: [
                    "dotnet",
                    str(csharp_output_dll(project)),
                ],
                label=(
                    f"C# checkpoint {phase} contract for {label}{output_contract_case_suffix(job)}"
                ),
                environment={"DOTNET_SYSTEM_GLOBALIZATION_INVARIANT": "1"},
            )

    if not use_solution and any(case.get("oracle_solution") for case in cases):
        solution_root_value = checkpoint.get("solution")
        if not isinstance(solution_root_value, str):
            raise AutomationError(f"Missing checkpoint reference solution for {label}.")
        solution_root = repo_path(ctx, solution_root_value).resolve()
        solution_relative = solution_root.relative_to(ctx.root.resolve()).as_posix()
        oracle_outputs: dict[int, str] = {}
        oracle_jobs: list[dict[str, Any]] = []
        for index, case in enumerate(cases):
            if not case.get("oracle_solution"):
                continue
            oracle_job = dict(case)
            oracle_job["working_dir"] = solution_relative
            oracle_job["program"] = f"{solution_relative}/{entrypoint}"
            oracle_job["_capture_stdout"] = lambda output, case_index=index: (
                oracle_outputs.__setitem__(case_index, output)
            )
            oracle_jobs.append(oracle_job)
        run_checkpoint_jobs(solution_root, oracle_jobs, "reference")
        for index, job in enumerate(jobs):
            if job.get("oracle_solution"):
                job["_required_stdout_equals"] = oracle_outputs[index]

    run_checkpoint_jobs(source_root, jobs, source_kind)
    print(f"Checkpoint check passed for {label} ({len(jobs)} cases).")


def check_solution_checkpoint_contracts(
    ctx: RepoContext, *, language_filter: str | None = None
) -> None:
    if language_filter is not None and language_filter not in ctx.manifest.languages:
        supported = ", ".join(sorted(ctx.manifest.languages))
        raise AutomationError(
            "Unsupported checkpoint language filter: "
            f"{language_filter}. Expected one of: {supported}."
        )

    try:
        checkpoints = load_learning_checkpoints(ctx.scripts_dir)
    except CurriculumError as error:
        raise AutomationError(str(error)) from error

    selected = [
        checkpoint
        for checkpoint in checkpoints
        if language_filter is None or checkpoint.get("language") == language_filter
    ]
    if not selected:
        suffix = f" for language '{language_filter}'" if language_filter else ""
        raise AutomationError(f"No checkpoint contracts configured{suffix}.")

    for checkpoint in sorted(
        selected,
        key=lambda item: (
            str(item.get("language")),
            str(item.get("kind")),
            str(item.get("level")),
        ),
    ):
        check_learning_checkpoint(
            ctx,
            language=str(checkpoint["language"]),
            kind=str(checkpoint["kind"]),
            level=str(checkpoint["level"]),
            submission=None,
            use_solution=True,
        )

    suffix = f" in language '{language_filter}'" if language_filter else ""
    print(f"Checkpoint contracts passed for {len(selected)} solutions{suffix}.")


def is_vacuous_stdout_pattern(pattern: str) -> bool:
    normalized = pattern.strip()
    if normalized in {r"\S", r".+", r"[\s\S]+", r"(?s).+"}:
        return True

    try:
        compiled = re.compile(pattern, re.MULTILINE)
    except re.error:
        return False
    return all(compiled.search(sample) for sample in ["", "x", "not expected output\n"])


def output_contract_case_suffix(job: dict[str, Any]) -> str:
    case_name = job.get("name")
    return f" case '{case_name}'" if isinstance(case_name, str) and case_name else ""


def run_csharp_source_output_contracts(
    ctx: RepoContext,
    jobs: list[dict[str, Any]],
    *,
    label_prefix: str,
) -> int:
    executed_jobs = 0
    if not jobs:
        return executed_jobs

    with tempfile.TemporaryDirectory(prefix="csharp-source-output-contracts-") as temp_root:
        temp_root_path = Path(temp_root)
        compiled_targets: dict[str, Path] = {}
        for job in jobs:
            source_path = repo_path(ctx, job["program"])
            if not source_path.is_file():
                raise AutomationError(f"Missing C# contract source: {source_path}")
            case_suffix = output_contract_case_suffix(job)

            run_target = compiled_targets.get(job["program"])
            if run_target is None:
                project_dir = temp_root_path / f"exercise-{len(compiled_targets)}"
                project_dir.mkdir(parents=True, exist_ok=True)
                project_path = project_dir / "exercise-check.csproj"
                escaped_source = xml_escape(str(source_path.resolve()))
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
                            f'    <Compile Include="{escaped_source}" Link="Program.cs" />',
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
                    action=f"C# build for {label_prefix} contract {job['program']}",
                    timeout_seconds=180,
                )
                run_target = project_dir / "bin" / "Debug" / "net8.0" / "exercise-check.dll"
                compiled_targets[job["program"]] = run_target
            working_dir = repo_path(ctx, job["working_dir"]) if "working_dir" in job else ctx.root
            setup_files = job.get("setup_files", [])
            cleanup_paths = list(job.get("cleanup_paths", []))
            capture_stdout = bool(
                job.get("required_stdout_contains")
                or job.get("required_stdout_patterns")
                or job.get("oracle_solution")
                or job.get("_capture_stdout")
                or job.get("required_stdout_equals")
                or job.get("_required_stdout_equals")
            )

            try:
                for file_spec in setup_files:
                    target = working_dir / file_spec["path"]
                    target.write_text("\n".join(file_spec["lines"]) + "\n", encoding="utf-8")

                input_text = None
                if "input_lines" in job:
                    input_text = "\n".join(job["input_lines"]) + "\n"
                elif "input_file" in job:
                    input_text = str((working_dir / job["input_file"]).resolve()) + "\n"

                label = f"C# {label_prefix} output contract for {job['program']}{case_suffix}"
                completed = run_command(
                    ["dotnet", str(run_target)],
                    cwd=working_dir,
                    input_text=input_text,
                    environment={"DOTNET_SYSTEM_GLOBALIZATION_INVARIANT": "1"},
                    capture_stdout=capture_stdout,
                    quiet_stdout=not capture_stdout,
                    action=(
                        f"C# execution for {label_prefix} output contract "
                        f"{job['program']}{case_suffix}"
                    ),
                    timeout_seconds=30,
                )
                if capture_stdout:
                    assert_output_contract(completed.stdout or "", job, label)

                for output_name in job.get("required_outputs", []):
                    if not (working_dir / output_name).exists():
                        raise AutomationError(f"{label} did not create {output_name}")

                for output_spec in job.get("required_output_contains", []):
                    output_path = working_dir / output_spec["path"]
                    if not output_path.exists():
                        raise AutomationError(f"{label} did not create {output_spec['path']}")

                    output_text = output_path.read_text(encoding="utf-8")
                    for expected in output_spec.get("contains", []):
                        if expected not in output_text:
                            raise AutomationError(
                                f"{label} output {output_spec['path']} did not contain "
                                f"expected text: {expected}\nActual output:\n{output_text}"
                            )
                executed_jobs += 1
            finally:
                remove_paths(working_dir, cleanup_paths)

    return executed_jobs


def run_java_source_output_contracts(
    ctx: RepoContext,
    jobs: list[dict[str, Any]],
    *,
    label_prefix: str,
) -> int:
    executed_jobs = 0
    if not jobs:
        return executed_jobs

    with tempfile.TemporaryDirectory(prefix="java-source-output-contracts-") as temp_root:
        temp_root_path = Path(temp_root)
        compiled_targets: dict[str, Path] = {}
        for job in jobs:
            source_path = repo_path(ctx, job["program"])
            if not source_path.is_file():
                raise AutomationError(f"Missing Java contract source: {source_path}")
            case_suffix = output_contract_case_suffix(job)

            class_dir = compiled_targets.get(job["program"])
            if class_dir is None:
                class_dir = temp_root_path / f"java-contract-{len(compiled_targets)}"
                compile_java_source(ctx, source_path, class_dir)
                compiled_targets[job["program"]] = class_dir
            smoke_runtime_job(
                ctx,
                job,
                command_builder=lambda current_job, working_dir, compiled_dir=class_dir: [
                    find_java_tool("java", ctx),
                    "-cp",
                    str(compiled_dir),
                    java_class_name(resolve_job_path(ctx, working_dir, current_job["program"])),
                ],
                label=(f"Java {label_prefix} output contract for {job['program']}{case_suffix}"),
            )
            executed_jobs += 1

    return executed_jobs


def run_go_source_output_contracts(
    ctx: RepoContext,
    jobs: list[dict[str, Any]],
    *,
    label_prefix: str,
) -> int:
    if not jobs:
        return 0

    executed_jobs = 0
    with tempfile.TemporaryDirectory(prefix="go-source-output-contracts-") as temp_root:
        temp_root_path = Path(temp_root)
        compiled_targets: dict[str, Path] = {}
        for job in jobs:
            source_path = repo_path(ctx, job["program"])
            if not source_path.exists():
                raise AutomationError(f"Missing Go contract source: {source_path}")

            binary = compiled_targets.get(job["program"])
            if binary is None:
                output = temp_root_path / f"go-contract-{len(compiled_targets)}"
                run_command(
                    ["go", "build", "-o", str(output), *go_target_arguments(source_path)],
                    action=f"Go compilation for output contract {job['program']}",
                    timeout_seconds=120,
                )
                binary = compiled_binary_path(ctx, output)
                compiled_targets[job["program"]] = binary

            case_suffix = output_contract_case_suffix(job)
            smoke_runtime_job(
                ctx,
                job,
                command_builder=lambda _job, _working_dir, target=binary: [str(target)],
                label=f"Go {label_prefix} output contract for {job['program']}{case_suffix}",
            )
            executed_jobs += 1

    return executed_jobs


def check_example_output_contracts(ctx: RepoContext, *, language_filter: str | None = None) -> None:
    contracts = load_example_output_contracts(ctx)
    if language_filter is not None:
        contracts = {language_filter: contracts.get(language_filter, [])}
    if not contracts:
        raise AutomationError("No example output contracts configured.")

    executed_jobs = 0
    python_cmd = find_python_command()
    node_cmd = find_node_command()

    for job in contracts.get("python", []):
        smoke_runtime_job(
            ctx,
            job,
            command_builder=lambda current_job, working_dir: [
                python_cmd,
                str(resolve_job_path(ctx, working_dir, current_job["program"])),
            ],
            label=f"Python example output contract for {job['program']}",
        )
        executed_jobs += 1

    executed_jobs += run_go_source_output_contracts(
        ctx,
        contracts.get("go", []),
        label_prefix="example",
    )

    if contracts.get("typescript"):
        with tempfile.TemporaryDirectory(prefix="ts-output-contracts-") as temp_root:
            temp_root_path = Path(temp_root)
            compile_typescript(ctx, out_dir=temp_root_path)
            for job in contracts.get("typescript", []):
                smoke_runtime_job(
                    ctx,
                    job,
                    command_builder=lambda current_job, working_dir: [
                        node_cmd,
                        str(
                            typescript_output_path(
                                ctx,
                                temp_root_path,
                                resolve_job_path(ctx, working_dir, current_job["program"]),
                            )
                        ),
                    ],
                    label=f"TypeScript example output contract for {job['program']}",
                )
                executed_jobs += 1

    csharp_contracts = contracts.get("csharp", [])
    if csharp_contracts:
        built_projects = sorted({job["project"] for job in csharp_contracts})
        for project in built_projects:
            project_path = repo_path(ctx, project)
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
                action=f"C# build for output contract {project}",
                timeout_seconds=180,
            )
        for job in csharp_contracts:
            smoke_runtime_job(
                ctx,
                job,
                command_builder=lambda current_job, working_dir: [
                    "dotnet",
                    str(
                        csharp_output_dll(
                            resolve_job_path(ctx, working_dir, current_job["project"])
                        )
                    ),
                ],
                label=f"C# example output contract for {job['project']}",
                environment={"DOTNET_SYSTEM_GLOBALIZATION_INVARIANT": "1"},
                timeout_seconds=30,
            )
            executed_jobs += 1

    executed_jobs += run_java_source_output_contracts(
        ctx,
        contracts.get("java", []),
        label_prefix="example",
    )

    cpp_contracts = contracts.get("cpp", [])
    if cpp_contracts:
        toolchain = resolve_gpp_toolchain(ctx)
        with tempfile.TemporaryDirectory(prefix="cpp-output-contracts-") as temp_root:
            temp_root_path = Path(temp_root)
            for index, job in enumerate(cpp_contracts):
                source_path = repo_path(ctx, job["program"])
                if not source_path.is_file():
                    raise AutomationError(f"Missing C++ contract source: {source_path}")

                output_path = temp_root_path / f"cpp_contract_{index}"
                compile_command = cpp_compile_command(ctx, toolchain, source_path, output_path)
                compile_action = f"C++ compilation for output contract {job['program']}"
                if toolchain.mode == "wsl":
                    compile_action = f"C++ WSL compilation for output contract {job['program']}"
                run_command(compile_command, action=compile_action, timeout_seconds=120)

                input_text = None
                if "input_lines" in job:
                    input_text = "\n".join(job["input_lines"]) + "\n"

                if toolchain.mode == "wsl":
                    binary_command = [
                        "wsl",
                        "bash",
                        "-lc",
                        shlex.quote(to_wsl_path(output_path)),
                    ]
                else:
                    binary_command = [str(compiled_binary_path(ctx, output_path))]
                binary_command.extend(str(argument) for argument in job.get("arguments", []))

                working_dir = (
                    repo_path(ctx, job["working_dir"]) if "working_dir" in job else ctx.root
                )
                cleanup_paths = list(job.get("cleanup_paths", []))
                label = f"C++ example output contract for {job['program']}"
                try:
                    for file_spec in job.get("setup_files", []):
                        target = working_dir / file_spec["path"]
                        target.write_text("\n".join(file_spec["lines"]) + "\n", encoding="utf-8")
                    completed = run_command(
                        binary_command,
                        cwd=working_dir,
                        input_text=input_text,
                        capture_stdout=True,
                        action=f"C++ execution for output contract {job['program']}",
                        timeout_seconds=30,
                    )
                    assert_output_contract(completed.stdout or "", job, label)
                    for output_name in job.get("required_outputs", []):
                        if not (working_dir / output_name).exists():
                            raise AutomationError(f"{label} did not create {output_name}")
                    for output_spec in job.get("required_output_contains", []):
                        generated = working_dir / output_spec["path"]
                        if not generated.exists():
                            raise AutomationError(f"{label} did not create {output_spec['path']}")
                        generated_text = generated.read_text(encoding="utf-8")
                        for expected in output_spec.get("contains", []):
                            if expected not in generated_text:
                                raise AutomationError(
                                    f"{label} output {output_spec['path']} did not contain "
                                    f"expected text: {expected}\nActual output:\n{generated_text}"
                                )
                    executed_jobs += 1
                finally:
                    remove_paths(working_dir, cleanup_paths)

    if executed_jobs == 0:
        raise AutomationError("No example output contract jobs were executed.")

    suffix = "" if language_filter is None else f" in language '{language_filter}'"
    print(f"Example output contracts passed for {executed_jobs} jobs{suffix}.")


def check_exercise_output_contracts(
    ctx: RepoContext,
    language_filter: str | None = None,
    *,
    contracts_override: dict[str, list[dict[str, Any]]] | None = None,
    success_message: str | None = None,
) -> None:
    contracts = contracts_override or load_exercise_output_contracts(ctx)
    if not contracts:
        raise AutomationError("No exercise output contracts configured.")

    executed_jobs = 0
    python_cmd = find_python_command()
    node_cmd = find_node_command()
    allowed_languages = {"cpp", "csharp", "go", "java", "python", "typescript"}
    if language_filter is not None and language_filter not in allowed_languages:
        raise AutomationError(
            "Unsupported exercise output contracts language filter: "
            f"{language_filter}. Allowed: {', '.join(sorted(allowed_languages))}."
        )

    for job in contracts.get("python", []) if language_filter in (None, "python") else []:
        case_suffix = output_contract_case_suffix(job)
        smoke_runtime_job(
            ctx,
            job,
            command_builder=lambda current_job, working_dir: [
                python_cmd,
                str(resolve_job_path(ctx, working_dir, current_job["program"])),
            ],
            label=f"Python exercise output contract for {job['program']}{case_suffix}",
        )
        executed_jobs += 1

    if language_filter in (None, "go"):
        executed_jobs += run_go_source_output_contracts(
            ctx,
            contracts.get("go", []),
            label_prefix="exercise",
        )

    if language_filter in (None, "typescript") and contracts.get("typescript"):
        with tempfile.TemporaryDirectory(prefix="ts-exercise-output-contracts-") as temp_root:
            temp_root_path = Path(temp_root)
            compile_typescript(ctx, out_dir=temp_root_path)
            for job in contracts.get("typescript", []):
                case_suffix = output_contract_case_suffix(job)
                smoke_runtime_job(
                    ctx,
                    job,
                    command_builder=lambda current_job, working_dir: [
                        node_cmd,
                        str(
                            typescript_output_path(
                                ctx,
                                temp_root_path,
                                resolve_job_path(ctx, working_dir, current_job["program"]),
                            )
                        ),
                    ],
                    label=(
                        f"TypeScript exercise output contract for {job['program']}{case_suffix}"
                    ),
                )
                executed_jobs += 1

    if language_filter in (None, "csharp"):
        executed_jobs += run_csharp_source_output_contracts(
            ctx,
            contracts.get("csharp", []),
            label_prefix="exercise",
        )

    if language_filter in (None, "java"):
        executed_jobs += run_java_source_output_contracts(
            ctx,
            contracts.get("java", []),
            label_prefix="exercise",
        )

    cpp_contracts = contracts.get("cpp", []) if language_filter in (None, "cpp") else []
    if cpp_contracts:
        toolchain = resolve_gpp_toolchain(ctx)
        with tempfile.TemporaryDirectory(prefix="cpp-exercise-output-contracts-") as temp_root:
            temp_root_path = Path(temp_root)
            compiled_targets: dict[str, Path] = {}
            for job in cpp_contracts:
                source_path = repo_path(ctx, job["program"])
                if not source_path.is_file():
                    raise AutomationError(f"Missing C++ contract source: {source_path}")
                case_suffix = output_contract_case_suffix(job)

                binary_output = compiled_targets.get(job["program"])
                if binary_output is None:
                    binary_output = temp_root_path / f"cpp-contract-{len(compiled_targets)}"
                    compile_command = cpp_compile_command(
                        ctx, toolchain, source_path, binary_output
                    )
                    compile_action = f"C++ compilation for contract {job['program']}"
                    if toolchain.mode == "wsl":
                        compile_action = f"C++ WSL compilation for contract {job['program']}"
                    run_command(compile_command, action=compile_action, timeout_seconds=120)
                    compiled_targets[job["program"]] = binary_output

                working_dir = (
                    repo_path(ctx, job["working_dir"]) if "working_dir" in job else ctx.root
                )
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

                    if toolchain.mode == "wsl":
                        binary_command = [
                            "wsl",
                            "bash",
                            "-lc",
                            shlex.quote(to_wsl_path(binary_output)),
                        ]
                    else:
                        binary_command = [str(compiled_binary_path(ctx, binary_output))]
                    binary_command.extend(str(argument) for argument in job.get("arguments", []))

                    label = f"C++ exercise output contract for {job['program']}{case_suffix}"
                    completed = run_command(
                        binary_command,
                        cwd=working_dir,
                        input_text=input_text,
                        capture_stdout=True,
                        action=(
                            f"C++ execution for exercise output contract "
                            f"{job['program']}{case_suffix}"
                        ),
                        timeout_seconds=30,
                    )
                    assert_output_contract(completed.stdout or "", job, label)

                    for output_name in job.get("required_outputs", []):
                        if not (working_dir / output_name).exists():
                            raise AutomationError(f"{label} did not create {output_name}")

                    for output_spec in job.get("required_output_contains", []):
                        output_path = working_dir / output_spec["path"]
                        if not output_path.exists():
                            raise AutomationError(f"{label} did not create {output_spec['path']}")

                        output_text = output_path.read_text(encoding="utf-8")
                        for expected in output_spec.get("contains", []):
                            if expected not in output_text:
                                raise AutomationError(
                                    f"{label} output {output_spec['path']} did not contain "
                                    f"expected text: {expected}\nActual output:\n{output_text}"
                                )
                    executed_jobs += 1
                finally:
                    remove_paths(working_dir, cleanup_paths)

    if executed_jobs == 0:
        raise AutomationError("No exercise output contract jobs were executed.")

    if success_message is not None:
        print(success_message)
    elif language_filter is None:
        print(f"Exercise output contracts passed for {executed_jobs} jobs.")
    else:
        print(
            "Exercise output contracts passed for "
            f"{executed_jobs} jobs in language '{language_filter}'."
        )


def exercise_contract_key(
    target: str, *, language: str, config: dict[str, Any]
) -> tuple[str, str, str] | None:
    normalized = target.replace("\\", "/")
    expected_files = {
        language_exercise_file(config, exercise_id): exercise_id for exercise_id in ("01", "02")
    }
    pattern = (
        rf"^languages/{re.escape(language)}/([^/]+)/([^/]+)/"
        r"exercises/(?:solutions/)?([^/]+)$"
    )
    match = re.match(pattern, normalized)
    if not match:
        return None
    exercise_id = expected_files.get(match.group(3))
    if exercise_id is None:
        return None
    return match.group(1), match.group(2), exercise_id


def active_module_languages(ctx: RepoContext) -> list[str]:
    return [
        language
        for language, config in ctx.manifest.languages.items()
        if config.get("module_levels")
    ]


def documented_exercise_edge_cases(readme: Path, exercise_id: str) -> list[str]:
    text = readme.read_text(encoding="utf-8")
    specs = text.split("### Exercise Specs", maxsplit=1)[-1]
    match = re.search(
        rf"(?:^|\n){int(exercise_id)}\.\s.*?(?=\n[12]\.\s|\n## Check Your Work|"
        r"\n## Checkpoint|\Z)",
        specs,
        re.DOTALL,
    )
    if not match:
        return []
    edge_match = re.search(r"^- Edge cases:\s*(.+)$", match.group(0), re.MULTILINE)
    if not edge_match:
        return []
    raw = edge_match.group(1).strip().rstrip(".")
    return [part.replace("`", "").strip() for part in raw.split(";") if part.strip()]


def learning_exercise_config_failures(ctx: RepoContext) -> list[str]:
    failures: list[str] = []
    configured_keys: set[tuple[str, str, str, str]] = set()
    try:
        outcomes_by_module = load_curriculum_outcomes(ctx.scripts_dir)
    except CurriculumError as error:
        return [str(error)]

    for exercise in load_learning_exercises(ctx):
        language = exercise.get("language")
        level = exercise.get("level")
        module = exercise.get("module")
        exercise_id = exercise.get("exercise")
        key = (language, level, module, exercise_id)
        label = "/".join(str(part) for part in key)

        if not all(isinstance(part, str) and part for part in key):
            failures.append(f"scripts/learning_exercises.json: invalid identity -> {label}")
            continue
        typed_key = (language, level, module, exercise_id)
        if typed_key in configured_keys:
            failures.append(f"scripts/learning_exercises.json: duplicate exercise -> {label}")
        configured_keys.add(typed_key)

        config = ctx.manifest.languages.get(language)
        if config is None:
            failures.append(f"scripts/learning_exercises.json: unknown language -> {label}")
            continue
        if exercise_id not in {"01", "02"}:
            failures.append(f"scripts/learning_exercises.json: invalid exercise id -> {label}")
            continue
        expected_route_role = "guided" if exercise_id == "01" else "both"
        if exercise.get("route_role") != expected_route_role:
            failures.append(
                f"scripts/learning_exercises.json: {label} route_role must be {expected_route_role}"
            )
        if exercise.get("starter_mode") != "guided":
            failures.append(f"scripts/learning_exercises.json: {label} starter_mode must be guided")

        file_name = language_exercise_file(config, exercise_id)
        exercise_root = f"languages/{language}/{level}/{module}/exercises"
        expected_paths = {
            "starter": f"{exercise_root}/{file_name}",
            "solution": f"{exercise_root}/solutions/{file_name}",
        }
        for path_kind, expected_path in expected_paths.items():
            actual_path = exercise.get(path_kind)
            if actual_path != expected_path:
                failures.append(
                    f"scripts/learning_exercises.json: {label} {path_kind} must be {expected_path}"
                )
            elif not repo_path(ctx, actual_path).is_file():
                failures.append(
                    f"scripts/learning_exercises.json: missing {path_kind} -> {actual_path}"
                )

        starter_path = repo_path(ctx, expected_paths["starter"])
        solution_path = repo_path(ctx, expected_paths["solution"])
        if starter_path.is_file() and solution_path.is_file():
            starter_text = starter_path.read_text(encoding="utf-8")
            solution_text = solution_path.read_text(encoding="utf-8")
            if starter_text == solution_text:
                failures.append(
                    f"scripts/learning_exercises.json: starter equals solution -> {label}"
                )
            if has_template_narration(starter_text) or has_template_narration(solution_text):
                failures.append(
                    f"scripts/learning_exercises.json: template narration remains -> {label}"
                )
            if "TODO" not in starter_text:
                failures.append(f"scripts/learning_exercises.json: starter has no TODO -> {label}")
            if has_generic_starter_prompt(starter_text):
                failures.append(
                    f"scripts/learning_exercises.json: starter has a generic TODO -> {label}"
                )
            if guided_todo_count(starter_text) < 3:
                failures.append(
                    "scripts/learning_exercises.json: starter needs behavior-specific "
                    f"TODO 1, TODO 2, and TODO 3 -> {label}"
                )

        module_key = f"{level}/{module}"
        module_outcomes = outcomes_by_module.get(module_key)
        expected_outcome_ids = list(module_outcomes.ids) if module_outcomes else []
        if exercise.get("outcome_ids") != expected_outcome_ids:
            failures.append(
                "scripts/learning_exercises.json: "
                f"{label} outcome_ids must be {expected_outcome_ids}"
            )

        cases = exercise.get("cases")
        if not isinstance(cases, list) or not cases:
            failures.append(f"scripts/learning_exercises.json: no cases -> {label}")
        else:
            if len(cases) < 3:
                failures.append(
                    f"scripts/learning_exercises.json: at least three cases are required -> {label}"
                )
            case_names: set[str] = set()
            covered: set[str] = set()
            execution_cases: dict[str, int] = {}
            for index, case in enumerate(cases, start=1):
                if not isinstance(case, dict):
                    failures.append(
                        f"scripts/learning_exercises.json: {label} case {index} is invalid"
                    )
                    continue
                case_name = case.get("name")
                if not isinstance(case_name, str) or not case_name:
                    failures.append(
                        f"scripts/learning_exercises.json: {label} case {index} has no name"
                    )
                elif case_name in case_names:
                    failures.append(
                        f"scripts/learning_exercises.json: {label} duplicate case '{case_name}'"
                    )
                else:
                    case_names.add(case_name)
                if case.get("shared_execution") is True:
                    failures.append(
                        "scripts/learning_exercises.json: "
                        f"shared_execution is not allowed -> {label} case {index}"
                    )
                case_coverage = case.get("covers", [])
                if isinstance(case_coverage, list):
                    covered.update(item for item in case_coverage if isinstance(item, str))
                execution = json.dumps(
                    {
                        key: case.get(key)
                        for key in (
                            "input_lines",
                            "input_file",
                            "arguments",
                            "setup_files",
                            "working_dir",
                        )
                    },
                    sort_keys=True,
                )
                previous_case = execution_cases.get(execution)
                if previous_case is not None:
                    failures.append(
                        "scripts/learning_exercises.json: "
                        f"{label} case {index} duplicates case {previous_case} execution"
                    )
                else:
                    execution_cases.setdefault(execution, index)
                normalizers = case.get("oracle_normalizers", [])
                if not isinstance(normalizers, list) or any(
                    normalizer not in {"timings", "unordered_lines"} for normalizer in normalizers
                ):
                    failures.append(
                        "scripts/learning_exercises.json: "
                        f"{label} case {index} has invalid oracle_normalizers"
                    )
                if case.get("oracle_solution") is True and not has_valid_oracle_waiver(case):
                    failures.append(
                        "scripts/learning_exercises.json: oracle_solution requires "
                        f"oracle_waiver -> {label} case {index}"
                    )
                if not (
                    case.get("required_stdout_equals")
                    or case.get("required_stdout_contains")
                    or case.get("required_stdout_patterns")
                    or case.get("oracle_solution") is True
                ):
                    failures.append(
                        "scripts/learning_exercises.json: "
                        f"{label} case {index} has no assertions or solution oracle"
                    )
            if "normal" not in covered:
                failures.append(f"scripts/learning_exercises.json: no normal case -> {label}")
            readme = ctx.root / "languages" / language / level / module / "README.md"
            for edge in documented_exercise_edge_cases(readme, exercise_id):
                if edge not in covered:
                    failures.append(
                        f"scripts/learning_exercises.json: uncovered edge '{edge}' -> {label}"
                    )

    expected_keys = {
        (language, level, module, exercise_id)
        for language in active_module_languages(ctx)
        for level, modules in ctx.manifest.module_order.items()
        if level in ctx.manifest.languages[language].get("module_levels", [])
        for module in modules
        if module in expected_modules_for_language_level(ctx, language, level)
        for exercise_id in ("01", "02")
    }
    for missing in sorted(expected_keys - configured_keys):
        failures.append("scripts/learning_exercises.json: missing exercise -> " + "/".join(missing))
    for extra in sorted(configured_keys - expected_keys):
        failures.append(
            "scripts/learning_exercises.json: unexpected exercise -> " + "/".join(extra)
        )

    return failures


def parity_check_languages(ctx: RepoContext) -> list[str]:
    return active_module_languages(ctx)


def example_contract_key_for_language(language: str) -> str:
    return "project" if language == "csharp" else "program"


def example_contract_targets_for_smoke(config: dict[str, Any]) -> set[str]:
    if "example_projects" in config:
        return set(config.get("example_projects", []))
    return set(config.get("example_paths", []))


def all_module_example_contract_targets(ctx: RepoContext, language: str) -> set[str]:
    config = ctx.manifest.languages[language]
    targets: set[str] = set()
    for level in config.get("module_levels", []):
        for module in expected_modules_for_language_level(ctx, language, level):
            example_dir = ctx.root / "languages" / language / level / module / "example"
            if language == "csharp":
                projects = [
                    project
                    for project in example_dir.glob("*.csproj")
                    if 'Compile Include="main.cs"' in project.read_text(encoding="utf-8")
                ]
                if len(projects) == 1:
                    targets.add(projects[0].relative_to(ctx.root).as_posix())
                continue
            target = example_dir / language_example_main(config)
            targets.add(target.relative_to(ctx.root).as_posix())
    return targets


def module_example_path(ctx: RepoContext, language: str, level: str, module: str) -> Path:
    config = ctx.manifest.languages[language]
    return (
        ctx.root
        / "languages"
        / language
        / level
        / module
        / "example"
        / language_example_main(config)
    )


def curriculum_outcome_failures(ctx: RepoContext) -> list[str]:
    failures: list[str] = []
    try:
        outcomes_by_module = load_curriculum_outcomes(ctx.scripts_dir)
    except CurriculumError as error:
        return [str(error)]

    expected_modules = {
        f"{level}/{module}"
        for level, modules in ctx.manifest.module_order.items()
        for module in modules
    }
    missing_modules = sorted(expected_modules - set(outcomes_by_module))
    extra_modules = sorted(set(outcomes_by_module) - expected_modules)
    for module_key in missing_modules:
        failures.append(f"scripts/curriculum_outcomes.json: missing module -> {module_key}")
    for module_key in extra_modules:
        failures.append(f"scripts/curriculum_outcomes.json: unknown module -> {module_key}")

    active_languages = set(active_module_languages(ctx))
    for module_key, module_outcomes in outcomes_by_module.items():
        unknown_adaptations = sorted(set(module_outcomes.language_adaptations) - active_languages)
        for language in unknown_adaptations:
            failures.append(
                "scripts/curriculum_outcomes.json: "
                f"unknown language adaptation '{language}' -> {module_key}"
            )
        unknown_titles = sorted(set(module_outcomes.display_titles) - active_languages)
        for language in unknown_titles:
            failures.append(
                "scripts/curriculum_outcomes.json: "
                f"unknown display-title language '{language}' -> {module_key}"
            )
        if (
            module_outcomes.display_titles
            and set(module_outcomes.display_titles) != active_languages
        ):
            missing_titles = sorted(active_languages - set(module_outcomes.display_titles))
            failures.append(
                "scripts/curriculum_outcomes.json: "
                f"display titles incomplete for {module_key} -> {', '.join(missing_titles)}"
            )

        if module_key not in expected_modules:
            continue
        level, module = module_key.split("/", maxsplit=1)
        for language in sorted(active_languages):
            config = ctx.manifest.languages[language]
            if level not in config.get("module_levels", []):
                continue
            readme = ctx.root / "languages" / language / level / module / "README.md"
            text = readme.read_text(encoding="utf-8") if readme.is_file() else ""
            if "## Learning Outcomes" not in text:
                failures.append(f"{readme}: missing -> ## Learning Outcomes")
                continue
            for outcome_id in module_outcomes.ids:
                if not re.search(rf"^- `{re.escape(outcome_id)}`:\s+\S", text, re.MULTILINE):
                    failures.append(f"{readme}: missing outcome id -> {outcome_id}")
    return failures


def check_exercise_parity(ctx: RepoContext) -> None:
    failures: list[str] = []
    languages = parity_check_languages(ctx)

    for level, modules in ctx.manifest.module_order.items():
        for module in modules:
            for language in languages:
                config = ctx.manifest.languages[language]
                if level not in config.get("module_levels", []):
                    continue
                if module not in expected_modules_for_language_level(ctx, language, level):
                    continue
                for exercise_id in ("01", "02"):
                    exercise_path = (
                        ctx.root
                        / "languages"
                        / language
                        / level
                        / module
                        / "exercises"
                        / language_exercise_file(config, exercise_id)
                    )
                    if not exercise_path.is_file():
                        failures.append(f"{exercise_path}: missing exercise file for parity check")

    contracts = load_exercise_output_contracts(ctx)
    expected_levels = set(ctx.manifest.module_order.keys())
    expected_modules = {
        (level, module)
        for level, modules in ctx.manifest.module_order.items()
        for module in modules
    }
    contract_keys_by_language: dict[str, set[tuple[str, str, str]]] = {}

    unknown_languages = sorted(language for language in contracts if language not in languages)
    for language in unknown_languages:
        failures.append(f"scripts/learning_exercises.json: unexpected language key '{language}'")

    for language in languages:
        jobs = contracts.get(language, [])
        if not jobs:
            failures.append(
                f"scripts/learning_exercises.json: no contracts configured for {language}"
            )
            contract_keys_by_language[language] = set()
            continue

        config = ctx.manifest.languages[language]
        keys: set[tuple[str, str, str]] = set()
        for job in jobs:
            target = job.get("program")
            if not target:
                failures.append(
                    f"scripts/learning_exercises.json: {language} contract missing 'program' field"
                )
                continue

            target_path = repo_path(ctx, target)
            if not target_path.is_file():
                failures.append(
                    "scripts/learning_exercises.json: "
                    f"{language} contract target does not exist -> {target}"
                )

            key = exercise_contract_key(target, language=language, config=config)
            if key is None:
                failures.append(
                    "scripts/learning_exercises.json: "
                    f"{language} contract target must be a configured exercise file -> {target}"
                )
                continue

            level, module, exercise_id = key
            if level not in expected_levels:
                failures.append(
                    "scripts/learning_exercises.json: "
                    f"{language} contract uses unknown level '{level}' -> {target}"
                )
            if (level, module) not in expected_modules:
                failures.append(
                    "scripts/learning_exercises.json: "
                    f"{language} contract uses unknown module '{module}' in level '{level}' -> "
                    f"{target}"
                )
            if exercise_id not in {"01", "02"}:
                failures.append(
                    "scripts/learning_exercises.json: "
                    f"{language} contract exercise id must be 01 or 02 -> {target}"
                )
            keys.add(key)

            if not (
                job.get("required_stdout_equals")
                or job.get("required_stdout_contains")
                or job.get("required_stdout_patterns")
                or job.get("oracle_solution") is True
            ):
                failures.append(
                    "scripts/learning_exercises.json: "
                    f"{language} contract has no assertions or oracle -> {target}"
                )
            for pattern in job.get("required_stdout_patterns", []):
                if is_vacuous_stdout_pattern(pattern):
                    failures.append(
                        "scripts/learning_exercises.json: "
                        f"{language} contract has a vacuous stdout pattern -> {target}"
                    )

        contract_keys_by_language[language] = keys

    failures.extend(learning_exercise_config_failures(ctx))

    total_contracts = sum(len(keys) for keys in contract_keys_by_language.values())
    if total_contracts == 0:
        failures.append(
            "scripts/learning_exercises.json: no exercise contracts parsed for any language"
        )

    if failures:
        print("Exercise parity validation failed:")
        for failure in failures:
            print(f" - {failure}")
        raise AutomationError("Exercise parity validation failed.")

    print("Exercise parity validation passed.")


def module_focus_comment(path: Path) -> tuple[str | None, str | None]:
    lines = path.read_text(encoding="utf-8").splitlines()
    header_comment_lines: list[str] = []
    comment_pattern = (
        re.compile(r"^\s*#\s*(.*)$") if path.suffix == ".py" else re.compile(r"^\s*//\s*(.*)$")
    )

    for line in lines[:10]:
        if not line.strip():
            if header_comment_lines:
                continue
            continue
        comment_match = comment_pattern.match(line)
        if comment_match:
            header_comment_lines.append(comment_match.group(1).strip())
            continue
        break

    if not header_comment_lines:
        return None, None

    merged = " ".join(part for part in header_comment_lines if part).strip()
    focus_match = re.search(r"Module focus:\s*(.+?)(?=\s+Why it matters:|$)", merged)
    why_match = re.search(r"Why it matters:\s*(.+?\.)", merged)
    focus = focus_match.group(1).strip() if focus_match else None
    why = why_match.group(1).strip() if why_match else None
    return focus, why


def check_cross_language_parity(ctx: RepoContext) -> None:
    failures: list[str] = curriculum_outcome_failures(ctx)
    languages = parity_check_languages(ctx)

    for level, modules in ctx.manifest.module_order.items():
        for module in modules:
            focuses: dict[str, str] = {}
            why_lines: dict[str, str] = {}
            for language in languages:
                config = ctx.manifest.languages[language]
                if level not in config.get("module_levels", []):
                    continue
                if module not in expected_modules_for_language_level(ctx, language, level):
                    continue

                example_path = module_example_path(ctx, language, level, module)
                if not example_path.is_file():
                    failures.append(f"{example_path}: missing example entrypoint for parity check")
                    continue

                focus, why = module_focus_comment(example_path)
                if not focus:
                    failures.append(f"{example_path}: missing 'Module focus' header comment")
                else:
                    focuses[language] = focus
                if not why:
                    failures.append(f"{example_path}: missing 'Why it matters' header comment")
                else:
                    why_lines[language] = why

            focus_values = sorted(set(focuses.values()))
            if len(focus_values) > 1:
                details = ", ".join(
                    f"{language}={value}" for language, value in sorted(focuses.items())
                )
                failures.append(
                    "languages/*/"
                    f"{level}/{module}/example/*: "
                    f"module focus mismatch across tracks -> {details}"
                )

            why_values = sorted(set(why_lines.values()))
            if len(why_values) > 1:
                details = ", ".join(
                    f"{language}={value}" for language, value in sorted(why_lines.items())
                )
                failures.append(
                    "languages/*/"
                    f"{level}/{module}/example/*: "
                    f"'Why it matters' mismatch across tracks -> {details}"
                )

    contracts = load_example_output_contracts(ctx)
    for language in active_module_languages(ctx):
        contract_jobs = contracts.get(language, [])
        target_key = example_contract_key_for_language(language)
        contract_targets = {job.get(target_key) for job in contract_jobs}
        expected_targets = all_module_example_contract_targets(ctx, language)
        missing = sorted(target for target in expected_targets if target not in contract_targets)
        for target in missing:
            failures.append(
                f"scripts/example_output_contracts.json: missing {language} contract for {target}"
            )

    for language, jobs in contracts.items():
        for job in jobs:
            key = example_contract_key_for_language(language)
            target = job.get(key)
            if not target:
                failures.append(
                    "scripts/example_output_contracts.json: "
                    f"{language} contract missing '{key}' field"
                )
                continue
            target_path = repo_path(ctx, target)
            if not target_path.exists():
                failures.append(
                    "scripts/example_output_contracts.json: "
                    f"contract target does not exist -> {target}"
                )
            if not (
                job.get("required_stdout_equals")
                or job.get("required_stdout_contains")
                or job.get("required_stdout_patterns")
                or job.get("oracle_solution") is True
            ):
                failures.append(
                    "scripts/example_output_contracts.json: "
                    f"{language} contract has no assertions or oracle -> {target}"
                )
            for pattern in job.get("required_stdout_patterns", []):
                if is_vacuous_stdout_pattern(pattern):
                    failures.append(
                        "scripts/example_output_contracts.json: "
                        f"{language} contract has a vacuous stdout pattern -> {target}"
                    )

    if failures:
        print("Cross-language parity validation failed:")
        for failure in failures:
            print(f" - {failure}")
        raise AutomationError("Cross-language parity validation failed.")

    print("Cross-language parity validation passed.")


def test_automation(ctx: RepoContext) -> None:
    python_cmd = find_python_command()
    run_command(
        [
            python_cmd,
            "-m",
            "unittest",
            "discover",
            "-s",
            "scripts/tests",
            "-t",
            ".",
            "-p",
            "test_*.py",
        ],
        cwd=ctx.root,
        action="Automation unit tests",
    )
    print("Automation unit tests passed.")


def verify_repo(ctx: RepoContext) -> None:
    python_cmd = find_python_command()
    phases: list[tuple[str, Any]] = [
        ("Automation unit tests", lambda: test_automation(ctx)),
        (
            "Markdown links",
            lambda: run_command(
                [python_cmd, str(ctx.scripts_dir / "check-links.py")],
                action="Markdown link check",
            ),
        ),
        ("README structure", lambda: check_readme_structure(ctx)),
        ("Module completeness", lambda: check_module_completeness(ctx)),
        ("Checkpoint completeness", lambda: check_checkpoint_completeness(ctx)),
        ("Documentation sync", lambda: check_doc_sync(ctx)),
        ("Example comments", lambda: check_example_comments(ctx)),
        (
            "Education quality gate",
            lambda: audit_education_quality(ctx, fail_on_blocking_findings=True),
        ),
        ("Cross-language parity", lambda: check_cross_language_parity(ctx)),
        ("Exercise parity", lambda: check_exercise_parity(ctx)),
        ("Example output contracts", lambda: check_example_output_contracts(ctx)),
        ("Exercise output contracts", lambda: check_exercise_output_contracts(ctx)),
        ("Checkpoint solution contracts", lambda: check_solution_checkpoint_contracts(ctx)),
        ("Uncovered starter and auxiliary builds", lambda: build_verification_gaps(ctx)),
    ]

    verification_started = perf_counter()
    phase_durations: list[dict[str, Any]] = []
    for index, (name, action) in enumerate(phases, start=1):
        print(f"[{index}/{len(phases)}] {name}...")
        phase_started = perf_counter()
        action()
        duration = perf_counter() - phase_started
        phase_durations.append({"phase": name, "seconds": round(duration, 3)})
        print(f"[{index}/{len(phases)}] {name} completed in {duration:.2f}s.")

    total_duration = perf_counter() - verification_started
    timing_path = ctx.root / "build" / "reports" / "verify-repo-timings.json"
    timing_path.parent.mkdir(parents=True, exist_ok=True)
    timing_path.write_text(
        json.dumps(
            {
                "generated_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                "total_seconds": round(total_duration, 3),
                "phases": phase_durations,
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    print(f"Repository verification completed successfully in {total_duration:.2f}s.")
    print(f"Timing report: {timing_path.relative_to(ctx.root).as_posix()}")
