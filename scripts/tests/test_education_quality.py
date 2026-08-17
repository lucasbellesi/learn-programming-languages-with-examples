import unittest

from scripts.automation_core.ops import guided_todo_count, has_generic_starter_prompt


class EducationQualityTests(unittest.TestCase):
    def test_generic_prompts_are_detected_case_insensitively(self) -> None:
        self.assertTrue(has_generic_starter_prompt("// TODO: Implement the README specification"))
        self.assertFalse(has_generic_starter_prompt("// TODO 2: reject negative account balances"))

    def test_guided_scaffold_requires_three_numbered_steps(self) -> None:
        text = "\n".join(["TODO 1: prepare", "TODO 2: transform", "TODO 3: report"])
        self.assertEqual(guided_todo_count(text), 3)


if __name__ == "__main__":
    unittest.main()
