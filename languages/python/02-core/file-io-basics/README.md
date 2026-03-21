# File I/O Basics (Python)

This module teaches safe text-file reading and writing with beginner-friendly patterns.

## Quick Run

~~~bash
python example/main.py
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

## Checkpoint

- [ ] I can open files safely and handle missing paths.
- [ ] I can parse and validate simple text rows.
- [ ] I can skip malformed data without aborting the run.
- [ ] I completed exercises/01.py.
- [ ] I completed exercises/02.py.
