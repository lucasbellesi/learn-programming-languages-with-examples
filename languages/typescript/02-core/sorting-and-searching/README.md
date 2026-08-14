# Sorting and Searching

This module practices ordering data and locating target values with explicit comparisons.

## Learning Metadata

- Difficulty: Intermediate.
- Estimated Time: 30-45 minutes.
- Prerequisites: `02-core/algorithms-basics` and `01-foundations/arrays-and-vectors`.
- Cross-Language Lens: Compare custom comparators, stable sort expectations, and hand-written search logic before assuming the standard library does the same thing everywhere.

## Learning Outcomes

- `COR-SRT-01`: Choose and apply sorting and searching operations correctly.
- `COR-SRT-02`: Explain ordering, duplicates, missing values, and stability tradeoffs.

## Quick Run

Run from the repository root:

~~~bash
python scripts/automation.py run-module --module-path languages/typescript/02-core/sorting-and-searching
~~~

## Topics Covered

- Numeric sorting with explicit comparators.
- Searching sorted data with binary search.
- Deciding when linear search is still the simpler answer.
- Keeping sort and search helpers predictable.

## Common Pitfalls

- Forgetting that JavaScript and TypeScript sort strings by default.
- Running binary search on unsorted input.
- Returning the wrong boundary when a target is missing.

## Cross-Language Notes

- Compared with C++, the other tracks keep the same ordering and lookup ideas but differ in how visible comparator design is.
- Relative to Python and TypeScript, Go and C# ask for more explicit decisions around helper functions and ordering rules.
- The key comparison is not the algorithm itself, but how much control each language exposes around sorting behavior.

## Exercise Focus

- exercises/01.ts: sort integers ascending.
- exercises/02.ts: run binary search on a sorted array.

### Exercise Specs

1. exercises/01.ts
- Input: integer `n`, then `n` integers.
- Output: the sorted values in ascending order.
- Edge cases: repeated values; negative values; `n <= 0`.

2. exercises/02.ts
- Input: integer `n`, then `n` sorted integers, then a target.
- Output: target index or `-1`.
- Edge cases: target absent; repeated values; `n <= 0`.

## Check Your Work

Run from the repository root after implementing a starter:

```bash
python scripts/automation.py check-exercise --language typescript --level 02-core --module sorting-and-searching --exercise 01
```

Change `--exercise 01` to `--exercise 02` for the second task. Consult `exercises/solutions/` only after making a complete attempt.

## Checkpoint

- [ ] I can sort numbers without relying on accidental string behavior.
- [ ] I can explain when binary search is valid.
- [ ] I can return `-1` cleanly when a target is missing.
- [ ] I completed exercises/01.ts.
- [ ] I completed exercises/02.ts.
