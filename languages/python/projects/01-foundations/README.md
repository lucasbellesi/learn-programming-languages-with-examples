# 01 Foundations Project: Student Score Summary

## Goal

Build a console program that reads student names and scores, then prints summary statistics.

## Quick Run

```bash
python main.py
```

## Requirements

- Ask for number of students.
- Read each student name as a full line and score with numeric validation.
- Keep score input in the range `0` to `100`.
- Print all student records.
- Print minimum score, maximum score, and average score.

## Concepts Practiced

- Input handling with `input`.
- Loops and conditionals.
- Lists and dictionaries.
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

## Extension Ideas

- Add grade letters (A/B/C).
- Sort output by score.
- Print pass/fail counts using a threshold.
