# Concurrency Basics (C#)

This module introduces safe multithreaded coordination with tasks, locks, and monitor signaling.

## Learning Metadata

- Difficulty: Advanced.
- Estimated Time: 45-60 minutes.
- Prerequisites: `01-foundations/control-flow`, `03-advanced/structs-and-classes`.
- Cross-Language Lens: Compare `std::thread`, `Task`, goroutines, and Python threads as different concurrency building blocks.

## Learning Outcomes

- `EXP-CON-01`: Coordinate concurrent work without data races or lost results.
- `EXP-CON-02`: Define completion, cancellation, and error propagation behavior.

## Quick Run

Run from the repository root:

~~~bash
python scripts/automation.py run-module --module-path languages/csharp/04-expert/concurrency-basics
~~~

## Topics Covered

- Starting concurrent work with `Task.Run`.
- Waiting for workers to finish with `Task.WaitAll`.
- Protecting shared state with `lock`.
- Coordinating producer-consumer flow with `Monitor.Wait` and `Monitor.PulseAll`.

## Common Pitfalls

- Updating shared state without synchronization.
- Capturing changing loop variables incorrectly in worker lambdas.
- Waiting on a monitor without re-checking the queue condition.
- Forgetting to notify waiting consumers when production is complete.

## Cross-Language Notes

- C# keeps real multithreading, but the comparison with C++ shifts from raw threads toward `Task`, `lock`, and runtime-managed coordination.
- Compared with Go and TypeScript, this track still shares the thread-based mental model more directly.
- The useful cross-language question is which runtime gives you the strongest safety default for concurrent work.

## Exercise Focus

- exercises/01.cs: parallel chunk sum with worker tasks.
- exercises/02.cs: producer-consumer queue with `Monitor`.

### Exercise Specs

1. exercises/01.cs
- Input: one line of integers, then worker count.
- Output: per-worker partial sums and final total.
- Edge cases: worker count larger than list size; non-positive worker count; empty list.

2. exercises/02.cs
- Input: number of items to produce.
- Output: produced/consumed item logs and completion summary.
- Edge cases: zero items; consumer waiting while queue is empty.

## Check Your Work

Run from the repository root after implementing a starter:

```bash
python scripts/automation.py check-exercise --language csharp --level 04-expert --module concurrency-basics --exercise 01
```

Change `--exercise 01` to `--exercise 02` for the second task. Consult `exercises/solutions/` only after making a complete attempt.

## Checkpoint

- [ ] I can start concurrent workers and wait for all of them to finish.
- [ ] I can explain why `lock` is needed around shared state.
- [ ] I can coordinate a producer and consumer with monitor signaling.
- [ ] I completed exercises/01.cs.
- [ ] I completed exercises/02.cs.

