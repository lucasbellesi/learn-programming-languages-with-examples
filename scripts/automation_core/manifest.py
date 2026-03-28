from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class Manifest:
    data: dict[str, Any]

    @property
    def required_readme_headings(self) -> list[str]:
        return list(self.data["required_readme_headings"])

    @property
    def checkpoint_kinds(self) -> list[str]:
        return list(self.data["checkpoint_kinds"])

    @property
    def module_order(self) -> dict[str, list[str]]:
        return {key: list(value) for key, value in self.data["module_order"].items()}

    @property
    def languages(self) -> dict[str, dict[str, Any]]:
        return dict(self.data["languages"])

    @property
    def docs(self) -> dict[str, Any]:
        return dict(self.data["docs"])

    @property
    def smoke(self) -> dict[str, dict[str, Any]]:
        return dict(self.data["smoke"])

    @property
    def lint(self) -> dict[str, dict[str, Any]]:
        return dict(self.data["lint"])


def load_manifest(scripts_dir: Path) -> Manifest:
    manifest_path = scripts_dir / "automation_manifest.json"
    with manifest_path.open("r", encoding="utf-8") as handle:
        return Manifest(json.load(handle))
