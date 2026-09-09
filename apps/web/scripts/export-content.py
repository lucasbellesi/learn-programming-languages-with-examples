"""Build the web catalog from the canonical curriculum, without executing content."""

import json
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "scripts"))
from automation_core.guidance import format_hint, load_exercise_guidance  # noqa: E402
from automation_core.links import check_file  # noqa: E402

OUT = ROOT / "apps/web/generated"
MANIFEST = json.loads((ROOT / "scripts/automation_manifest.json").read_text())
EXERCISES = json.loads((ROOT / "scripts/learning_exercises.json").read_text())["exercises"]
CHECKPOINTS = json.loads((ROOT / "scripts/learning_checkpoints.json").read_text())["checkpoints"]
EXAMPLES = json.loads((ROOT / "scripts/example_output_contracts.json").read_text())["languages"]


def read(relative):
    path = (ROOT / relative).resolve()
    if not path.is_relative_to(ROOT) or not path.is_file():
        raise ValueError(f"Invalid curriculum path: {relative}")
    return path.read_text(encoding="utf-8")


def main():
    revision = (
        os.environ.get("VERCEL_GIT_COMMIT_SHA")
        or subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
    )
    if not re.fullmatch(r"[0-9a-f]{40}", revision):
        raise ValueError("A full content commit SHA is required")
    docs, activities, solutions = [], {}, {}
    for language, config in MANIFEST["languages"].items():
        for level, modules in MANIFEST["module_order"].items():
            for module in modules:
                base = f"languages/{language}/{level}/{module}"
                markdown = read(f"{base}/README.md")
                doc_id = f"{language}/{level}/{module}"
                entry = "Main.java" if language == "java" else f"main.{config['extension']}"
                example_path = f"{base}/example/{entry}"
                items = [
                    {
                        "id": f"{doc_id}/example",
                        "title": "Example",
                        "path": example_path,
                        "source": read(example_path),
                        "kind": "example",
                        "cases": [],
                        "hints": [],
                    }
                ]
                items[0]["support"] = [
                    {"name": p.name, "source": p.read_text(encoding="utf-8")}
                    for p in sorted((ROOT / base / "example").iterdir())
                    if p.suffix in {".h", ".hpp"}
                ]
                items[0]["cases"] = [
                    {**case, "name": case.get("name", "Example output")}
                    for case in EXAMPLES[language]
                    if case.get("program") == example_path
                    or (
                        language == "csharp"
                        and str(Path(case.get("project", "")).parent).replace("\\", "/")
                        == f"{base}/example"
                    )
                ]
                if level == "01-foundations" and not items[0]["cases"]:
                    raise ValueError(f"Missing example contract: {example_path}")
                exercises = [
                    e
                    for e in EXERCISES
                    if (e["language"], e["level"], e["module"]) == (language, level, module)
                ]
                if len(exercises) != 2:
                    raise ValueError(f"Expected two exercises: {doc_id}")
                for exercise in exercises:
                    activity_id = f"{doc_id}/{exercise['exercise']}"
                    guidance = load_exercise_guidance(
                        ROOT,
                        language=language,
                        level=level,
                        module=module,
                        exercise_id=exercise["exercise"],
                        outcome_ids=tuple(exercise["outcome_ids"]),
                    )
                    hints = [
                        format_hint(
                            guidance, language=language, level=level, module=module, stage=i
                        )
                        for i in (1, 2, 3)
                    ]
                    items.append(
                        {
                            "id": activity_id,
                            "title": f"Exercise {exercise['exercise']}",
                            "path": exercise["starter"],
                            "source": read(exercise["starter"]),
                            "kind": "exercise",
                            "cases": exercise["cases"],
                            "hints": hints,
                        }
                    )
                    solutions[activity_id] = {
                        "filename": Path(exercise["solution"]).name,
                        "source": read(exercise["solution"]),
                    }
                for item in items:
                    item.update(
                        language=language, enabled=level == "01-foundations", revision=revision
                    )
                    activities[item["id"]] = item
                docs.append(
                    {
                        "id": doc_id,
                        "language": language,
                        "level": level,
                        "kind": "module",
                        "title": re.search(r"^# (.+)", markdown, re.M)[1],
                        "markdown": markdown,
                        "path": f"{base}/README.md",
                        "activities": [item["id"] for item in items],
                    }
                )
        for checkpoint in [c for c in CHECKPOINTS if c["language"] == language]:
            kind, level = checkpoint["kind"], checkpoint["level"]
            path = f"languages/{language}/{kind}s/{level}/README.md"
            markdown = read(path)
            files = []
            for source in sorted((ROOT / checkpoint["starter"]).rglob("*")):
                if source.is_file() and not any(
                    part in {"bin", "obj", "build", "node_modules", "__pycache__"}
                    for part in source.parts
                ):
                    if source.suffix in {
                        ".cpp",
                        ".h",
                        ".hpp",
                        ".cs",
                        ".csproj",
                        ".go",
                        ".java",
                        ".py",
                        ".ts",
                        ".json",
                        ".md",
                        ".txt",
                    }:
                        files.append(
                            {
                                "path": source.relative_to(ROOT).as_posix(),
                                "source": source.read_text(encoding="utf-8"),
                            }
                        )
            docs.append(
                {
                    "id": f"{language}/{level}/{kind}",
                    "language": language,
                    "level": level,
                    "kind": kind,
                    "title": re.search(r"^# (.+)", markdown, re.M)[1],
                    "path": path,
                    "markdown": markdown,
                    "activities": [],
                    "files": files,
                }
            )
    if (
        len(docs) != 192
        or len(activities) != 432
        or sum(a["enabled"] for a in activities.values()) != 144
    ):
        raise ValueError("Curriculum coverage changed; review the web coverage contract")
    for document in docs:
        broken = check_file(ROOT, ROOT / document["path"])
        if broken:
            raise ValueError("Broken curriculum links: " + "; ".join(broken))
    OUT.mkdir(exist_ok=True)
    for name, data in {
        "catalog": {"revision": revision, "docs": docs, "activities": activities},
        "solutions": solutions,
    }.items():
        (OUT / f"{name}.json").write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
    print(
        f"Catalog: {len(docs)} documents, {len(activities)} activities, 144 executable activities"
    )


if __name__ == "__main__":
    main()
