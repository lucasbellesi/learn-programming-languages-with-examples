# Assessment 02: Core

## Goal

Practice validation, counting, file output, and defensive logic.

## Task

Write a program that reads integer values until `-1`, then:

1. Ignores any value outside range `0..100`.
2. Prints count of valid values.
3. Prints min, max, and average for valid values.
4. Prints a frequency table by tens:
- `0-9`, `10-19`, ..., `90-100`
5. Saves the same report to `core_assessment_report.txt`.

## Learning Metadata

- Difficulty: Intermediate.
- Estimated Time: 45-60 minutes.
- Prerequisites: All `02-core` modules, especially `input-validation`, `maps-and-frequency-counting`, and `error-handling-and-defensive-programming`.
- Learning Focus: Prove validation, aggregation, defensive handling, and report generation under mixed-quality input.

## Learning Outcomes

- `COR-VAL-01`
- `COR-ALG-01`
- `COR-FIO-01`
- `COR-ERR-02`

## Quick Run

Run the checkpoint checker from the repository root. The starter is intentionally incomplete, so the first run establishes the work still to do:

~~~bash
python scripts/automation.py check-checkpoint --language cpp --kind assessment --level 02-core
~~~

## Sample Input

```text
12 17 31 77 91 105 64 -3 88 -1
```

## Expected Behavior

- `105` and `-3` are ignored.
- Only values in `0..100` are used for statistics and frequency table.
- If no valid values are entered, print a friendly message and still create the report file.

## Cross-Language Notes

- This is the canonical validation-and-counting assessment for the core level.
- Compared with the other tracks, it keeps the most explicit control over parse flow, ranges, and report generation.
- Use it to compare how each runtime expresses the same defensive-programming goal.

## Check Your Work

Implement the task in `starter/`, then run from the repository root:

```bash
python scripts/automation.py check-checkpoint --language cpp --kind assessment --level 02-core
```

Use `--solution` only after completing a full attempt. Each failed case reports targeted feedback without exposing the implementation.

## What To Check

- out-of-range or malformed values do not pollute the valid-score summary
- frequency buckets match the accepted scores exactly
- the generated report contains the same summary shape promised by the README
