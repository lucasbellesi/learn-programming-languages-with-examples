# 04 Expert Capstone: Resource Pipeline Monitor

## Goal

Build a small pipeline simulator using RAII-style ownership and timing metrics.

## Learning Metadata

- Difficulty: Advanced.
- Estimated Time: 75-105 minutes.
- Prerequisites: All `04-expert` modules, especially `concurrency-basics`, `performance-and-profiling-basics`, and `modularization-and-build-structure`.
- Learning Focus: Integrate reusable components, runtime measurements, and multi-step coordination into one cohesive capstone.

## Quick Run

```bash
g++ -std=c++17 -Wall -Wextra -pedantic -pthread main.cpp -o expert_capstone
./expert_capstone
```

## Requirements

- Represent processing steps as objects owned by `std::unique_ptr`.
- Process a list of jobs through all steps.
- Measure pipeline duration with `std::chrono`.
- Print per-step execution summary.

## Sample Output

```text
Running 3 jobs through 2 steps...
Step load processed 3 jobs
Step transform processed 3 jobs
Elapsed (microseconds): 42
```

## Cross-Language Notes

- This capstone is the canonical expert integration point for ownership, synchronization, timing, and multi-file structure.
- Other tracks keep the same learner goal but adapt the runtime model to their own concurrency and cleanup primitives.
- Use this project as the baseline when comparing how expert-level design changes across languages.

## What To Check

- every job passes through each step in the intended order
- per-step summary counts match the processed workload
- elapsed timing is reported and remains a positive measurement

## Extension Ideas

- Add optional logging levels.
- Add configurable step costs.

