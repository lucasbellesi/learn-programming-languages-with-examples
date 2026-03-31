# Assessment 04: Expert

## Goal

Practice shared-data coordination, concurrent work distribution, and thread-safe aggregation.

## Task

Write a program that:

1. Keeps the assessment data in one owned container.
2. Splits work across multiple tasks.
3. Uses `lock` to protect shared aggregation state.
4. Computes:
- total sum
- minimum value
- maximum value
5. Prints per-worker partial sums and final summary.

## Quick Run

```bash
dotnet run --project assessment-04-expert.csproj
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

- Shared updates happen only inside the `lock`.
- Each worker computes its own partial result before merging it.
- All tasks finish before the final summary is printed.
