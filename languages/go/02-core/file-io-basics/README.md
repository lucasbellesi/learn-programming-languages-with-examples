# File I/O Basics (Go)

This module teaches safe text-file reading and writing with simple stream patterns.

## Learning Metadata

- Difficulty: Intermediate.
- Estimated Time: 30-45 minutes.
- Prerequisites: `01-foundations/types-and-io`, `01-foundations/strings`.
- Cross-Language Lens: Compare text-file APIs, line parsing, and error handling styles while keeping the workflow conceptually identical.

## Quick Run

~~~bash
go run example/main.go
~~~

## Topics Covered

- Reading files line by line with `bufio.Scanner`.
- Writing summary files with `os.WriteFile`.
- Parsing `name score` rows with `strings.Fields` and `strconv.Atoi`.
- Handling malformed lines without stopping the full run.

## Common Pitfalls

- Assuming file paths always exist.
- Trusting every row format before validating token count.
- Ignoring parse errors from numeric conversion.

## Exercise Focus

- exercises/01.go: copy lines from one file to another with line numbers.
- exercises/02.go: parse `name score` rows, count invalid rows, and compute average.

### Exercise Specs

1. exercises/01.go
- Input: source file path and destination file path.
- Output: destination file with numbered lines (`1: ...`, `2: ...`).
- Edge cases: missing source file; empty source file.

2. exercises/02.go
- Input: file path with rows in the format `name score`.
- Output: valid row count, invalid row count, and average score.
- Edge cases: malformed rows; file with no valid rows.

## Checkpoint

- [ ] I can open files safely and handle missing paths.
- [ ] I can parse and validate simple text rows.
- [ ] I can skip malformed data without aborting the run.
- [ ] I completed exercises/01.go.
- [ ] I completed exercises/02.go.
