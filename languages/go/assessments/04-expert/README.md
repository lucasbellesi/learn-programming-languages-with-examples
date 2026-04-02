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

## Quick Run

```bash
go run main.go
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

## Cross-Language Notes

- Compared with the C++ assessment, this version can express worker coordination with less ceremony and a different balance between communication and locking.
- Relative to Python and TypeScript, the runtime makes concurrent execution feel more direct and less simulated.
- The useful cross-language question is how much synchronization detail the learner must write explicitly.

## What To Check

- work is split across multiple workers without inconsistent shared state
- partial results combine into a correct final summary
- ownership or resource-lifetime decisions are explicit and safe for the chosen language track

