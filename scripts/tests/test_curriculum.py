from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from scripts.automation_core.curriculum import (
    CurriculumError,
    load_curriculum_outcomes,
    load_json_object,
    load_learning_checkpoints,
)


class CurriculumTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def write(self, name: str, payload: object) -> None:
        (self.root / name).write_text(json.dumps(payload), encoding="utf-8")

    def valid_outcomes(self) -> dict[str, object]:
        return {
            "modules": {
                "01-foundations/sample": {
                    "outcomes": [
                        {"id": "A-01", "description": "First"},
                        {"id": "A-02", "description": "Second"},
                    ]
                }
            }
        }

    def test_load_json_rejects_missing_file(self) -> None:
        with self.assertRaisesRegex(CurriculumError, "Missing curriculum"):
            load_json_object(self.root / "missing.json")

    def test_load_json_rejects_list_root(self) -> None:
        self.write("sample.json", [])
        with self.assertRaisesRegex(CurriculumError, "top-level object"):
            load_json_object(self.root / "sample.json")

    def test_outcomes_load_ids(self) -> None:
        self.write("curriculum_outcomes.json", self.valid_outcomes())
        result = load_curriculum_outcomes(self.root)
        self.assertEqual(result["01-foundations/sample"].ids, ("A-01", "A-02"))

    def test_outcomes_require_modules_object(self) -> None:
        self.write("curriculum_outcomes.json", {})
        with self.assertRaisesRegex(CurriculumError, "modules"):
            load_curriculum_outcomes(self.root)

    def test_outcomes_require_two_to_four(self) -> None:
        payload = self.valid_outcomes()
        payload["modules"]["01-foundations/sample"]["outcomes"] = [
            {"id": "A-01", "description": "First"}
        ]
        self.write("curriculum_outcomes.json", payload)
        with self.assertRaisesRegex(CurriculumError, "2 to 4"):
            load_curriculum_outcomes(self.root)

    def test_outcomes_reject_duplicate_ids(self) -> None:
        payload = self.valid_outcomes()
        payload["modules"]["02-core/other"] = {
            "outcomes": [
                {"id": "A-01", "description": "Duplicate"},
                {"id": "B-02", "description": "Second"},
            ]
        }
        self.write("curriculum_outcomes.json", payload)
        with self.assertRaisesRegex(CurriculumError, "duplicate outcome"):
            load_curriculum_outcomes(self.root)

    def test_outcomes_reject_missing_description(self) -> None:
        payload = self.valid_outcomes()
        payload["modules"]["01-foundations/sample"]["outcomes"][0]["description"] = ""
        self.write("curriculum_outcomes.json", payload)
        with self.assertRaisesRegex(CurriculumError, "no description"):
            load_curriculum_outcomes(self.root)

    def test_outcomes_load_adaptations(self) -> None:
        payload = self.valid_outcomes()
        payload["modules"]["01-foundations/sample"]["language_adaptations"] = {
            "python": ["Dynamic typing lens"]
        }
        self.write("curriculum_outcomes.json", payload)
        result = load_curriculum_outcomes(self.root)
        self.assertEqual(
            result["01-foundations/sample"].language_adaptations["python"],
            ("Dynamic typing lens",),
        )

    def test_outcomes_reject_invalid_adaptation(self) -> None:
        payload = self.valid_outcomes()
        payload["modules"]["01-foundations/sample"]["language_adaptations"] = {"python": "invalid"}
        self.write("curriculum_outcomes.json", payload)
        with self.assertRaisesRegex(CurriculumError, "invalid language adaptation"):
            load_curriculum_outcomes(self.root)

    def test_outcomes_load_display_titles(self) -> None:
        payload = self.valid_outcomes()
        payload["modules"]["01-foundations/sample"]["display_titles"] = {
            "python": "Native Sample Title"
        }
        self.write("curriculum_outcomes.json", payload)
        result = load_curriculum_outcomes(self.root)
        self.assertEqual(
            result["01-foundations/sample"].display_titles["python"],
            "Native Sample Title",
        )

    def test_outcomes_reject_invalid_display_title(self) -> None:
        payload = self.valid_outcomes()
        payload["modules"]["01-foundations/sample"]["display_titles"] = {"python": ""}
        self.write("curriculum_outcomes.json", payload)
        with self.assertRaisesRegex(CurriculumError, "invalid display titles"):
            load_curriculum_outcomes(self.root)

    def test_checkpoints_load_copy(self) -> None:
        self.write("learning_checkpoints.json", {"checkpoints": [{"language": "python"}]})
        result = load_learning_checkpoints(self.root)
        self.assertEqual(result, [{"language": "python"}])

    def test_checkpoints_require_list(self) -> None:
        self.write("learning_checkpoints.json", {"checkpoints": {}})
        with self.assertRaisesRegex(CurriculumError, "checkpoints.*list"):
            load_learning_checkpoints(self.root)

    def test_checkpoints_reject_non_object(self) -> None:
        self.write("learning_checkpoints.json", {"checkpoints": ["bad"]})
        with self.assertRaisesRegex(CurriculumError, "every checkpoint"):
            load_learning_checkpoints(self.root)


if __name__ == "__main__":
    unittest.main()
