# Algorithms Basics (Python)

This module introduces common algorithmic patterns over lists.

## Quick Run

~~~bash
python example/main.py
~~~

## Topics Covered

- Linear search for the first matching index.
- Counting occurrences of a target value.
- One-pass minimum and maximum scanning.
- Combining multiple statistics in a single loop.

## Common Pitfalls

- Forgetting to handle empty lists before min/max logic.
- Initializing minimum or maximum with invalid defaults.
- Doing multiple passes when one pass is enough.

## Exercise Focus

- exercises/01.py: linear search and first index.
- exercises/02.py: minimum, maximum, and even-count in one pass.

### Exercise Specs

1. exercises/01.py
- Input: integer `n`, then `n` values, then a target.
- Output: first index of target or `-1`.
- Edge cases: `n <= 0`; target not present.

2. exercises/02.py
- Input: integer `n`, then `n` values.
- Output: minimum, maximum, and even count.
- Edge cases: all odd numbers (even count `0`); all equal values.

## Checkpoint

- [ ] I can implement linear search confidently.
- [ ] I can compute multiple statistics in one pass.
- [ ] I can reason about edge cases before coding.
- [ ] I completed exercises/01.py.
- [ ] I completed exercises/02.py.
