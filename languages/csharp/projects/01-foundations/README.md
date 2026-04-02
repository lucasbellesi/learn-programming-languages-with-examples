# 01 Foundations Capstone: Student Score Summary

## Goal

Build a console program that reads student names and scores, then prints summary statistics.

## Learning Metadata

- Difficulty: Beginner.
- Estimated Time: 45-75 minutes.
- Prerequisites: All `01-foundations` modules, especially `types-and-io`, `control-flow`, and `arrays-and-vectors`.
- Learning Focus: Integrate validated input, record storage, and summary statistics in one small end-to-end program.

## Quick Run

```bash
dotnet run --project foundations-project.csproj
```

## Requirements

- Ask for number of students.
- Read each student name with full-line input and score with numeric validation.
- Keep score input in the range `0` to `100`.
- Print all student records.
- Print minimum score, maximum score, and average score.

## Concepts Practiced

- Full-line input and numeric parsing.
- Loops and conditionals.
- `List<T>` for dynamic storage.
- Basic statistics: min, max, average.

## Sample Input

```text
3
Ana Smith
91
Bob Lee
77
Carla Mendez
88
```

## Sample Output

```text
Students:
- Ana Smith: 91
- Bob Lee: 77
- Carla Mendez: 88
Average: 85.33333333333333
Minimum: 77
Maximum: 91
```

## Common Pitfalls

- Accepting invalid scores without retrying.
- Forgetting that student names may contain spaces.
- Dividing by zero when no students are provided.

## Cross-Language Notes

- Compared with the C++ capstone, the same foundations goal is expressed with simpler console and collection APIs.
- Relative to Python and TypeScript, the program still keeps stronger type structure around records and summary logic.
- The useful comparison is beginner ergonomics under a managed, statically typed runtime.

## What To Check

- invalid score input is rejected or retried without corrupting later reads
- names with spaces stay intact from input to output
- reported average, minimum, and maximum match the entered records

## Extension Ideas

- Add grade letters (A/B/C).
- Sort output by score.
- Print pass/fail counts using a threshold.
