# Algorithms Basics (Go)

This module introduces common algorithmic patterns over slices.

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
python scripts/automation.py run-module --module-path languages/go/02-core/algorithms-basics
~~~

## Topics Covered

- Linear search for the first matching index.
- Counting occurrences of a target value.
- One-pass minimum and maximum scanning.
- Combining multiple statistics in one traversal.

## Common Pitfalls

- Ignoring empty-slice checks before min/max logic.
- Initializing min/max with invalid defaults.
- Running extra loops when a single pass is enough.

## Cross-Language Notes

- In Go, read this module through the native focus ?Algorithms Basics?; the shared folder name remains stable for side-by-side navigation.
- Use explicit errors, slices/maps, interfaces, and defer to demonstrate how to implement linear scans and accumulations with clear invariants.
- Compare observable behavior with the other tracks when learning to analyze behavior for empty, duplicate, and missing values; equivalent evidence matters more than identical syntax.

## Exercise Focus

- exercises/01.go: linear search and first index.
- exercises/02.go: minimum, maximum, and even-count in one pass.

### Exercise Specs

1. exercises/01.go
- Input: integer `n`, then `n` values, then a target.
- Output: first index of target or `-1`.
- Edge cases: `n <= 0`; target not present.

2. exercises/02.go
- Input: integer `n`, then `n` values.
- Output: minimum, maximum, and even count.
- Edge cases: all odd numbers (even count `0`); all equal values.

## Check Your Work

Run from the repository root after implementing a starter:

```bash
python scripts/automation.py check-exercise --language go --level 02-core --module algorithms-basics --exercise 01
```

Change `--exercise 01` to `--exercise 02` for the second task. Consult `exercises/solutions/` only after making a complete attempt.

## Checkpoint

- [ ] I can implement linear search confidently.
- [ ] I can compute multiple statistics in one pass.
- [ ] I can handle empty and boundary cases safely.
- [ ] I completed exercises/01.go.
- [ ] I completed exercises/02.go.
