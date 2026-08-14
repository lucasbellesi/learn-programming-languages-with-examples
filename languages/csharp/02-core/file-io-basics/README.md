# File I/O Basics (C#)

This module teaches safe text-file reading and writing with basic stream APIs.

## Learning Metadata

- Difficulty: Intermediate.
- Estimated Time: 30-45 minutes.
- Prerequisites: `01-foundations/types-and-io`, `01-foundations/strings`.
- Cross-Language Lens: Compare text-file APIs, line parsing, and error handling styles while keeping the workflow conceptually identical.

## Learning Outcomes

- `COR-FIO-01`: Read and write explicit paths while reporting I/O failures.
- `COR-FIO-02`: Parse records defensively and distinguish valid from rejected rows.

## Quick Run

Run from the repository root:

~~~bash
python scripts/automation.py run-module --module-path languages/csharp/02-core/file-io-basics
~~~

## Topics Covered

- Reading text files line by line with `StreamReader`.
- Writing summaries with `StreamWriter`.
- Validating simple `name score` rows with `TryParse`.
- Handling malformed lines without crashing the program.

## Common Pitfalls

- Assuming input files always exist.
- Parsing rows without checking token count first.
- Stopping at the first malformed line instead of skipping it safely.

## Cross-Language Notes

- C# keeps file work explicit but wraps it in a richer standard library than the C++ stream model.
- Compared with Go, Python, and TypeScript, the APIs often feel more feature-rich while staying strongly typed.
- The main comparison is convenience APIs without losing the need for validation and malformed-row handling.

## Exercise Focus

- exercises/01.cs: copy lines from one file to another with line numbers.
- exercises/02.cs: parse `name score` rows, count invalid rows, and compute average.

### Exercise Specs

1. exercises/01.cs
- Input: source file path and destination file path.
- Output: destination file with numbered lines (`1: ...`, `2: ...`).
- Edge cases: missing source file; empty source file.

2. exercises/02.cs
- Input: file path with rows in the format `name score`.
- Output: valid row count, invalid row count, and average score.
- Edge cases: malformed rows; file with no valid rows.

## Check Your Work

Run from the repository root after implementing a starter:

```bash
python scripts/automation.py check-exercise --language csharp --level 02-core --module file-io-basics --exercise 01
```

Change `--exercise 01` to `--exercise 02` for the second task. Consult `exercises/solutions/` only after making a complete attempt.

## Checkpoint

- [ ] I can open files safely and handle missing paths.
- [ ] I can parse and validate simple text rows.
- [ ] I can skip malformed data without aborting the run.
- [ ] I completed exercises/01.cs.
- [ ] I completed exercises/02.cs.
