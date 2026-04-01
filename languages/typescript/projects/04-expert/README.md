# 04 Expert Capstone: Async Resource Pipeline Monitor

## Goal

Build a small async pipeline that coordinates reusable steps, measures elapsed time, and closes its log resource explicitly.

## Learning Metadata

- Difficulty: Advanced.
- Estimated Time: 75-105 minutes.
- Prerequisites: All `04-expert` modules, especially `concurrency-basics`, `performance-and-profiling-basics`, and `modularization-and-build-structure`.
- Learning Focus: Integrate async coordination, explicit cleanup, timing, and modular object behavior into one cohesive TypeScript program.

## Quick Run

~~~bash
npm run build:typescript
node build/typescript/projects/04-expert/main.js
~~~

## Requirements

- Represent processing steps as reusable objects.
- Run several jobs through all steps asynchronously.
- Measure elapsed time with Node timing tools.
- Close the log resource explicitly even if work changes later.
- Print a per-step execution summary.

## Sample Output

```text
Running 3 jobs through 2 steps...
Step load processed 3 jobs
Step transform processed 3 jobs
Elapsed (ms): 12.34
Report closed: true
```

The step counts and the final closed-state line should stay exact. Only the measured time will vary.

## What To Check

- every job passes through each step in the intended order
- per-step counts match the number of processed jobs
- elapsed timing is reported as a positive measurement
- the resource cleanup path runs before the program exits

## Extension Ideas

- Add configurable worker counts.
- Persist the audit log to disk.
