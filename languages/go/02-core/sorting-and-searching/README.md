# Sorting and Searching (Go)

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
python scripts/automation.py run-module --module-path languages/go/02-core/sorting-and-searching
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

- In Go, read this module through the native focus ?Sorting and Searching?; the shared folder name remains stable for side-by-side navigation.
- Use explicit errors, slices/maps, interfaces, and defer to demonstrate how to choose and apply sorting and searching operations correctly.
- Compare observable behavior with the other tracks when learning to explain ordering, duplicates, missing values, and stability tradeoffs; equivalent evidence matters more than identical syntax.

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

## Check Your Work

Run from the repository root after implementing a starter:

```bash
python scripts/automation.py check-exercise --language go --level 02-core --module sorting-and-searching --exercise 01
```

Change `--exercise 01` to `--exercise 02` for the second task. Consult `exercises/solutions/` only after making a complete attempt.

## Checkpoint

- [ ] I can implement selection sort from scratch.
- [ ] I know when linear vs binary search is appropriate.
- [ ] I can debug boundary conditions in search loops.
- [ ] I completed exercises/01.go.
- [ ] I completed exercises/02.go.
