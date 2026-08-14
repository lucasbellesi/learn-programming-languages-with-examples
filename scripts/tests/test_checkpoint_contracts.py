from __future__ import annotations

import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

from scripts.automation_core.ops import (
    AutomationError,
    check_solution_checkpoint_contracts,
)


class CheckpointContractTests(unittest.TestCase):
    def setUp(self) -> None:
        self.ctx = SimpleNamespace(
            scripts_dir=Path("scripts"),
            manifest=SimpleNamespace(languages={"cpp": {}, "java": {}}),
        )

    @patch("scripts.automation_core.ops.check_learning_checkpoint")
    @patch("scripts.automation_core.ops.load_learning_checkpoints")
    def test_filters_and_runs_solution_contracts(self, load_checkpoints, check_checkpoint) -> None:
        load_checkpoints.return_value = [
            {"language": "java", "kind": "project", "level": "02-core"},
            {"language": "cpp", "kind": "assessment", "level": "01-foundations"},
            {"language": "cpp", "kind": "project", "level": "01-foundations"},
        ]

        check_solution_checkpoint_contracts(self.ctx, language_filter="cpp")

        self.assertEqual(check_checkpoint.call_count, 2)
        check_checkpoint.assert_any_call(
            self.ctx,
            language="cpp",
            kind="assessment",
            level="01-foundations",
            submission=None,
            use_solution=True,
        )
        check_checkpoint.assert_any_call(
            self.ctx,
            language="cpp",
            kind="project",
            level="01-foundations",
            submission=None,
            use_solution=True,
        )

    @patch("scripts.automation_core.ops.load_learning_checkpoints", return_value=[])
    def test_rejects_empty_selection(self, _load_checkpoints) -> None:
        with self.assertRaisesRegex(AutomationError, "No checkpoint contracts configured"):
            check_solution_checkpoint_contracts(self.ctx, language_filter="cpp")

    def test_rejects_unknown_language(self) -> None:
        with self.assertRaisesRegex(AutomationError, "Unsupported checkpoint language filter"):
            check_solution_checkpoint_contracts(self.ctx, language_filter="rust")


if __name__ == "__main__":
    unittest.main()
