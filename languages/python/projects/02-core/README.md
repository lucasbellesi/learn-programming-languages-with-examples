# 02 Core Project: File-Based Grade Analyzer

## Goal

Build a program that reads student grades from a text file and writes a summary report.

## Learning Metadata

- Difficulty: Intermediate.
- Estimated Time: 60-90 minutes.
- Prerequisites: All `02-core` modules, especially `input-validation`, `file-io-basics`, and `error-handling-and-defensive-programming`.
- Learning Focus: Integrate parsing, validation, and file-backed reporting without letting malformed rows break the workflow.

## Quick Run

```bash
python main.py
```

## Requirements

- Ask for an input file path.
- Read lines in the format `Full Name Score`.
- Skip invalid rows without stopping the whole program.
- Print a short summary to the console.
- Write the detailed report to `report.txt`.

## Concepts Practiced

- File input and output.
- Defensive parsing.
- Lists and dictionaries.
- Basic aggregation.

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

- Failing when a line has too few columns.
- Accepting scores outside `0..100`.
- Overwriting the report without making it clear to the user.

## What To Check

- malformed rows are skipped or counted without crashing the program
- the report artifact is created in the expected working directory
- summary values are computed only from valid rows

## Extension Ideas

- Sort the report by score.
- Add grade buckets.
- Let the user choose the output file path.
