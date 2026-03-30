# Concurrency Basics (C#)

This module introduces safe multithreaded coordination with tasks, locks, and monitor signaling.

## Quick Run

~~~bash
dotnet run --project example/concurrency-basics-example.csproj
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

## Checkpoint

- [ ] I can start concurrent workers and wait for all of them to finish.
- [ ] I can explain why `lock` is needed around shared state.
- [ ] I can coordinate a producer and consumer with monitor signaling.
- [ ] I completed exercises/01.cs.
- [ ] I completed exercises/02.cs.
