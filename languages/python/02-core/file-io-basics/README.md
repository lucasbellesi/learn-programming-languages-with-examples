# File I/O Basics (Python)

This module teaches safe text-file reading and writing with beginner-friendly patterns.

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
python scripts/automation.py run-module --module-path languages/python/02-core/file-io-basics
~~~

## Topics Covered

- Reading files line by line with context managers.
- Writing summary files safely with explicit output paths.
- Parsing `name score` rows with split and integer conversion.
- Skipping malformed rows while keeping the program stable.

## Common Pitfalls

- Assuming input files always exist.
- Parsing rows without checking token count first.
- Letting one malformed row terminate the full run.

## Cross-Language Notes

- Python makes file processing compact, so the comparison with C++ and Go highlights how little ceremony is required to read and transform text.
- Compared with C#, the code often becomes shorter, but validation discipline matters just as much.
- The key lesson is that concise I/O does not remove the need for defensive parsing.

## Exercise Focus

- exercises/01.py: copy lines from one file to another with line numbers.
- exercises/02.py: parse `name score` rows, count invalid rows, and compute average.

### Exercise Specs

1. exercises/01.py
- Input: source file path and destination file path.
- Output: destination file with numbered lines (`1: ...`, `2: ...`).
- Edge cases: missing source file; empty source file.

2. exercises/02.py
- Input: file path with rows in the format `name score`.
- Output: valid row count, invalid row count, and average score.
- Edge cases: malformed rows; file with no valid rows.

## Check Your Work

Run from the repository root after implementing a starter:

```bash
python scripts/automation.py check-exercise --language python --level 02-core --module file-io-basics --exercise 01
```

Change `--exercise 01` to `--exercise 02` for the second task. Consult `exercises/solutions/` only after making a complete attempt.

## Checkpoint

- [ ] I can open files safely and handle missing paths.
- [ ] I can parse and validate simple text rows.
- [ ] I can skip malformed data without aborting the run.
- [ ] I completed exercises/01.py.
- [ ] I completed exercises/02.py.
