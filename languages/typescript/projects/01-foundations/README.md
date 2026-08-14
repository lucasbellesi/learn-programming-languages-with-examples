# 01 Foundations Capstone: Student Score Summary

## Goal

Build a console program that reads student names and scores, then prints summary statistics.

## Learning Metadata

- Difficulty: Beginner.
- Estimated Time: 45-75 minutes.
- Prerequisites: All `01-foundations` modules, especially `types-and-io`, `control-flow`, and `arrays-and-vectors`.
- Learning Focus: Integrate validated input, record storage, and summary statistics in one small end-to-end program.

## Learning Outcomes

- `FND-TIO-02`
- `FND-CFL-02`
- `FND-FUN-01`
- `FND-SEQ-02`

## Quick Run

Run the checkpoint checker from the repository root. The starter is intentionally incomplete, so the first run establishes the work still to do:

~~~bash
python scripts/automation.py check-checkpoint --language typescript --kind project --level 01-foundations
~~~

## Requirements

- Ask for number of students.
- Read each student name with full-line input and score with numeric validation.
- Keep score input in the range `0` to `100`.
- Print all student records.
- Print minimum score, maximum score, and average score.

## Milestones

1. Model the input and domain rules.
2. Implement the smallest end-to-end workflow.
3. Add validation and boundary behavior.
4. Refactor only after every configured case passes.

## Concepts Practiced

- Text parsing and validation loops.
- Arrays of structured records.
- Conditions and loops.
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
Average: 85.00
Minimum: 77
Maximum: 91
```

## Common Pitfalls

- Forgetting that all stdin input starts as text.
- Accepting invalid scores without retrying.
- Dividing by zero when no students are provided.

## Cross-Language Notes

- Compared with the C++ capstone, this version keeps the same learner goal but routes everything through Node string parsing.
- Relative to Python, the type layer gives more structure to records and summary calculations.
- The main comparison is beginner console programming with static guidance on top of a scripting runtime.

## What To Check

- invalid score input is rejected or retried without corrupting later reads
- names with spaces stay intact from input to output
- reported average, minimum, and maximum match the entered records

## Check Your Work

Implement the task in `starter/`, then run from the repository root:

```bash
python scripts/automation.py check-checkpoint --language typescript --kind project --level 01-foundations
```

Use `--solution` only after completing a full attempt. Each failed case reports targeted feedback without exposing the implementation.

## Extension Ideas

- Add grade letters (A/B/C).
- Sort output by score.
- Print pass/fail counts using a threshold.
