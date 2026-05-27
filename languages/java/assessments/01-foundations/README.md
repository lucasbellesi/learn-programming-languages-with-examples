# Assessment 01: Foundations

## Goal

Build confidence with input handling, loops, methods, lists, and strings.

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

## Learning Metadata

- Difficulty: Beginner.
- Estimated Time: 30-45 minutes.
- Prerequisites: All `01-foundations` modules, especially `types-and-io`, `control-flow`, and `strings`.
- Learning Focus: Prove you can read structured input, preserve names, and compute accurate summaries without step-by-step scaffolding.

## Quick Run

```bash
javac -d build/java languages/java/assessments/01-foundations/Main.java
java -cp build/java Main
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
Average: 78.00
Highest: Ana Smith (91)
Lowest: Bob Lee (55)
Passed: 2/3
```

## Cross-Language Notes

- Compared with C++, Java keeps the assessment strongly typed with less setup code.
- Relative to Python and TypeScript, Java's explicit record type makes the stored data shape visible.
- The comparison to watch is how much structure is useful before introducing packages and projects.

## What To Check

- full names are preserved exactly as entered
- highest and lowest records match the actual dataset
- pass counts and averages use the required scoring rules
