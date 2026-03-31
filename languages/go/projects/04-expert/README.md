# 04 Expert Capstone: Resource Pipeline Monitor

## Goal

Build a small pipeline simulator using owned step objects and timing metrics.

## Learning Metadata

- Difficulty: Expert Capstone.
- Estimated Time: 60-90 minutes.
- Prerequisites: all `04-expert` modules, especially `concurrency-basics` and `performance-and-profiling-basics`.
- Learning Focus: integrate reusable step objects, pipeline orchestration, and timing into one cohesive program.
## Quick Run

```bash
go run main.go
```

## Requirements

- Represent processing steps as reusable objects.
- Process a list of jobs through all steps.
- Measure pipeline duration with `time`.
- Print per-step execution summary.

## Expected Output

```text
Running 3 jobs through 2 steps...
Step load processed 3 jobs
Step transform processed 3 jobs
Elapsed (microseconds): <positive integer>
```

The first three lines should stay exact. Only the measured microsecond value should vary.

## Extension Ideas

- Add optional logging levels.
- Add configurable step costs.
