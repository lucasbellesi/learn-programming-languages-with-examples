# Assessment 02: Core

## Goal

Practice validation, aggregation, file output, and defensive handling of mixed-quality input.

## Task

Write a program that:

1. Repeatedly reads integer scores until the user enters `-1`.
2. Accepts only values in the range `0..100`.
3. Ignores invalid numeric values outside the accepted range.
4. Prints:
- count of valid scores
- average score
- minimum score
- maximum score
- frequency table by tens (`0-9`, `10-19`, ..., `90-100`)
5. Writes the same report to `core_assessment_report.txt`.

## Learning Metadata

- Difficulty: Intermediate.
- Estimated Time: 45-60 minutes.
- Prerequisites: All `02-core` modules, especially `input-validation`, `maps-and-frequency-counting`, and `error-handling-and-defensive-programming`.
- Learning Focus: Prove validation, aggregation, defensive handling, and report generation under mixed-quality input.

## Quick Run

```bash
python main.py
```

## Sample Input

```text
91
88
72
105
60
-1
```

## Sample Output (shape)

```text
Valid scores: 4
Average: 77.75
Minimum: 60
Maximum: 91
Frequency:
- 0-9: 0
- 10-19: 0
- 20-29: 0
- 30-39: 0
- 40-49: 0
- 50-59: 0
- 60-69: 1
- 70-79: 1
- 80-89: 1
- 90-100: 1
Report written to core_assessment_report.txt
```

## What To Check

- out-of-range or malformed values do not pollute the valid-score summary
- frequency buckets match the accepted scores exactly
- the generated report contains the same summary shape promised by the README
