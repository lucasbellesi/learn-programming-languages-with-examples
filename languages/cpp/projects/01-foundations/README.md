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
g++ -std=c++17 -Wall -Wextra -pedantic main.cpp -o foundations_capstone
./foundations_capstone
```

## Requirements

- Ask for number of students.
- Read each student name with `getline` and score with numeric validation.
- Keep score input in the range `0` to `100`.
- Print all student records.
- Print minimum score, maximum score, and average score.

## Concepts Practiced

- Input handling with `cin` and `getline`.
- Loops and conditionals.
- `vector` for dynamic storage.
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
Average: 85.3333
Minimum: 77
Maximum: 91
```

## Common Pitfalls

- Forgetting to clear the newline after reading numeric input.
- Accepting invalid scores without retrying.
- Dividing by zero when no students are provided.

## What To Check

- invalid score input is rejected or retried without corrupting later reads
- names with spaces stay intact from input to output
- reported average, minimum, and maximum match the entered records

## Extension Ideas

- Add grade letters (A/B/C).
- Sort output by score.
- Print pass/fail counts using a threshold.
