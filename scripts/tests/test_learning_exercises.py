from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from scripts.automation_core.manifest import Manifest
from scripts.automation_core.ops import (
    AutomationError,
    RepoContext,
    assert_output_contract,
    check_learning_exercise,
)


class LearningExerciseTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        self.scripts_dir = self.root / "scripts"
        self.scripts_dir.mkdir()
        self.ctx = RepoContext(
            root=self.root,
            scripts_dir=self.scripts_dir,
            manifest=Manifest({}),
        )

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def write_config(self, exercises: list[dict[str, object]]) -> None:
        payload = {
            "case_sets": {
                "sample": [
                    {
                        "name": "visible case name",
                        "input_lines": ["input"],
                        "required_stdout_contains": ["expected"],
                    }
                ]
            },
            "exercises": exercises,
        }
        (self.scripts_dir / "learning_exercises.json").write_text(
            json.dumps(payload), encoding="utf-8"
        )

    @staticmethod
    def exercise_config() -> dict[str, object]:
        return {
            "language": "python",
            "level": "01-foundations",
            "module": "types-and-io",
            "exercise": "01",
            "starter": "starter.py",
            "solution": "solution.py",
            "case_set": "sample",
        }

    def create_sources(self) -> None:
        (self.root / "starter.py").write_text("print('starter')\n", encoding="utf-8")
        (self.root / "solution.py").write_text("print('solution')\n", encoding="utf-8")

    @patch("builtins.print")
    @patch("scripts.automation_core.ops.check_exercise_output_contracts")
    def test_selects_submission_and_preserves_case_name(self, check_contracts, _print) -> None:
        self.create_sources()
        self.write_config([self.exercise_config()])

        check_learning_exercise(
            self.ctx,
            language="python",
            level="01-foundations",
            module="types-and-io",
            exercise_id="01",
            submission="solution.py",
            use_solution=False,
        )

        contracts = check_contracts.call_args.kwargs["contracts_override"]
        self.assertEqual(contracts["python"][0]["program"], "solution.py")
        self.assertEqual(contracts["python"][0]["name"], "visible case name")

    def test_rejects_duplicate_exercise_configuration(self) -> None:
        config = self.exercise_config()
        self.write_config([config, dict(config)])

        with self.assertRaisesRegex(AutomationError, "Duplicate learner exercise"):
            check_learning_exercise(
                self.ctx,
                language="python",
                level="01-foundations",
                module="types-and-io",
                exercise_id="01",
                submission=None,
                use_solution=False,
            )

    @patch("scripts.automation_core.ops.check_exercise_output_contracts")
    def test_rejects_submission_outside_repository(self, check_contracts) -> None:
        self.create_sources()
        self.write_config([self.exercise_config()])

        with tempfile.TemporaryDirectory() as external_dir:
            external_source = Path(external_dir) / "submission.py"
            external_source.write_text("print('external')\n", encoding="utf-8")

            with self.assertRaisesRegex(AutomationError, "inside the repository"):
                check_learning_exercise(
                    self.ctx,
                    language="python",
                    level="01-foundations",
                    module="types-and-io",
                    exercise_id="01",
                    submission=str(external_source),
                    use_solution=False,
                )

        check_contracts.assert_not_called()

    @patch("scripts.automation_core.ops.check_exercise_output_contracts")
    def test_rejects_typescript_submission_outside_track(self, check_contracts) -> None:
        submission = self.root / "submission.ts"
        submission.write_text("console.log('submission');\n", encoding="utf-8")
        config = self.exercise_config()
        config["language"] = "typescript"
        config["starter"] = "languages/typescript/starter.ts"
        config["solution"] = "languages/typescript/solution.ts"
        self.write_config([config])

        with self.assertRaisesRegex(AutomationError, "under languages/typescript"):
            check_learning_exercise(
                self.ctx,
                language="typescript",
                level="01-foundations",
                module="types-and-io",
                exercise_id="01",
                submission="submission.ts",
                use_solution=False,
            )

        check_contracts.assert_not_called()

    def test_rejects_forbidden_output(self) -> None:
        with self.assertRaisesRegex(AutomationError, "printed forbidden text: Sum:"):
            assert_output_contract(
                "Count must be positive.\nSum: 0\n",
                {"forbidden_stdout_contains": ["Sum:"]},
                "sample contract",
            )


class EntryExerciseCoverageTests(unittest.TestCase):
    """Check that named error cases actually reach the advertised input boundary."""

    @classmethod
    def setUpClass(cls) -> None:
        path = Path(__file__).resolve().parents[1] / "learning_exercises.json"
        cls.exercises = {
            exercise["language"]: exercise
            for exercise in json.loads(path.read_text(encoding="utf-8"))["exercises"]
            if exercise["module"] == "types-and-io" and exercise["exercise"] == "02"
        }

    def test_wrong_token_count_covers_missing_and_extra_fields(self) -> None:
        for language in ("python", "csharp", "go"):
            with self.subTest(language=language):
                cases = [
                    case
                    for case in self.exercises[language]["cases"]
                    if "wrong token count" in case["covers"]
                ]
                counts = [len(" ".join(case["input_lines"]).split()) for case in cases]
                self.assertTrue(any(count < 3 for count in counts))
                self.assertTrue(any(count > 3 for count in counts))
                for case, count in zip(cases, counts):
                    self.assertNotEqual(count, 3)
                    self.assertIn("Invalid format.", case["required_stdout_equals"])
                    with self.assertRaises(AutomationError):
                        assert_output_contract(
                            "Enter product price quantity: Product: notebook\nTotal price: 0.00\n",
                            case,
                            language,
                        )

    def test_invalid_price_reaches_numeric_validation(self) -> None:
        case = next(
            case
            for case in self.exercises["typescript"]["cases"]
            if "invalid price should print an error" in case["covers"]
        )
        parts = " ".join(case["input_lines"]).split()
        self.assertEqual(len(parts), 3)
        with self.assertRaises(ValueError):
            float(parts[1])
        self.assertGreaterEqual(int(parts[2]), 0)
        self.assertEqual(case["required_stdout_equals"], "Invalid invoice data.\n")


if __name__ == "__main__":
    unittest.main()
