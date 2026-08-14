# Assessment 04: Expert

## Goal

Practice ownership, thread-safe work distribution, and result aggregation.

## Task

Write a program that:

1. Uses `unique_ptr` to manage a shared data container.
2. Splits work across multiple threads.
3. Uses `mutex` to protect shared aggregation state.
4. Computes:
- total sum
- minimum value
- maximum value
5. Prints per-thread partial sums and final summary.

## Learning Metadata

- Difficulty: Advanced.
- Estimated Time: 45-60 minutes.
- Prerequisites: All `04-expert` modules, especially `memory-management-and-raii`, `smart-pointers-in-depth`, and `concurrency-basics`.
- Learning Focus: Prove you can coordinate work safely, choose the right ownership model for the track, and aggregate results under expert-level constraints.

## Learning Outcomes

- `EXP-MEM-02`
- `EXP-CON-01`
- `EXP-PER-01`
- `EXP-MOD-01`

## Quick Run

Run the checkpoint checker from the repository root. The starter is intentionally incomplete, so the first run establishes the work still to do:

~~~bash
python scripts/automation.py check-checkpoint --language cpp --kind assessment --level 04-expert
~~~

## Expected Output (shape)

```text
Worker 0 partial sum: ...
Worker 1 partial sum: ...
...
Final summary:
Total: ...
Minimum: ...
Maximum: ...
```

## Cross-Language Notes

- This is the canonical expert assessment for coordination, aggregation, and deterministic reasoning under concurrency pressure.
- Other tracks keep the same final outputs but adapt worker execution to their own runtime model.
- Compare how much explicit synchronization each language demands to reach the same summary.

## Check Your Work

Implement the task in `starter/`, then run from the repository root:

```bash
python scripts/automation.py check-checkpoint --language cpp --kind assessment --level 04-expert
```

Use `--solution` only after completing a full attempt. Each failed case reports targeted feedback without exposing the implementation.

## What To Check

- work is split across multiple workers without inconsistent shared state
- partial results combine into a correct final summary
- ownership or resource-lifetime decisions are explicit and safe for the chosen language track

