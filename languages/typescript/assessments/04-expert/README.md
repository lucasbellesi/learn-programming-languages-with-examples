# Assessment 04: Expert

## Goal

Practice async work splitting, stable aggregation, and explicit summary reporting in TypeScript.

## Task

Write a program that:

1. Keeps the assessment data in one shared array.
2. Splits the data into several async worker jobs.
3. Computes per-worker partial sums.
4. Aggregates:
- total sum
- minimum value
- maximum value
5. Prints partial results and a final summary.

## Learning Metadata

- Difficulty: Advanced.
- Estimated Time: 45-60 minutes.
- Prerequisites: All `04-expert` modules, especially `smart-pointers-in-depth`, `concurrency-basics`, and `performance-and-profiling-basics`.
- Learning Focus: Prove you can structure async work clearly, return partial summaries safely, and combine them into deterministic final output.

## Quick Run

~~~bash
npm run build:typescript
node build/typescript/assessments/04-expert/main.js
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

## Cross-Language Notes

- Compared with the C++ assessment, this version turns worker coordination into async job orchestration instead of shared-memory threading.
- Relative to Go, C#, and Python, deterministic output order matters more because completion order can differ under the event loop.
- The core comparison is stable aggregation logic across radically different concurrency primitives.

## What To Check

- worker jobs return correct partial summaries
- final totals come from the returned worker data, not hardcoded output
- the final report stays deterministic even though work is scheduled asynchronously

