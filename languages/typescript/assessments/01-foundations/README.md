# Assessment 01: Foundations

## Goal

Build confidence with input handling, loops, functions, arrays, and strings.

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

~~~bash
npm run build:typescript
node build/typescript/assessments/01-foundations/main.js
~~~

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

- Compared with the C++ assessment, this version keeps the same input-and-summary challenge in a Node console setting.
- Relative to Python, static types give more guidance for records and aggregates without changing the runtime parsing model.
- The main comparison is typed beginner architecture over a scripting-style execution environment.

## What To Check

- full names are preserved exactly as entered
- highest and lowest records match the actual dataset
- pass counts and averages use the required scoring rules
