# Algorithms Basics (C#)

This module introduces common algorithmic patterns over collections.

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
python scripts/automation.py run-module --module-path languages/csharp/02-core/algorithms-basics
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

- In C#, read this module through the native focus ?Algorithms Basics?; the shared folder name remains stable for side-by-side navigation.
- Use static types, .NET collections, and managed-resource patterns to demonstrate how to implement linear scans and accumulations with clear invariants.
- Compare observable behavior with the other tracks when learning to analyze behavior for empty, duplicate, and missing values; equivalent evidence matters more than identical syntax.

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

## Check Your Work

Run from the repository root after implementing a starter:

```bash
python scripts/automation.py check-exercise --language csharp --level 02-core --module algorithms-basics --exercise 01
```

Change `--exercise 01` to `--exercise 02` for the second task. Consult `exercises/solutions/` only after making a complete attempt.

## Checkpoint

- [ ] I can implement linear search confidently.
- [ ] I can compute multiple statistics in one pass.
- [ ] I can handle edge cases before indexing collections.
- [ ] I completed exercises/01.cs.
- [ ] I completed exercises/02.cs.
