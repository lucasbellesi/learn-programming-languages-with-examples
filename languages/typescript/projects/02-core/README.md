# 02 Core Project: File-Based Grade Analyzer

## Goal

Build a TypeScript console program that reads student grades from a text file and writes a summary report.

## Learning Metadata

- Difficulty: Intermediate.
- Estimated Time: 60-90 minutes.
- Prerequisites: All `02-core` modules, especially `input-validation`, `file-io-basics`, and `error-handling-and-defensive-programming`.
- Learning Focus: Integrate file parsing, validation, and report generation without letting malformed rows stop the whole workflow.

## Quick Run

~~~bash
npm run build:typescript
node build/typescript/projects/02-core/main.js
~~~

## Requirements

- Read an input file path from stdin.
- Parse rows in the form `Full Name Score`.
- Skip invalid rows without crashing the program.
- Print a short summary to stdout.
- Write a detailed report to `report.txt`.

## Concepts Practiced

- File input and output.
- Defensive parsing.
- Arrays of structured records.
- Aggregation with summary statistics.

## Sample Input File

```text
Ana Smith 91
Bob Lee 77
InvalidRow
Carla Mendez 88
```

## Sample Output (shape)

```text
Valid records: 3
Invalid rows skipped: 1
Average: 85.33
Report written to report.txt
```

## Common Pitfalls

- Treating malformed rows as valid partial records.
- Accepting scores outside `0..100`.
- Writing the report without making its location explicit.

## Cross-Language Notes

- Compared with the C++ checkpoint, this version shifts the same parsing and reporting job onto Node file APIs and typed objects.
- Relative to Python, the compile-time type layer helps keep parsed record handling organized.
- The useful comparison is script-like I/O with stronger data-shape discipline.

## What To Check

- malformed rows are skipped without stopping valid processing
- the report file is created in the current working directory
- average, minimum, and maximum use only valid rows

## Extension Ideas

- Sort the report by score.
- Add grade buckets.
- Let the user choose the output file path.
