# 04 Expert Capstone: Resource Pipeline Monitor

## Goal

Build a concurrent pipeline simulator with explicit resource ownership, deterministic executor cleanup, timing metrics, and focused source boundaries.

## Learning Metadata

- Difficulty: Advanced.
- Estimated Time: 75-105 minutes.
- Prerequisites: All `04-expert` modules, especially `concurrency-basics`, `performance-and-profiling-basics`, and `modularization-and-build-structure`.
- Learning Focus: Integrate reusable components, runtime measurements, concurrent coordination, and deterministic cleanup into one cohesive Java capstone.

## Learning Outcomes

- `EXP-MEM-02`
- `EXP-CON-01`
- `EXP-PER-01`
- `EXP-MOD-01`

## Quick Run

Run the checkpoint checker from the repository root. The starter is intentionally incomplete, so the first run establishes the work still to do:

~~~bash
python scripts/automation.py check-checkpoint --language java --kind project --level 04-expert
~~~

## Requirements

- Represent jobs and processing steps as validated domain objects.
- Process jobs concurrently while preserving step order within each job.
- Keep shared step counters thread-safe.
- Own the executor through an `AutoCloseable` pipeline and close it predictably.
- Measure pipeline duration with `System.nanoTime`.
- Separate orchestration, processing, and report data across source files.

## Expected Output

```text
Running 3 jobs through 2 steps...
Step load processed 3 jobs
Step transform processed 3 jobs
Every job completed every step: true
Executor terminated: true
Elapsed (microseconds): <positive integer>
```

Only the measured microsecond value should vary.

## Cross-Language Notes

- Compared with C++, Java uses garbage-collected references but still needs explicit executor shutdown and thread-safe counters.
- Relative to C#, Java uses `ExecutorService`, futures, and `System.nanoTime` in place of tasks and `Stopwatch`.
- The multi-file source set makes the build boundary visible without introducing Maven or Gradle yet.

## What To Check

- every job passes through each step in the intended order
- per-step summary counts match the processed workload under concurrent execution
- the executor is terminated after the `try-with-resources` scope
- elapsed timing is reported as a positive measurement

## Check Your Work

Implement the task in `starter/`, then run from the repository root:

```bash
python scripts/automation.py check-checkpoint --language java --kind project --level 04-expert
```

Use `--solution` only after completing a full attempt. Each failed case reports targeted feedback without exposing the implementation.

## Extension Ideas

- Add configurable worker and step counts.
- Attach an immutable processing result to each job.
- Move the source set into named packages and a Maven or Gradle project.
