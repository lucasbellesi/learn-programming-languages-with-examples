# Sorting and Searching (C#)

This module introduces basic sorting and searching techniques.

## Learning Metadata

- Difficulty: Intermediate.
- Estimated Time: 30-45 minutes.
- Prerequisites: `02-core/algorithms-basics`, `01-foundations/arrays-and-vectors`.
- Cross-Language Lens: Compare built-in sort and search helpers and the stability guarantees each standard library makes.

## Learning Outcomes

- `COR-SRT-01`: Choose and apply sorting and searching operations correctly.
- `COR-SRT-02`: Explain ordering, duplicates, missing values, and stability tradeoffs.

## Quick Run

Run from the repository root:

~~~bash
python scripts/automation.py run-module --module-path languages/csharp/02-core/sorting-and-searching
~~~

## Topics Covered

- Sorting integer collections in ascending order.
- Implementing linear and binary search patterns.
- Understanding why binary search requires sorted data.
- Reasoning about time complexity tradeoffs.

## Common Pitfalls

- Running binary search on unsorted input.
- Off-by-one errors in `left` and `right` boundaries.
- Forgetting to return `-1` when a target is missing.

## Cross-Language Notes

- In C#, read this module through the native focus ?Sorting and Searching?; the shared folder name remains stable for side-by-side navigation.
- Use static types, .NET collections, and managed-resource patterns to demonstrate how to choose and apply sorting and searching operations correctly.
- Compare observable behavior with the other tracks when learning to explain ordering, duplicates, missing values, and stability tradeoffs; equivalent evidence matters more than identical syntax.

## Exercise Focus

- exercises/01.cs: implement selection sort.
- exercises/02.cs: binary search on sorted input.

### Exercise Specs

1. exercises/01.cs
- Input: integer `n`, then `n` integers.
- Output: numbers sorted ascending.
- Edge cases: duplicate values; already sorted input.

2. exercises/02.cs
- Input: sorted list and target.
- Output: index of target or `-1`.
- Edge cases: target smaller than min; target larger than max.

## Check Your Work

Run from the repository root after implementing a starter:

```bash
python scripts/automation.py check-exercise --language csharp --level 02-core --module sorting-and-searching --exercise 01
```

Change `--exercise 01` to `--exercise 02` for the second task. Consult `exercises/solutions/` only after making a complete attempt.

## Checkpoint

- [ ] I can implement selection sort from scratch.
- [ ] I know when linear vs binary search is appropriate.
- [ ] I can debug boundary conditions in search loops.
- [ ] I completed exercises/01.cs.
- [ ] I completed exercises/02.cs.
