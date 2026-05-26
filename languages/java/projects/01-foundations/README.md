# 01 Foundations Project: Student Score Summary

## Goal

Build a console program that reads student names and scores, then prints summary statistics.

## Learning Metadata

- Difficulty: Beginner.
- Estimated Time: 45-75 minutes.
- Prerequisites: All `01-foundations` modules, especially `types-and-io`, `control-flow`, and `arrays-and-vectors`.
- Learning Focus: Integrate validated input, record storage, and summary statistics in one small end-to-end Java program.

## Quick Run

```bash
javac -d build/java languages/java/projects/01-foundations/Main.java
java -cp build/java Main
```

## Requirements

- Ask for number of students.
- Read each student name as a full line and score with numeric validation.
- Keep score input in the range `0` to `100`.
- Print all student records.
- Print minimum score, maximum score, and average score.

## Concepts Practiced

- Console input with `Scanner`.
- Loops and conditionals.
- Lists and small records.
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
Average: 85.33
Minimum: 77
Maximum: 91
```

## Common Pitfalls

- Accepting empty names.
- Accepting invalid scores without retrying.
- Dividing by zero when no students are provided.

## Cross-Language Notes

- Compared with C++, Java keeps explicit types while avoiding manual memory management.
- Relative to Python, Java requires more structure up front but catches more type mistakes before execution.
- This checkpoint stays package-free so the compile and run path remains beginner-friendly.

## What To Check

- invalid score input is rejected or retried without corrupting later reads
- names with spaces stay intact from input to output
- reported average, minimum, and maximum match the entered records

## Extension Ideas

- Add grade letters (A/B/C).
- Sort output by score.
- Print pass/fail counts using a threshold.
