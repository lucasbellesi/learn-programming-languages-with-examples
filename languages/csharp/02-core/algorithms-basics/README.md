# Algorithms Basics (C#)

This module introduces common algorithmic patterns over collections.

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
