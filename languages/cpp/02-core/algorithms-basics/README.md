# Algorithms Basics

This module introduces common algorithmic patterns over vectors.

## Learning Metadata

- Difficulty: Intermediate.
- Estimated Time: 30-45 minutes.
- Prerequisites: `01-foundations/arrays-and-vectors`, `01-foundations/functions`.
- Cross-Language Lens: Compare hand-written loops with library helpers and see when explicit iteration stays clearer for beginners.

## Learning Outcomes

- `COR-ALG-01`: Implement linear scans and accumulations with clear invariants.
- `COR-ALG-02`: Analyze behavior for empty, duplicate, and missing values.

## Quick Run

Run from the repository root:

~~~bash
python scripts/automation.py run-module --module-path languages/cpp/02-core/algorithms-basics
~~~

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

- In C++, read this module through the native focus ?Algorithms Basics?; the shared folder name remains stable for side-by-side navigation.
- Use explicit value/reference semantics and standard-library types to demonstrate how to implement linear scans and accumulations with clear invariants.
- Compare observable behavior with the other tracks when learning to analyze behavior for empty, duplicate, and missing values; equivalent evidence matters more than identical syntax.

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

## Check Your Work

Run from the repository root after implementing a starter:

```bash
python scripts/automation.py check-exercise --language cpp --level 02-core --module algorithms-basics --exercise 01
```

Change `--exercise 01` to `--exercise 02` for the second task. Consult `exercises/solutions/` only after making a complete attempt.

## Checkpoint

- [ ] I can apply linear search confidently.
- [ ] I can combine multiple statistics in a single loop.
- [ ] I can reason about algorithm edge cases.
- [ ] I completed both exercises.
