# 02 Core Capstone: File-Based Grade Analyzer

## Goal

Read `name score` pairs from a text file, validate entries, and write a summary report.

## Quick Run

```bash
go run main.go
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

## Extension Ideas

- Sort scores descending in report.
- Add pass/fail threshold summary.
