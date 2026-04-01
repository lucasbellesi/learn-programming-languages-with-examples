# Performance and Profiling Basics

This module introduces basic measurement and comparison tools in TypeScript using Node's timing APIs.

## Learning Metadata

- Difficulty: Advanced.
- Estimated Time: 45-60 minutes.
- Prerequisites: `02-core/algorithms-basics`, `02-core/maps-and-frequency-counting`, and `03-advanced/copy-and-move-semantics`.
- Cross-Language Lens: Compare Node timing tools and allocation costs with native profilers and lower-level memory behavior in other tracks.

## Quick Run

~~~bash
npm run build:typescript
node build/typescript/04-expert/performance-and-profiling-basics/example/main.js
~~~

## Topics Covered

- Measuring elapsed time with `performance.now`.
- Warming up before comparing implementations.
- Averaging multiple runs instead of trusting one sample.
- Comparing allocation-heavy and allocation-light approaches.

## Common Pitfalls

- Measuring tiny workloads where noise dominates the result.
- Timing setup work instead of the target operation.
- Drawing conclusions from a single run.
- Optimizing before checking algorithmic cost first.

## Exercise Focus

- exercises/01.ts: compare repeated array scans with `Map` lookups.
- exercises/02.ts: compare string concatenation with buffered joins.

### Exercise Specs

1. exercises/01.ts
- Input: none.
- Output: average milliseconds for scan-based and map-based lookups.
- Edge cases: very small data sizes may hide the expected difference.

2. exercises/02.ts
- Input: none.
- Output: average milliseconds for both string-building approaches.
- Edge cases: workloads too small to show a meaningful difference.

## Checkpoint

- [ ] I can measure TypeScript code with `performance.now`.
- [ ] I can average multiple runs before comparing implementations.
- [ ] I can explain how allocation patterns affect runtime.
- [ ] I completed exercises/01.ts.
- [ ] I completed exercises/02.ts.
