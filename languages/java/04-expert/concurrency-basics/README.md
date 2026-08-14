# Concurrency Basics (Java)

This module introduces safe multithreaded coordination with executors, futures, synchronization, and blocking queues.

## Learning Metadata

- Difficulty: Advanced.
- Estimated Time: 45-60 minutes.
- Prerequisites: `01-foundations/control-flow`, `03-advanced/structs-and-classes`.
- Cross-Language Lens: Compare Java executors and futures with `std::thread`, C# tasks, goroutines, Python threads, and TypeScript promises.

## Learning Outcomes

- `EXP-CON-01`: Coordinate concurrent work without data races or lost results.
- `EXP-CON-02`: Define completion, cancellation, and error propagation behavior.

## Quick Run

Run from the repository root:

~~~bash
python scripts/automation.py run-module --module-path languages/java/04-expert/concurrency-basics
~~~

## Topics Covered

- Running bounded worker pools with `ExecutorService`.
- Collecting deterministic results through `Future` values.
- Protecting shared mutable state with `synchronized`.
- Coordinating producers and consumers with `BlockingQueue`.
- Shutting executors down predictably.

## Common Pitfalls

- Updating shared state without synchronization.
- Printing from workers and expecting a deterministic order.
- Blocking forever because a consumer never receives a completion signal.
- Forgetting to shut down an executor.
- Assuming more threads always make CPU-bound work faster.

## Cross-Language Notes

- Java separates task submission from thread management through executors.
- Compared with raw C++ threads, `Future` and `BlockingQueue` provide higher-level coordination boundaries.
- Compared with TypeScript promises, Java workers can execute CPU-bound tasks in parallel on multiple threads.
- The learner goal is to return results from workers and keep shared mutation small and explicit.

## Exercise Focus

- exercises/Exercise01.java: parallel chunk sum with a fixed worker pool.
- exercises/Exercise02.java: producer-consumer flow with a blocking queue and completion marker.

### Exercise Specs

1. exercises/Exercise01.java
- Input: integer count, values, and requested worker count.
- Output: ordered partial sums and final total.
- Edge cases: non-positive counts; worker count larger than the value count.

2. exercises/Exercise02.java
- Input: number of items to produce.
- Output: produced/consumed logs and completion summary.
- Edge cases: zero items; negative item count.

## Check Your Work

Run from the repository root after implementing a starter:

```bash
python scripts/automation.py check-exercise --language java --level 04-expert --module concurrency-basics --exercise 01
```

Change `--exercise 01` to `--exercise 02` for the second task. Consult `exercises/solutions/` only after making a complete attempt.

## Checkpoint

- [ ] I can submit tasks to an executor and collect their results.
- [ ] I can explain when shared state needs synchronization.
- [ ] I can coordinate a producer and consumer with a blocking queue.
- [ ] I can shut an executor down reliably.
- [ ] I completed exercises/Exercise01.java.
- [ ] I completed exercises/Exercise02.java.
