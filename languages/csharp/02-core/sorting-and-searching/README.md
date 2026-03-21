# Sorting and Searching (C#)

This module introduces basic sorting and searching techniques.

## Quick Run

~~~bash
dotnet run --project example/sorting-and-searching-example.csproj
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

## Checkpoint

- [ ] I can implement selection sort from scratch.
- [ ] I know when linear vs binary search is appropriate.
- [ ] I can debug boundary conditions in search loops.
- [ ] I completed exercises/01.cs.
- [ ] I completed exercises/02.cs.
