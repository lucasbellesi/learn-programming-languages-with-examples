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

## Quick Run

```bash
python main.py
```

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

## What To Check

- Shared updates happen only while the lock is held.
- Each thread computes its own partial result before merging it.
- All threads finish before the final summary is printed.
