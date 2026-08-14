# 04 Expert Capstone: Resource Pipeline Monitor

## Goal

Build a small pipeline simulator using ownership-aware steps and timing metrics.

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

Run the reference solution from the repository root:

```bash
python scripts/automation.py check-checkpoint --language csharp --kind project --level 04-expert --solution
```

## Requirements

- Represent processing steps as reusable objects.
- Process a list of jobs through all steps.
- Measure pipeline duration with `Stopwatch`.
- Print per-step execution summary.

## Expected Output

```text
Running 3 jobs through 2 steps...
Step load processed 3 jobs
Step transform processed 3 jobs
Elapsed (microseconds): <positive integer>
```

The first three lines should stay exact. Only the measured microsecond value should vary.

## Cross-Language Notes

- Compared with the C++ capstone, this version keeps the same systems mindset while leaning on `Task`, `Stopwatch`, and managed cleanup patterns.
- Relative to Go and TypeScript, it still feels structurally close to the thread-and-object model of the canonical track.
- The useful comparison is how much runtime support reduces incidental complexity without changing the learner goal.

## What To Check

- every job passes through each step in the intended order
- per-step summary counts match the processed workload
- elapsed timing is reported and remains a positive measurement

## Check Your Work

Implement the task in `starter/`, then run from the repository root:

```bash
python scripts/automation.py check-checkpoint --language csharp --kind project --level 04-expert
```

Use `--solution` only after completing a full attempt. Each failed case reports targeted feedback without exposing the implementation.

## Extension Ideas

- Add optional logging levels.
- Add configurable step costs.

