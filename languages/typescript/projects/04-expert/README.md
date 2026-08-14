# 04 Expert Capstone: Async Resource Pipeline Monitor

## Goal

Build a small async pipeline that coordinates reusable steps, measures elapsed time, and closes its log resource explicitly.

## Learning Metadata

- Difficulty: Advanced.
- Estimated Time: 75-105 minutes.
- Prerequisites: All `04-expert` modules, especially `concurrency-basics`, `performance-and-profiling-basics`, and `modularization-and-build-structure`.
- Learning Focus: Integrate async coordination, explicit cleanup, timing, and modular object behavior into one cohesive TypeScript program.

## Learning Outcomes

- `EXP-MEM-02`
- `EXP-CON-01`
- `EXP-PER-01`
- `EXP-MOD-01`

## Quick Run

Run the reference solution from the repository root:

```bash
python scripts/automation.py check-checkpoint --language typescript --kind project --level 04-expert --solution
```

## Requirements

- Represent processing steps as reusable objects.
- Run several jobs through all steps asynchronously.
- Measure elapsed time with Node timing tools.
- Close the log resource explicitly even if work changes later.
- Print a per-step execution summary.

## Sample Output

```text
Running 3 jobs through 2 steps...
Step load processed 3 jobs
Step transform processed 3 jobs
Elapsed (ms): 12.34
Report closed: true
```

The step counts and the final closed-state line should stay exact. Only the measured time will vary.

## Cross-Language Notes

- Compared with the C++ capstone, this version translates the same expert goal into async coordination, explicit cleanup, and import-based structure.
- Relative to Go and C#, it trades true shared-memory threading for event-loop orchestration.
- The key comparison is how much of expert-level design survives even when the runtime primitives are completely different.

## What To Check

- every job passes through each step in the intended order
- per-step counts match the number of processed jobs
- elapsed timing is reported as a positive measurement
- the resource cleanup path runs before the program exits

## Check Your Work

Implement the task in `starter/`, then run from the repository root:

```bash
python scripts/automation.py check-checkpoint --language typescript --kind project --level 04-expert
```

Use `--solution` only after completing a full attempt. Each failed case reports targeted feedback without exposing the implementation.

## Extension Ideas

- Add configurable worker counts.
- Persist the audit log to disk.

