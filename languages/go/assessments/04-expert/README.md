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

## Quick Run

```bash
go run main.go
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

- Shared updates happen only while the mutex is held.
- Each goroutine computes its own partial result before merging it.
- The final summary is printed only after all goroutines finish.
