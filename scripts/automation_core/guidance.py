from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path


class GuidanceError(RuntimeError):
    pass


@dataclass(frozen=True)
class ExerciseGuidance:
    task: str
    input_contract: str
    output_contract: str
    edge_cases: str
    outcome_ids: tuple[str, ...]


LANGUAGE_TOOLBOX: dict[str, dict[str, str]] = {
    "cpp": {
        "io": "std::cin/std::getline and explicit stream-state recovery",
        "collections": "std::vector, iterators, and standard algorithms",
        "objects": "constructors, references, value semantics, and RAII",
        "concurrency": "std::thread, mutexes, futures, and scoped ownership",
    },
    "csharp": {
        "io": "Console.ReadLine, TryParse, and invariant numeric formatting",
        "collections": (
            "arrays, List<T>, Dictionary<TKey,TValue>, and LINQ where it clarifies intent"
        ),
        "objects": "constructors, interfaces, records/classes, and IDisposable",
        "concurrency": "Task, async coordination, locks, and deterministic disposal",
    },
    "go": {
        "io": "bufio.Scanner/Reader, fmt parsing, and explicit error checks",
        "collections": "slices, maps, range loops, and sort/search helpers",
        "objects": "structs, constructor functions, interfaces, and defer/Close",
        "concurrency": "goroutines, channels, sync primitives, and explicit completion",
    },
    "java": {
        "io": "Scanner or buffered input, parse methods, and explicit exceptions",
        "collections": "arrays, List, Map, streams, and Comparator helpers",
        "objects": "constructors, records/classes, interfaces, and defensive copies",
        "concurrency": "ExecutorService, futures, synchronization, and try-with-resources",
    },
    "python": {
        "io": "input, explicit conversion, exceptions, and context managers",
        "collections": "lists, dictionaries, comprehensions, and sorted helpers",
        "objects": "dataclasses/classes, copy boundaries, protocols, and with/finally",
        "concurrency": "threading/concurrent.futures, locks, and explicit result aggregation",
    },
    "typescript": {
        "io": "Node stdin/file APIs, Number conversion, and explicit narrowing",
        "collections": "arrays, Map, typed callbacks, and comparator functions",
        "objects": "interfaces/classes, nullable ownership slots, and explicit cleanup",
        "concurrency": "Promise coordination, async functions, and deterministic aggregation",
    },
}


def _section(text: str, start_heading: str, end_heading: str | None = None) -> str:
    end_pattern = rf"(?=^## {re.escape(end_heading)}\s*$)" if end_heading else r"\Z"
    match = re.search(
        rf"(?ms)^## {re.escape(start_heading)}\s*$\n(.*?){end_pattern}",
        text,
    )
    return match.group(1).strip() if match else ""


def _exercise_block(specs: str, exercise_id: str) -> str:
    number = int(exercise_id)
    match = re.search(
        rf"(?ms)^{number}\.\s+[^\n]+\n(.*?)(?=^\d+\.\s+|\Z)",
        specs,
    )
    return match.group(1).strip() if match else ""


def _field(block: str, label: str) -> str:
    match = re.search(rf"(?m)^- {re.escape(label)}:\s*(.+)$", block)
    return match.group(1).strip() if match else "Not specified; inspect the module example first."


def _toolbox_category(level: str, module: str) -> str:
    if level == "04-expert" and module in {
        "concurrency-basics",
        "performance-and-profiling-basics",
    }:
        return "concurrency"
    if level in {"03-advanced", "04-expert"}:
        return "objects"
    if module in {
        "arrays-and-vectors",
        "strings",
        "algorithms-basics",
        "sorting-and-searching",
        "maps-and-frequency-counting",
    }:
        return "collections"
    return "io"


def load_exercise_guidance(
    root: Path,
    *,
    language: str,
    level: str,
    module: str,
    exercise_id: str,
    outcome_ids: tuple[str, ...],
) -> ExerciseGuidance:
    readme = root / "languages" / language / level / module / "README.md"
    if not readme.is_file():
        raise GuidanceError(f"Module README does not exist: {readme}")

    text = readme.read_text(encoding="utf-8")
    focus = _section(text, "Exercise Focus", "Check Your Work")
    task_match = re.search(
        rf"(?m)^- .*?(?:{re.escape(exercise_id)}|Exercise{int(exercise_id):02d})[^:]*:\s*(.+)$",
        focus,
    )
    task = task_match.group(1).strip() if task_match else "Implement the named exercise behavior."
    specs_match = re.search(r"(?ms)^### Exercise Specs\s*$\n(.*?)(?=^## |\Z)", text)
    specs = specs_match.group(1).strip() if specs_match else ""
    block = _exercise_block(specs, exercise_id)
    return ExerciseGuidance(
        task=task,
        input_contract=_field(block, "Input"),
        output_contract=_field(block, "Output"),
        edge_cases=_field(block, "Edge cases"),
        outcome_ids=outcome_ids,
    )


def format_hint(
    guidance: ExerciseGuidance,
    *,
    language: str,
    level: str,
    module: str,
    stage: int,
) -> str:
    if stage == 1:
        outcomes = ", ".join(guidance.outcome_ids)
        return f"Conceptual hint: {guidance.task}\nOutcomes to demonstrate: {outcomes}."
    if stage == 2:
        return (
            "Structural hint:\n"
            f"- Read: {guidance.input_contract}\n"
            f"- Produce: {guidance.output_contract}\n"
            f"- Design the main path before handling: {guidance.edge_cases}"
        )
    if stage == 3:
        toolbox = LANGUAGE_TOOLBOX.get(language)
        if toolbox is None:
            raise GuidanceError(f"Unsupported language for hints: {language}")
        category = _toolbox_category(level, module)
        return (
            f"Language toolbox: consider {toolbox[category]}. "
            "Use only the pieces that make the required behavior clearer."
        )
    raise GuidanceError("Hint stage must be 1, 2, or 3.")
