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

- work is split across multiple workers without inconsistent shared state
- partial results combine into a correct final summary
- ownership or resource-lifetime decisions are explicit and safe for the chosen language track
