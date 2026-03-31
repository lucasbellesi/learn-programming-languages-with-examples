# Performance and Profiling Basics

This module introduces simple measurement and optimization patterns.

## Learning Metadata

- Difficulty: Expert.
- Estimated Time: 35-50 minutes.
- Prerequisites: `02-core/algorithms-basics`, `01-foundations/arrays-and-vectors`.
- Cross-Language Lens: Compare timing APIs, allocation behavior, and why micro-benchmarks can mislead in different runtimes.
## Quick Run

```bash
g++ -std=c++17 -Wall -Wextra -pedantic example/main.cpp -o performance_profiling_example
./performance_profiling_example
```

## More Examples

- `example/main.cpp` is the primary runnable sample for this module.
- Try one variation: copy it to `example/variation.cpp`, change one rule, and compare outputs.

## Topics Covered

- Measuring elapsed time with `std::chrono`.
- Comparing two algorithm choices.
- Avoiding premature optimization.
- Data structure and allocation effects.

## Common Pitfalls

- Timing too-small workloads.
- Drawing conclusions from one run.
- Ignoring algorithmic complexity.

## Exercise Focus

- `exercises/01.cpp`: compare pass-by-value vs const-reference.
- `exercises/02.cpp`: compare vector push with/without reserve.

### Exercise Specs

1. `exercises/01.cpp`
- Input: vector size.
- Output: timing for value vs reference calls.
- Edge cases: small size (noisy timings); larger size.

2. `exercises/02.cpp`
- Input: element count.
- Output: timing for push_back with and without reserve.
- Edge cases: zero count; large count.

## Checkpoint

- [ ] I can measure code sections with `std::chrono`.
- [ ] I can compare two implementations fairly.
- [ ] I can justify simple optimization choices.
- [ ] I completed both exercises.
