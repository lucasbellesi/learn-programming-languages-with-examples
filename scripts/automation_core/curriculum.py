from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


class CurriculumError(RuntimeError):
    pass


@dataclass(frozen=True)
class Outcome:
    id: str
    description: str


@dataclass(frozen=True)
class ModuleOutcomes:
    outcomes: tuple[Outcome, ...]
    language_adaptations: dict[str, tuple[str, ...]]
    display_titles: dict[str, str]

    @property
    def ids(self) -> tuple[str, ...]:
        return tuple(outcome.id for outcome in self.outcomes)


def load_json_object(path: Path) -> dict[str, Any]:
    if not path.is_file():
        raise CurriculumError(f"Missing curriculum file: {path}")
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise CurriculumError(f"{path}: expected a top-level object.")
    return payload


def load_curriculum_outcomes(scripts_dir: Path) -> dict[str, ModuleOutcomes]:
    path = scripts_dir / "curriculum_outcomes.json"
    payload = load_json_object(path)
    modules = payload.get("modules")
    if not isinstance(modules, dict):
        raise CurriculumError(f"{path}: expected a 'modules' object.")

    result: dict[str, ModuleOutcomes] = {}
    seen_ids: set[str] = set()
    for module_key, raw_module in modules.items():
        if not isinstance(module_key, str) or "/" not in module_key:
            raise CurriculumError(f"{path}: invalid module key {module_key!r}.")
        if not isinstance(raw_module, dict):
            raise CurriculumError(f"{path}: module '{module_key}' must be an object.")
        raw_outcomes = raw_module.get("outcomes")
        if not isinstance(raw_outcomes, list) or not 2 <= len(raw_outcomes) <= 4:
            raise CurriculumError(f"{path}: module '{module_key}' must define 2 to 4 outcomes.")

        outcomes: list[Outcome] = []
        for raw_outcome in raw_outcomes:
            if not isinstance(raw_outcome, dict):
                raise CurriculumError(f"{path}: invalid outcome in '{module_key}'.")
            outcome_id = raw_outcome.get("id")
            description = raw_outcome.get("description")
            if not isinstance(outcome_id, str) or not outcome_id:
                raise CurriculumError(f"{path}: outcome in '{module_key}' has no id.")
            if not isinstance(description, str) or not description:
                raise CurriculumError(f"{path}: outcome '{outcome_id}' has no description.")
            if outcome_id in seen_ids:
                raise CurriculumError(f"{path}: duplicate outcome id '{outcome_id}'.")
            seen_ids.add(outcome_id)
            outcomes.append(Outcome(outcome_id, description))

        raw_adaptations = raw_module.get("language_adaptations", {})
        if not isinstance(raw_adaptations, dict):
            raise CurriculumError(
                f"{path}: language adaptations for '{module_key}' must be an object."
            )
        adaptations: dict[str, tuple[str, ...]] = {}
        for language, notes in raw_adaptations.items():
            if (
                not isinstance(language, str)
                or not isinstance(notes, list)
                or not all(isinstance(note, str) and note for note in notes)
            ):
                raise CurriculumError(f"{path}: invalid language adaptation for '{module_key}'.")
            adaptations[language] = tuple(notes)

        raw_display_titles = raw_module.get("display_titles", {})
        if not isinstance(raw_display_titles, dict) or any(
            not isinstance(language, str) or not isinstance(title, str) or not title.strip()
            for language, title in raw_display_titles.items()
        ):
            raise CurriculumError(f"{path}: invalid display titles for '{module_key}'.")

        result[module_key] = ModuleOutcomes(
            tuple(outcomes),
            adaptations,
            dict(raw_display_titles),
        )
    return result


def load_learning_checkpoints(scripts_dir: Path) -> list[dict[str, Any]]:
    path = scripts_dir / "learning_checkpoints.json"
    payload = load_json_object(path)
    checkpoints = payload.get("checkpoints")
    if not isinstance(checkpoints, list):
        raise CurriculumError(f"{path}: expected a 'checkpoints' list.")
    if not all(isinstance(checkpoint, dict) for checkpoint in checkpoints):
        raise CurriculumError(f"{path}: every checkpoint must be an object.")
    return [dict(checkpoint) for checkpoint in checkpoints]
