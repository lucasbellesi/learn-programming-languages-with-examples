# 02 Core Capstone: File-Based Grade Analyzer

## Goal

Read `name score` pairs from a text file, validate entries, and write a summary report.

## Learning Metadata

- Difficulty: Intermediate.
- Estimated Time: 60-90 minutes.
- Prerequisites: All `02-core` modules, especially `input-validation`, `file-io-basics`, and `error-handling-and-defensive-programming`.
- Learning Focus: Integrate parsing, validation, and file-backed reporting without letting malformed rows break the workflow.

## Learning Outcomes

- `COR-VAL-01`
- `COR-ALG-01`
- `COR-FIO-01`
- `COR-ERR-02`

## Quick Run

Run the reference solution from the repository root:

```bash
python scripts/automation.py check-checkpoint --language csharp --kind project --level 02-core --solution
```

## Requirements

- Input file path from user.
- Parse each line as `name score`.
- Skip invalid rows with a warning count.
- Compute average, min, max, and count.
- Write report to `report.txt`.

## Sample Input File

```text
Ana 91
Bob 77
Carla 88
```

## Sample Output File

```text
Valid rows: 3
Invalid rows: 0
Average: 85.33333333333333
Minimum: 77
Maximum: 91
```

## Cross-Language Notes

- Compared with the C++ checkpoint, this version keeps the same validation goal but relies on a richer file API surface.
- Relative to Python and TypeScript, the report flow remains strongly typed from parse to output.
- The main comparison is convenience methods without relaxing correctness expectations.

## What To Check

- malformed rows are skipped or counted without crashing the program
- the report artifact is created in the expected working directory
- summary values are computed only from valid rows

## Check Your Work

Implement the task in `starter/`, then run from the repository root:

```bash
python scripts/automation.py check-checkpoint --language csharp --kind project --level 02-core
```

Use `--solution` only after completing a full attempt. Each failed case reports targeted feedback without exposing the implementation.

## Extension Ideas

- Sort scores descending in report.
- Add pass/fail threshold summary.
