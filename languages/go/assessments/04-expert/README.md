# Assessment 04: Expert

## Goal

Practice shared-data coordination, concurrent work distribution, and thread-safe aggregation.

## Task

Write a program that:

1. Keeps the assessment data in one shared container.
2. Splits work across multiple goroutines.
3. Uses `sync.Mutex` to protect shared aggregation state.
4. Computes:
- total sum
- minimum value
- maximum value
5. Prints per-worker partial sums and final summary.

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
python scripts/automation.py check-checkpoint --language go --kind assessment --level 04-expert
~~~

## Expected Output

```text
Worker 0 partial sum: 48
Worker 1 partial sum: 97
Worker 2 partial sum: 60

Final summary:
Total: 205
Minimum: 2
Maximum: 45
```

The worker lines may appear in a different order, but the three partial sums and the final totals should match these values.

## Cross-Language Notes

- Compared with the C++ assessment, this version can express worker coordination with less ceremony and a different balance between communication and locking.
- Relative to Python and TypeScript, the runtime makes concurrent execution feel more direct and less simulated.
- The useful cross-language question is how much synchronization detail the learner must write explicitly.

## Check Your Work

Implement the task in `starter/`, then run from the repository root:

```bash
python scripts/automation.py check-checkpoint --language go --kind assessment --level 04-expert
```

Use `--solution` only after completing a full attempt. Each failed case reports targeted feedback without exposing the implementation.

## What To Check

- work is split across multiple workers without inconsistent shared state
- partial results combine into a correct final summary
- ownership or resource-lifetime decisions are explicit and safe for the chosen language track

