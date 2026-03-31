# Assessment 04: Expert

## Goal

Practice shared-data coordination, concurrent work distribution, and thread-safe aggregation.

## Task

Write a program that:

1. Keeps the assessment data in one shared container.
2. Splits work across multiple threads.
3. Uses a `Lock` to protect shared aggregation state.
4. Computes:
- total sum
- minimum value
- maximum value
5. Prints per-worker partial sums and final summary.

## Learning Metadata

- Difficulty: Expert Assessment.
- Estimated Time: 45-60 minutes.
- Prerequisites: `04-expert/concurrency-basics`, `04-expert/memory-management-and-raii`, `04-expert/smart-pointers-in-depth`.
- Learning Focus: prove you can coordinate concurrent workers, protect shared aggregation, and reason about ownership boundaries without step-by-step scaffolding.
## Quick Run

```bash
python main.py
```

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

## What To Check

- Shared updates happen only while the lock is held.
- Each thread computes its own partial result before merging it.
- All threads finish before the final summary is printed.
