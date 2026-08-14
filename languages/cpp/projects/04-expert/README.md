# 04 Expert Capstone: Resource Pipeline Monitor

## Goal

Build a small pipeline simulator using RAII-style ownership and timing metrics.

## Learning Metadata

- Difficulty: Advanced.
- Estimated Time: 75-105 minutes.
- Prerequisites: All `04-expert` modules, especially `concurrency-basics`, `performance-and-profiling-basics`, and `modularization-and-build-structure`.
- Learning Focus: Integrate reusable components, runtime measurements, and multi-step coordination into one cohesive capstone.

## Learning Outcomes

- `EXP-MEM-02`
- `EXP-CON-01`
- `EXP-PER-01`
- `EXP-MOD-01`

## Quick Run

Run the checkpoint checker from the repository root. The starter is intentionally incomplete, so the first run establishes the work still to do:

~~~bash
python scripts/automation.py check-checkpoint --language cpp --kind project --level 04-expert
~~~

## Requirements

- Represent processing steps as objects owned by `std::unique_ptr`.
- Process a list of jobs through all steps.
- Measure pipeline duration with `std::chrono`.
- Print per-step execution summary.

## Sample Output

```text
Running 3 jobs through 2 steps...
Step load processed 3 jobs
Step transform processed 3 jobs
Elapsed (microseconds): 42
```

## Cross-Language Notes

- This capstone is the canonical expert integration point for ownership, synchronization, timing, and multi-file structure.
- Other tracks keep the same learner goal but adapt the runtime model to their own concurrency and cleanup primitives.
- Use this project as the baseline when comparing how expert-level design changes across languages.

## What To Check

- every job passes through each step in the intended order
- per-step summary counts match the processed workload
- elapsed timing is reported and remains a positive measurement

## Check Your Work

Implement the task in `starter/`, then run from the repository root:

```bash
python scripts/automation.py check-checkpoint --language cpp --kind project --level 04-expert
```

Use `--solution` only after completing a full attempt. Each failed case reports targeted feedback without exposing the implementation.

## Extension Ideas

- Add optional logging levels.
- Add configurable step costs.

