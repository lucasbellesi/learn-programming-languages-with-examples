"""Regression coverage for authored journey references and completeness."""

import copy
import json
import sys
import unittest
from pathlib import Path

WEB = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(WEB / "scripts"))
from guided_content import attach_guides  # noqa: E402


class GuideTests(unittest.TestCase):
    def setUp(self):
        self.guides = json.loads((WEB / "content/guided-lessons.json").read_text())
        self.catalog = json.loads((WEB / "generated/catalog.json").read_text(encoding="utf-8"))

    def validate(self):
        attach_guides(self.guides, self.catalog["docs"], self.catalog["activities"])

    def test_fragments_are_extracted_from_the_canonical_example(self):
        self.validate()
        doc = next(d for d in self.catalog["docs"] if d["id"] == self.guides[0]["moduleId"])
        source = self.catalog["activities"][doc["guide"]["exampleId"]]["source"]
        for fragment in doc["guide"]["fragments"]:
            self.assertIn(fragment, source)

    def test_broken_references_fail(self):
        for field in ("exampleId", "moduleId", "nextModuleId"):
            with self.subTest(field=field):
                old = self.guides[0][field]
                self.guides[0][field] = "missing"
                with self.assertRaises(ValueError):
                    self.validate()
                self.guides[0][field] = old
        self.guides[0]["feedback"][0]["caseName"] = "missing"
        with self.assertRaises(ValueError):
            self.validate()

    def test_duplicate_and_incomplete_questions_fail(self):
        original = copy.deepcopy(self.guides)
        for mutate in (
            lambda g: g["prediction"].pop("correct"),
            lambda g: g["prediction"].update(explanation=""),
            lambda g: g["prediction"].update(correct="missing"),
            lambda g: g["review"][0].update(id=g["prediction"]["id"]),
            lambda g: g["steps"][0].update(id="predict"),
            lambda g: g["feedback"].pop(),
            lambda g: g["fragmentPrefixes"].append("missing"),
        ):
            self.guides = copy.deepcopy(original)
            mutate(self.guides[0])
            with self.assertRaises(ValueError):
                self.validate()


if __name__ == "__main__":
    unittest.main()
