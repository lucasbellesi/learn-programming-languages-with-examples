# Concurrency Basics

This module introduces real multithreaded programming with `std::thread`.

## Quick Run

```bash
g++ -std=c++17 -Wall -Wextra -pedantic -pthread example/main.cpp -o concurrency_basics_example
./concurrency_basics_example
```

On Linux, `-pthread` is required for thread support.

## Topics Covered

- Creating and joining threads with `std::thread`.
- Protecting shared state with `std::mutex` and `std::lock_guard`.
- Coordinating producer/consumer workflows with `std::condition_variable`.
- Preventing race conditions in shared data updates.

## Common Pitfalls

- Reading/writing shared state without synchronization.
- Forgetting to join threads before program exit.
- Waiting on condition variables without a predicate.

## Exercise Focus

- `exercises/01.cpp`: parallel chunk sum with worker threads.
- `exercises/02.cpp`: producer-consumer queue with mutex and condition variable.

### Exercise Specs

1. `exercises/01.cpp`
- Input: list of integers and number of worker threads.
- Output: per-thread partial sums and final total.
- Edge cases: thread count larger than list size; non-positive thread count.

2. `exercises/02.cpp`
- Input: number of items to produce.
- Output: produced/consumed item logs and completion summary.
- Edge cases: zero items; consumer waiting while queue is empty.

## Checkpoint

- [ ] I can create and join worker threads safely.
- [ ] I can protect critical sections with a mutex.
- [ ] I can coordinate producers and consumers correctly.
- [ ] I completed both exercises.
