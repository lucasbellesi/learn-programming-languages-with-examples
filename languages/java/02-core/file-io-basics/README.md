# File I/O Basics (Java)

This module practices reading and writing small text files with Java's standard library.

## Learning Metadata

- Difficulty: Intermediate.
- Estimated Time: 35-50 minutes.
- Prerequisites: `01-foundations/strings`, `02-core/input-validation`.
- Cross-Language Lens: Compare Java's `Path` and `Files` APIs with file handling in C++, C#, Go, Python, and TypeScript.

## Learning Outcomes

- `COR-FIO-01`: Read and write explicit paths while reporting I/O failures.
- `COR-FIO-02`: Parse records defensively and distinguish valid from rejected rows.

## Quick Run

Run from the repository root:

~~~bash
python scripts/automation.py run-module --module-path languages/java/02-core/file-io-basics
~~~

## Topics Covered

- Creating paths with `Path.of`.
- Reading all lines from a text file.
- Writing reports with `Files.write`.
- Skipping malformed records during file processing.

## Common Pitfalls

- Assuming every line has the expected shape.
- Forgetting that file paths are resolved relative to the process working directory.
- Writing output before validating the records that feed it.

## Cross-Language Notes

- Java file APIs throw checked `IOException`, so examples declare `throws IOException`.
- `List<String>` is a natural first structure for small text files.
- Larger programs should stream files, but this module keeps data small for clarity.

## Exercise Focus

- exercises/Exercise01.java: copy lines from one file to another with line numbers.
- exercises/Exercise02.java: read score records, skip invalid rows, and write a grade report.

### Exercise Specs

1. exercises/Exercise01.java
- Input: input file path and output file path.
- Output: count of copied lines.
- Edge cases: empty file; repeated lines.

2. exercises/Exercise02.java
- Input: input file path and output file path.
- Output: valid record count, skipped row count, average score, and report path.
- Edge cases: malformed rows; scores outside 0..100.

## Check Your Work

Run from the repository root after implementing a starter:

```bash
python scripts/automation.py check-exercise --language java --level 02-core --module file-io-basics --exercise 01
```

Change `--exercise 01` to `--exercise 02` for the second task. Consult `exercises/solutions/` only after making a complete attempt.

## Checkpoint

- [ ] I can read all lines from a text file.
- [ ] I can write a derived report to a new file.
- [ ] I completed exercises/Exercise01.java.
- [ ] I completed exercises/Exercise02.java.
- [ ] I cleaned up temporary files after testing.
