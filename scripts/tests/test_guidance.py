from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts.automation_core.guidance import format_hint, load_exercise_guidance


class GuidanceTests(unittest.TestCase):
    def test_loads_specs_and_formats_graduated_hints(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            module = root / "languages" / "python" / "01-foundations" / "sample"
            module.mkdir(parents=True)
            (module / "README.md").write_text(
                """# Sample

## Exercise Focus

- exercises/01.py: calculate a safe total.

### Exercise Specs

1. exercises/01.py
- Input: a count and numeric values.
- Output: the total.
- Edge cases: zero count; negative values.

## Check Your Work
""",
                encoding="utf-8",
            )

            guidance = load_exercise_guidance(
                root,
                language="python",
                level="01-foundations",
                module="sample",
                exercise_id="01",
                outcome_ids=("FND-01",),
            )

            self.assertIn("safe total", format_hint(
                guidance,
                language="python",
                level="01-foundations",
                module="sample",
                stage=1,
            ))
            self.assertIn("zero count", format_hint(
                guidance,
                language="python",
                level="01-foundations",
                module="sample",
                stage=2,
            ))
            self.assertIn("input", format_hint(
                guidance,
                language="python",
                level="01-foundations",
                module="sample",
                stage=3,
            ))


if __name__ == "__main__":
    unittest.main()
