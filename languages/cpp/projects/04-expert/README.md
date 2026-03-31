# 04 Expert Capstone: Resource Pipeline Monitor

## Goal

Build a small pipeline simulator using RAII-style ownership and timing metrics.

## Learning Metadata

- Difficulty: Expert Capstone.
- Estimated Time: 60-90 minutes.
- Prerequisites: all `04-expert` modules, especially `concurrency-basics` and `performance-and-profiling-basics`.
- Learning Focus: integrate reusable step objects, pipeline orchestration, and timing into one cohesive program.
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

## Extension Ideas

- Add optional logging levels.
- Add configurable step costs.
