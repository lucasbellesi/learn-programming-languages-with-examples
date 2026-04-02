# 02 Core Capstone: File-Based Grade Analyzer

## Goal

Read `name score` pairs from a text file, validate entries, and write a summary report.

## Learning Metadata

- Difficulty: Intermediate.
- Estimated Time: 60-90 minutes.
- Prerequisites: All `02-core` modules, especially `input-validation`, `file-io-basics`, and `error-handling-and-defensive-programming`.
- Learning Focus: Integrate parsing, validation, and file-backed reporting without letting malformed rows break the workflow.

## Quick Run

```bash
g++ -std=c++17 -Wall -Wextra -pedantic main.cpp -o core_capstone
./core_capstone
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
Average: 85.3333
Minimum: 77
Maximum: 91
```

## Cross-Language Notes

- This is the canonical file-processing checkpoint: parse rows, reject malformed input, and write a report deterministically.
- Compared with higher-level tracks, C++ exposes more of the mechanics of streams and parse loops.
- The useful cross-language question is how much library convenience changes the same defensive workflow.

## What To Check

- malformed rows are skipped or counted without crashing the program
- the report artifact is created in the expected working directory
- summary values are computed only from valid rows

## Extension Ideas

- Sort scores descending in report.
- Add pass/fail threshold summary.
