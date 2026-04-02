# 04 Expert Capstone: Resource Pipeline Monitor

## Goal

Build a small pipeline simulator using owned step objects and timing metrics.

## Learning Metadata

- Difficulty: Advanced.
- Estimated Time: 75-105 minutes.
- Prerequisites: All `04-expert` modules, especially `concurrency-basics`, `performance-and-profiling-basics`, and `modularization-and-build-structure`.
- Learning Focus: Integrate reusable components, runtime measurements, and multi-step coordination into one cohesive capstone.

## Quick Run

```bash
python main.py
```

## Requirements

- Represent processing steps as reusable objects.
- Process a list of jobs through all steps.
- Measure pipeline duration with `time.perf_counter`.
- Print per-step execution summary.

## Expected Output

```text
Running 3 jobs through 2 steps...
Step load processed 3 jobs
Step transform processed 3 jobs
Elapsed (microseconds): <positive integer>
```

The first three lines should stay exact. Only the measured microsecond value should vary.

## Cross-Language Notes

- Compared with the C++ capstone, this version emphasizes clarity of coordination and cleanup over raw systems-level control.
- Relative to C#, Go, and TypeScript, the runtime makes some mechanisms slower but keeps the learner goal readable.
- The right comparison here is how to preserve the same architecture when the runtime gives different performance and ownership tools.

## What To Check

- every job passes through each step in the intended order
- per-step summary counts match the processed workload
- elapsed timing is reported and remains a positive measurement

## Extension Ideas

- Add optional logging levels.
- Add configurable step costs.

