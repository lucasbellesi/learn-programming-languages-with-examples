from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

from scripts.automation_core.ops import (
    AutomationError,
    assert_output_contract,
    documented_exercise_edge_cases,
    exercise_contract_key,
    has_valid_oracle_waiver,
    has_template_narration,
    is_vacuous_stdout_pattern,
    output_contract_case_suffix,
    run_command,
)


class ContractHelperTests(unittest.TestCase):
    def test_run_command_can_set_a_reproducible_environment(self) -> None:
        completed = run_command(
            [sys.executable, "-c", "import os; print(os.environ['COURSE_LOCALE'])"],
            environment={"COURSE_LOCALE": "invariant"},
            capture_stdout=True,
        )
        self.assertEqual(completed.stdout.strip(), "invariant")

    def test_oracle_waiver_must_contain_a_reason(self) -> None:
        self.assertFalse(has_valid_oracle_waiver({"oracle_waiver": "  "}))
        self.assertTrue(has_valid_oracle_waiver({"oracle_waiver": "unordered runtime output"}))

    def test_template_narration_detects_legacy_exercise_guides(self) -> None:
        self.assertTrue(has_template_narration("/* Exercise Guide: copied boilerplate */"))
        self.assertFalse(has_template_narration("// Validate the count before allocating."))

    def test_contains_passes(self) -> None:
        assert_output_contract("Total: 10\n", {"required_stdout_contains": ["Total: 10"]}, "x")

    def test_contains_fails(self) -> None:
        with self.assertRaisesRegex(AutomationError, "expected text"):
            assert_output_contract("Total: 9\n", {"required_stdout_contains": ["Total: 10"]}, "x")

    def test_pattern_passes(self) -> None:
        assert_output_contract("Time: 42\n", {"required_stdout_patterns": [r"Time: \d+"]}, "x")

    def test_pattern_fails(self) -> None:
        with self.assertRaisesRegex(AutomationError, "expected pattern"):
            assert_output_contract(
                "Time: none\n", {"required_stdout_patterns": [r"Time: \d+"]}, "x"
            )

    def test_forbidden_passes(self) -> None:
        assert_output_contract("Ready\n", {"forbidden_stdout_contains": ["TODO"]}, "x")

    def test_oracle_requires_output(self) -> None:
        with self.assertRaisesRegex(AutomationError, "produced no output"):
            assert_output_contract("", {"oracle_solution": True}, "x")

    def test_oracle_accepts_output(self) -> None:
        assert_output_contract("Ready\n", {"oracle_solution": True}, "x")

    def test_oracle_capture_receives_output(self) -> None:
        captured: list[str] = []
        assert_output_contract("Ready\n", {"_capture_stdout": captured.append}, "x")
        self.assertEqual(captured, ["Ready\n"])

    def test_oracle_exact_output_rejects_difference(self) -> None:
        with self.assertRaisesRegex(AutomationError, "exact output contract"):
            assert_output_contract("Actual\n", {"required_stdout_equals": "Expected\n"}, "x")

    def test_oracle_timing_normalizer_ignores_measurements(self) -> None:
        assert_output_contract(
            "Elapsed time: 92.4 ms\n",
            {
                "_required_stdout_equals": "Elapsed time: 11.2 ms\n",
                "oracle_normalizers": ["timings"],
            },
            "x",
        )

    def test_timing_normalizer_handles_compact_second_units(self) -> None:
        assert_output_contract(
            "Concatenation: 0.000202s\nJoin: 0.000141s\n",
            {
                "required_stdout_equals": "Concatenation: 0.000208s\nJoin: 0.000143s\n",
                "oracle_normalizers": ["timings"],
            },
            "x",
        )

    def test_timing_normalizer_ignores_compact_unit_resolution(self) -> None:
        assert_output_contract(
            "Without capacity: 762.8µs\n",
            {
                "required_stdout_equals": "Without capacity: 0s\n",
                "oracle_normalizers": ["timings"],
            },
            "x",
        )

    def test_timing_normalizer_handles_units_in_labels(self) -> None:
        assert_output_contract(
            "Concatenation average ns: 200\n",
            {
                "required_stdout_equals": "Concatenation average ns: 220\n",
                "oracle_normalizers": ["timings"],
            },
            "x",
        )

    def test_oracle_unordered_lines_normalizer_ignores_order(self) -> None:
        assert_output_contract(
            "worker-b\nworker-a\n",
            {
                "_required_stdout_equals": "worker-a\nworker-b\n",
                "oracle_normalizers": ["unordered_lines"],
            },
            "x",
        )

    def test_vacuous_known_patterns(self) -> None:
        for pattern in (r"\S", r".+", r"[\s\S]+", r"(?s).+"):
            with self.subTest(pattern=pattern):
                self.assertTrue(is_vacuous_stdout_pattern(pattern))

    def test_specific_pattern_is_not_vacuous(self) -> None:
        self.assertFalse(is_vacuous_stdout_pattern(r"Total: \d+"))

    def test_invalid_regex_is_not_vacuous(self) -> None:
        self.assertFalse(is_vacuous_stdout_pattern("["))

    def test_case_suffix_named(self) -> None:
        self.assertEqual(output_contract_case_suffix({"name": "edge"}), " case 'edge'")

    def test_case_suffix_unnamed(self) -> None:
        self.assertEqual(output_contract_case_suffix({}), "")

    def test_contract_key_accepts_solution(self) -> None:
        config = {"extension": "py"}
        key = exercise_contract_key(
            "languages/python/01-foundations/sample/exercises/solutions/01.py",
            language="python",
            config=config,
        )
        self.assertEqual(key, ("01-foundations", "sample", "01"))

    def test_contract_key_rejects_wrong_filename(self) -> None:
        self.assertIsNone(
            exercise_contract_key(
                "languages/python/01-foundations/sample/exercises/03.py",
                language="python",
                config={"extension": "py"},
            )
        )

    def test_documented_edges_parse_semicolons(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "README.md"
            path.write_text(
                "### Exercise Specs\n\n1. task\n- Edge cases: `empty` input; duplicate values.\n\n"
                "2. task\n- Edge cases: zero.\n\n## Checkpoint\n",
                encoding="utf-8",
            )
            self.assertEqual(
                documented_exercise_edge_cases(path, "01"),
                ["empty input", "duplicate values"],
            )


if __name__ == "__main__":
    unittest.main()
