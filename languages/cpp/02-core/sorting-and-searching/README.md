# Sorting and Searching

This module introduces basic sorting and searching techniques.

## Learning Metadata

- Difficulty: Intermediate.
- Estimated Time: 30-45 minutes.
- Prerequisites: `02-core/algorithms-basics`, `01-foundations/arrays-and-vectors`.
- Cross-Language Lens: Compare built-in sort and search helpers and the stability guarantees each standard library makes.

## Quick Run

```bash
g++ -std=c++17 -Wall -Wextra -pedantic example/main.cpp -o sorting_searching_example
./sorting_searching_example
```

## More Examples

- `example/stable-vs-unstable-sort.cpp`:

```bash
g++ -std=c++17 -Wall -Wextra -pedantic example/stable-vs-unstable-sort.cpp -o sorting_stable_vs_unstable
./sorting_stable_vs_unstable
```

## Topics Covered

- Manual sorting with nested loops.
- Linear search.
- Binary search assumptions.
- Algorithm complexity intuition.

## Common Pitfalls

- Running binary search on unsorted data.
- Off-by-one index errors.
- Forgetting to return `-1` when target is missing.

## Cross-Language Notes

- Compared with C++, the other tracks keep the same ordering and lookup ideas but differ in how visible comparator design is.
- Relative to Python and TypeScript, Go and C# ask for more explicit decisions around helper functions and ordering rules.
- The key comparison is not the algorithm itself, but how much control each language exposes around sorting behavior.

## Exercise Focus

- `exercises/01.cpp`: implement selection sort.
- `exercises/02.cpp`: binary search on sorted input.

### Exercise Specs

1. `exercises/01.cpp`
- Input: integer `n`, then `n` integers.
- Output: numbers sorted ascending.
- Edge cases: duplicate values; already sorted input.

2. `exercises/02.cpp`
- Input: sorted list and target.
- Output: index of target or `-1`.
- Edge cases: target smaller than min; target larger than max.

## Checkpoint

- [ ] I can implement selection sort from scratch.
- [ ] I know when linear vs binary search is appropriate.
- [ ] I can debug boundary conditions in search loops.
- [ ] I completed both exercises.
