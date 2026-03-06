# Concurrency Basics

This module introduces concurrency concepts: interleaving, shared-state hazards, and synchronization intent.

## Quick Run

```bash
g++ -std=c++17 -Wall -Wextra -pedantic example/main.cpp -o concurrency_basics_example
./concurrency_basics_example
```

## Topics Covered

- Task interleaving concept.
- Race condition intuition.
- Critical section idea.
- Why mutexes/atomics are needed in real multithreaded code.

## Common Pitfalls

- Assuming shared updates are always safe.
- Treating read-modify-write as atomic when it is not.
- Ignoring ordering effects between operations.

## Exercise Focus

- `exercises/01.cpp`: simulate parallel chunk sum with interleaved steps.
- `exercises/02.cpp`: producer-consumer simulation with queue operations.

### Exercise Specs

1. `exercises/01.cpp`
- Input: list of integers and chunk size.
- Output: partial sums and final sum.
- Edge cases: chunk size larger than list; empty list.

2. `exercises/02.cpp`
- Input: sequence of produce/consume commands.
- Output: queue state transitions.
- Edge cases: consume on empty queue; multiple produce before consume.

## Checkpoint

- [ ] I can explain race conditions with examples.
- [ ] I can identify critical sections in shared-state workflows.
- [ ] I understand why synchronization primitives are required in real threads.
- [ ] I completed both exercises.
