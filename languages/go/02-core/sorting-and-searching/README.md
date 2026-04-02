# Sorting and Searching (Go)

This module introduces basic sorting and searching techniques.

## Learning Metadata

- Difficulty: Intermediate.
- Estimated Time: 30-45 minutes.
- Prerequisites: `02-core/algorithms-basics`, `01-foundations/arrays-and-vectors`.
- Cross-Language Lens: Compare built-in sort and search helpers and the stability guarantees each standard library makes.

## Quick Run

~~~bash
go run example/main.go
~~~

## Topics Covered

- Sorting integer slices in ascending order.
- Implementing binary search with index boundaries.
- Understanding search preconditions for sorted data.
- Comparing linear and logarithmic search costs.

## Common Pitfalls

- Applying binary search to unsorted values.
- Incorrect midpoint or boundary updates.
- Forgetting to return `-1` when target is absent.

## Cross-Language Notes

- Compared with C++, the other tracks keep the same ordering and lookup ideas but differ in how visible comparator design is.
- Relative to Python and TypeScript, Go and C# ask for more explicit decisions around helper functions and ordering rules.
- The key comparison is not the algorithm itself, but how much control each language exposes around sorting behavior.

## Exercise Focus

- exercises/01.go: implement selection sort.
- exercises/02.go: binary search on sorted input.

### Exercise Specs

1. exercises/01.go
- Input: integer `n`, then `n` integers.
- Output: numbers sorted ascending.
- Edge cases: duplicate values; already sorted input.

2. exercises/02.go
- Input: sorted list and target.
- Output: index of target or `-1`.
- Edge cases: target smaller than min; target larger than max.

## Checkpoint

- [ ] I can implement selection sort from scratch.
- [ ] I know when linear vs binary search is appropriate.
- [ ] I can debug boundary conditions in search loops.
- [ ] I completed exercises/01.go.
- [ ] I completed exercises/02.go.
