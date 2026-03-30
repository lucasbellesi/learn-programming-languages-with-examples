# 04 Expert Capstone: Resource Pipeline Monitor

## Goal

Build a small pipeline simulator using owned step objects and timing metrics.

## Quick Run

```bash
python main.py
```

## Requirements

- Represent processing steps as reusable objects.
- Process a list of jobs through all steps.
- Measure pipeline duration with `time.perf_counter`.
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
