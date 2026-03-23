# Assessment 01: Foundations

## Goal

Build confidence with input handling, loops, functions, slices, and strings.

## Task

Write a program that:

1. Reads an integer `N` (`N > 0`).
2. Reads `N` full names and exam scores (`0..100`).
3. Prints:
- all records
- average score
- highest score with student name
- lowest score with student name
- pass count (`score >= 60`)

## Quick Run

```bash
go run main.go
```

## Sample Input

```text
3
Ana Smith
91
Bob Lee
55
Carla Mendez
88
```

## Sample Output (shape)

```text
Students:
- Ana Smith: 91
- Bob Lee: 55
- Carla Mendez: 88
Average: 78
Highest: Ana Smith (91)
Lowest: Bob Lee (55)
Passed: 2/3
```
