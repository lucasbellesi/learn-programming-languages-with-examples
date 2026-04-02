# Concurrency Basics (Go)

This module introduces goroutines, mutexes, and channels for safe concurrent coordination.

## Learning Metadata

- Difficulty: Advanced.
- Estimated Time: 45-60 minutes.
- Prerequisites: `01-foundations/control-flow`, `03-advanced/structs-and-classes`.
- Cross-Language Lens: Compare `std::thread`, `Task`, goroutines, and Python threads as different concurrency building blocks.

## Quick Run

~~~bash
go run example/main.go
~~~

## Topics Covered

- Launching work with goroutines.
- Waiting for workers with `sync.WaitGroup`.
- Protecting shared state with `sync.Mutex`.
- Coordinating producer-consumer flow with channels.

## Common Pitfalls

- Accessing shared state without a mutex.
- Forgetting to wait for worker goroutines.
- Sending on a channel after it has been closed.
- Assuming channel order solves every synchronization problem.

## Cross-Language Notes

- Go reframes concurrency around goroutines and communication-friendly patterns rather than C++-style thread management.
- Compared with C#, Python, and TypeScript, it usually takes less ceremony to launch overlapping work.
- The key comparison is lightweight task structure versus explicit locking discipline.

## Exercise Focus

- exercises/01.go: parallel chunk sum with worker goroutines.
- exercises/02.go: producer-consumer queue with channels.

### Exercise Specs

1. exercises/01.go
- Input: one line of integers, then worker count.
- Output: per-worker partial sums and final total.
- Edge cases: worker count larger than list size; non-positive worker count; empty list.

2. exercises/02.go
- Input: number of items to produce.
- Output: produced/consumed item logs and completion summary.
- Edge cases: zero items; consumer waiting on an empty queue.

## Checkpoint

- [ ] I can start goroutines and wait for them safely.
- [ ] I can protect shared state with a mutex.
- [ ] I can use channels to coordinate producers and consumers.
- [ ] I completed exercises/01.go.
- [ ] I completed exercises/02.go.

