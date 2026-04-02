# Algorithms Basics

This module introduces common algorithmic patterns over vectors.

## Learning Metadata

- Difficulty: Intermediate.
- Estimated Time: 30-45 minutes.
- Prerequisites: `01-foundations/arrays-and-vectors`, `01-foundations/functions`.
- Cross-Language Lens: Compare hand-written loops with library helpers and see when explicit iteration stays clearer for beginners.

## Quick Run

```bash
g++ -std=c++17 -Wall -Wextra -pedantic example/main.cpp -o algorithms_basics_example
./algorithms_basics_example
```

## More Examples

- `example/main.cpp` is the primary runnable sample for this module.
- Try one variation: copy it to `example/variation.cpp`, change one rule, and compare outputs.

## Topics Covered

- Linear search.
- Counting matches.
- One-pass minimum/maximum scanning.
- Early loop exit for performance.

## Common Pitfalls

- Forgetting to handle empty input.
- Initializing min/max incorrectly.
- Running multiple passes when one pass is enough.

## Cross-Language Notes

- Compared with the C++ baseline, the same traversal and aggregation ideas are expressed with different defaults for loops, collections, and helper functions.
- Relative to Python, the statically typed tracks make intermediate state and accumulator types more explicit.
- The useful comparison is algorithm shape staying constant while the surrounding syntax and safety rails change.

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
