# 04 Expert Capstone: Resource Pipeline Monitor

## Goal

Build a small pipeline simulator using RAII-style ownership and timing metrics.

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
