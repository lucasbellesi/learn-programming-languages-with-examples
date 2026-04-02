# Algorithms Basics (C#)

This module introduces common algorithmic patterns over collections.

## Learning Metadata

- Difficulty: Intermediate.
- Estimated Time: 30-45 minutes.
- Prerequisites: `01-foundations/arrays-and-vectors`, `01-foundations/functions`.
- Cross-Language Lens: Compare hand-written loops with library helpers and see when explicit iteration stays clearer for beginners.

## Quick Run

~~~bash
dotnet run --project example/algorithms-basics-example.csproj
~~~

## Topics Covered

- Linear search for the first matching index.
- Counting occurrences of a target value.
- One-pass minimum and maximum scanning.
- Combining multiple statistics in one traversal.

## Common Pitfalls

- Forgetting empty-collection checks before min/max logic.
- Using incorrect initial values for min/max.
- Repeating loops when a single pass can compute all metrics.

## Cross-Language Notes

- Compared with the C++ baseline, the same traversal and aggregation ideas are expressed with different defaults for loops, collections, and helper functions.
- Relative to Python, the statically typed tracks make intermediate state and accumulator types more explicit.
- The useful comparison is algorithm shape staying constant while the surrounding syntax and safety rails change.

## Exercise Focus

- exercises/01.cs: linear search and first index.
- exercises/02.cs: minimum, maximum, and even-count in one pass.

### Exercise Specs

1. exercises/01.cs
- Input: integer `n`, then `n` values, then a target.
- Output: first index of target or `-1`.
- Edge cases: `n <= 0`; target not present.

2. exercises/02.cs
- Input: integer `n`, then `n` values.
- Output: minimum, maximum, and even count.
- Edge cases: all odd numbers (even count `0`); all equal values.

## Checkpoint

- [ ] I can implement linear search confidently.
- [ ] I can compute multiple statistics in one pass.
- [ ] I can handle edge cases before indexing collections.
- [ ] I completed exercises/01.cs.
- [ ] I completed exercises/02.cs.
