# File I/O Basics

This module teaches safe text-file reading and writing with streams.

## Quick Run

```bash
g++ -std=c++17 -Wall -Wextra -pedantic example/main.cpp -o file_io_example
./file_io_example
```

## More Examples

- `example/csv-like-reader.cpp`:

```bash
g++ -std=c++17 -Wall -Wextra -pedantic example/csv-like-reader.cpp -o file_io_csv_like_reader
./file_io_csv_like_reader
```

## Topics Covered

- `std::ifstream` for reading files.
- `std::ofstream` for writing files.
- Parsing simple structured lines.
- Handling missing file errors.

## Common Pitfalls

- Assuming files always open successfully.
- Not handling malformed lines.
- Forgetting to close output files (or relying on scope without understanding it).

## Exercise Focus

- `exercises/01.cpp`: copy lines with line numbers.
- `exercises/02.cpp`: parse `name score` rows and compute average.

### Exercise Specs

1. `exercises/01.cpp`
- Input: source file path and destination file path.
- Output: destination file with numbered lines.
- Edge cases: missing source file; empty source file.

2. `exercises/02.cpp`
- Input: file path with rows: `name score`.
- Output: valid row count and average score.
- Edge cases: malformed rows; file with no valid rows.

## Checkpoint

- [ ] I can open files safely and validate stream state.
- [ ] I can parse simple file formats.
- [ ] I can generate output files from processed data.
- [ ] I completed both exercises.
