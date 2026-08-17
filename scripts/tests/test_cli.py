from __future__ import annotations

import unittest

from scripts.automation_core.ops import build_parser


class CliTests(unittest.TestCase):
    def setUp(self) -> None:
        self.parser = build_parser()

    def test_doctor_parses_language(self) -> None:
        args = self.parser.parse_args(["doctor", "--language", "go"])
        self.assertEqual(args.language, "go")

    def test_verify_language_parses_language(self) -> None:
        args = self.parser.parse_args(["verify-language", "--language", "java"])
        self.assertEqual(args.language, "java")

    def test_run_module_parses_path(self) -> None:
        args = self.parser.parse_args(["run-module", "--module-path", "languages/python/x"])
        self.assertEqual(args.module_path, "languages/python/x")

    def test_exercise_solution_flag(self) -> None:
        args = self.parser.parse_args(
            [
                "check-exercise",
                "--language",
                "python",
                "--level",
                "01-foundations",
                "--module",
                "sample",
                "--exercise",
                "01",
                "--solution",
            ]
        )
        self.assertTrue(args.solution)

    def test_checkpoint_solution_flag(self) -> None:
        args = self.parser.parse_args(
            [
                "check-checkpoint",
                "--language",
                "cpp",
                "--kind",
                "project",
                "--level",
                "04-expert",
                "--solution",
            ]
        )
        self.assertTrue(args.solution)

    def test_checkpoint_submission_parses(self) -> None:
        args = self.parser.parse_args(
            [
                "check-checkpoint",
                "--language",
                "python",
                "--kind",
                "assessment",
                "--level",
                "01-foundations",
                "--submission",
                "work",
            ]
        )
        self.assertEqual(args.submission, "work")

    def test_example_contract_language_filter(self) -> None:
        args = self.parser.parse_args(["check-example-output-contracts", "--language", "cpp"])
        self.assertEqual(args.language, "cpp")

    def test_exercise_contract_language_filter(self) -> None:
        args = self.parser.parse_args(["check-exercise-output-contracts", "--language", "go"])
        self.assertEqual(args.language, "go")

    def test_hint_exercise_parses_stage(self) -> None:
        args = self.parser.parse_args(
            [
                "hint-exercise",
                "--language",
                "python",
                "--level",
                "01-foundations",
                "--module",
                "types-and-io",
                "--exercise",
                "01",
                "--stage",
                "2",
            ]
        )
        self.assertEqual(args.stage, 2)


if __name__ == "__main__":
    unittest.main()
