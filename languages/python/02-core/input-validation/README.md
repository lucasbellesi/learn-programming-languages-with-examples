# Input Validation (Python)

This module teaches defensive input handling for interactive programs.

## Quick Run

~~~bash
python example/main.py
~~~

## Topics Covered

- Validating integer and floating-point input with retry loops.
- Rejecting values outside accepted ranges.
- Reusing input-validation helpers to avoid duplicated logic.
- Keeping interactive programs stable when users type invalid data.

## Common Pitfalls

- Calling `int()` or `float()` once and crashing on invalid input.
- Accepting out-of-range values after successful parsing.
- Repeating similar validation logic instead of extracting helpers.

## Exercise Focus

- exercises/01.py: read an integer in range 1 to 100 and print its square.
- exercises/02.py: read a valid score count and valid scores, then print average.

### Exercise Specs

1. exercises/01.py
- Input: repeated attempts until a valid integer in range 1..100 is entered.
- Output: square of the accepted value.
- Edge cases: non-integer text; values below 1 or above 100.

2. exercises/02.py
- Input: score count in range 1..50, followed by scores in range 0..100.
- Output: average score.
- Edge cases: invalid value in the middle of score entry; boundary values 0 and 100.

## Checkpoint

- [ ] I can recover from type parsing errors without crashing.
- [ ] I can validate numeric ranges with retry loops.
- [ ] I can reuse helper functions for multiple validated inputs.
- [ ] I completed exercises/01.py.
- [ ] I completed exercises/02.py.
