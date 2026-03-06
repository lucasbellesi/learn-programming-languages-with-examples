# Algorithms Basics

This module introduces common algorithmic patterns over vectors.

## Quick Run

```bash
g++ -std=c++17 -Wall -Wextra -pedantic example/main.cpp -o algorithms_basics_example
./algorithms_basics_example
```

## Topics Covered

- Linear search.
- Counting matches.
- One-pass minimum/maximum scanning.
- Early loop exit for performance.

## Common Pitfalls

- Forgetting to handle empty input.
- Initializing min/max incorrectly.
- Running multiple passes when one pass is enough.

## Exercise Focus

- `exercises/01.cpp`: linear search and first index.
- `exercises/02.cpp`: min, max, and even-count in one pass.

### Exercise Specs

1. `exercises/01.cpp`
- Input: integer `n`, then `n` values, then target.
- Output: first index of target or `-1`.
- Edge cases: `n <= 0`; target not present.

2. `exercises/02.cpp`
- Input: integer `n`, then `n` values.
- Output: minimum, maximum, and even count.
- Edge cases: all odd numbers (even count `0`); all equal values.

## Checkpoint

- [ ] I can apply linear search confidently.
- [ ] I can combine multiple statistics in a single loop.
- [ ] I can reason about algorithm edge cases.
- [ ] I completed both exercises.
