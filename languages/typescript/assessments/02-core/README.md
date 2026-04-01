# Assessment 02: Core

## Goal

Practice validation, aggregation, file output, and defensive handling of mixed-quality numeric input.

## Task

Write a program that:

1. Reads integer tokens until the user enters `-1`.
2. Accepts only values in the range `0..100`.
3. Ignores malformed tokens and out-of-range values.
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

~~~bash
npm run build:typescript
node build/typescript/assessments/02-core/main.js
~~~

## Sample Input

```text
12 17 31 77 91 105 64 -3 88 -1
```

## Sample Output (shape)

```text
Valid count: 6
Minimum: 12
Maximum: 91
Average: 58.166666666666664
Frequency table:
0-9: 0
10-19: 1
20-29: 0
30-39: 1
40-49: 0
50-59: 0
60-69: 1
70-79: 1
80-89: 1
90-100: 1
Report saved to core_assessment_report.txt
```

## What To Check

- malformed and out-of-range values do not pollute valid statistics
- frequency buckets match the accepted scores exactly
- the generated report contains the same summary shape printed to stdout
