# Educational Example Review Rubric

Use this rubric when reviewing module entry examples under `languages/*/*/*/example/main.*`.

## Purpose

Keep examples easy to learn from while preserving technical correctness and cross-language parity.

## Review Checklist

- The file starts with a module-specific header comment that states the concept and why it matters.
- Comments are intent-first and appear before non-trivial logic blocks (validation, transformation, branching, output checks).
- The example follows one deterministic scenario so learners can rerun and compare outcomes.
- Output is explained in comments so learners can connect printed values to the code path.
- Language-specific adaptation notes are present only when concept mapping differs from C++ semantics.
- Naming and flow emphasize readability over cleverness.
- The example still matches the module topic and does not drift into unrelated concepts.

## Suggested Scoring

Score each category from 0 to 2.

- `Concept Framing`: clear concept + why it matters.
- `Narration Quality`: comments guide reasoning, not syntax.
- `Scenario Determinism`: same inputs lead to predictable learning output.
- `Output Explainability`: printed values are explained and verifiable.
- `Parity Discipline`: cross-language concept intent is preserved.

Interpretation:

- `9-10`: ready
- `7-8`: acceptable with minor polish
- `5-6`: needs focused revision
- `<5`: rewrite required before merge

## Tooling Support

Run the non-blocking audit report:

```bash
python scripts/automation.py audit-education-quality
```

Generated reports:

- `build/reports/education-quality-report.md`
- `build/reports/education-quality-report.json`
