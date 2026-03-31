# Concurrency Basics (Python)

This module introduces thread-based coordination with locks and queues in Python.

## Learning Metadata

- Difficulty: Advanced.
- Estimated Time: 45-60 minutes.
- Prerequisites: `01-foundations/control-flow`, `03-advanced/structs-and-classes`.
- Cross-Language Lens: Compare `std::thread`, `Task`, goroutines, and Python threads as different concurrency building blocks.

## Quick Run

~~~bash
python example/main.py
~~~

## Topics Covered

- Starting worker threads.
- Waiting for workers with `join`.
- Protecting shared state with `threading.Lock`.
- Coordinating producer-consumer flow with `queue.Queue`.

## Common Pitfalls

- Assuming the GIL removes the need for coordination design.
- Updating shared state without a lock.
- Forgetting to join worker threads before reading final results.
- Leaving consumer threads blocked without a completion signal.

## Exercise Focus

- exercises/01.py: parallel chunk sum with worker threads.
- exercises/02.py: producer-consumer queue with `queue.Queue`.

### Exercise Specs

1. exercises/01.py
- Input: one line of integers, then worker count.
- Output: per-worker partial sums and final total.
- Edge cases: worker count larger than list size; non-positive worker count; empty list.

2. exercises/02.py
- Input: number of items to produce.
- Output: produced/consumed item logs and completion summary.
- Edge cases: zero items; consumer waiting on an empty queue.

## Checkpoint

- [ ] I can start threads and wait for them to finish safely.
- [ ] I can protect shared state with a lock.
- [ ] I can use a queue to coordinate a producer and consumer.
- [ ] I completed exercises/01.py.
- [ ] I completed exercises/02.py.
