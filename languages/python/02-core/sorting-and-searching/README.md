# Sorting and Searching (Python)

This module introduces basic sorting and searching techniques.

## Quick Run

~~~bash
python example/main.py
~~~

## Topics Covered

- Sorting integer lists in ascending order.
- Implementing binary search with clear boundaries.
- Understanding why binary search requires sorted data.
- Comparing linear and logarithmic search strategies.

## Common Pitfalls

- Running binary search on unsorted input.
- Off-by-one mistakes in midpoint and boundaries.
- Forgetting to return `-1` when the target does not exist.

## Exercise Focus

- exercises/01.py: implement selection sort.
- exercises/02.py: binary search on sorted input.

### Exercise Specs

1. exercises/01.py
- Input: integer `n`, then `n` integers.
- Output: numbers sorted ascending.
- Edge cases: duplicate values; already sorted input.

2. exercises/02.py
- Input: sorted list and target.
- Output: index of target or `-1`.
- Edge cases: target smaller than min; target larger than max.

## Checkpoint

- [ ] I can implement selection sort from scratch.
- [ ] I know when linear vs binary search is appropriate.
- [ ] I can debug boundary conditions in search loops.
- [ ] I completed exercises/01.py.
- [ ] I completed exercises/02.py.
