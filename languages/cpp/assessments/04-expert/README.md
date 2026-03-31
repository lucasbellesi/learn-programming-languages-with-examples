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

- Difficulty: Expert Assessment.
- Estimated Time: 45-60 minutes.
- Prerequisites: `04-expert/concurrency-basics`, `04-expert/memory-management-and-raii`, `04-expert/smart-pointers-in-depth`.
- Learning Focus: prove you can coordinate concurrent workers, protect shared aggregation, and reason about ownership boundaries without step-by-step scaffolding.
## Quick Run

```bash
g++ -std=c++17 -Wall -Wextra -pedantic -pthread main.cpp -o assessment_04_expert
./assessment_04_expert
```

On Linux, `-pthread` is required for thread support.

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

- No data races (shared updates protected by `mutex`).
- Ownership is explicit (`unique_ptr`).
- Threads are always joined before program exit.
