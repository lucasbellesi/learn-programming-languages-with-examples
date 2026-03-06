# Input Validation

This module teaches defensive input handling in interactive programs.

## Quick Run

```bash
g++ -std=c++17 -Wall -Wextra -pedantic example/main.cpp -o input_validation_example
./input_validation_example
```

## Topics Covered

- Detecting extraction failure (`if (!(cin >> value))`).
- Clearing stream state with `cin.clear()`.
- Discarding invalid buffer with `cin.ignore(...)`.
- Reusable range-validation loops.

## Common Pitfalls

- Continuing reads without clearing failed stream state.
- Accepting out-of-range values.
- Duplicating validation loops instead of using helper functions.

## Exercise Focus

- `exercises/01.cpp`: read integer in range `[1, 100]` then print square.
- `exercises/02.cpp`: read valid scores and compute average.

### Exercise Specs

1. `exercises/01.cpp`
- Input: integer attempts until valid.
- Output: square of valid number.
- Edge cases: non-integer input; values below 1 or above 100.

2. `exercises/02.cpp`
- Input: score count in `[1, 50]`, then scores in `[0, 100]`.
- Output: class average.
- Edge cases: invalid types mid-sequence; boundary values `0`, `100`.

## Checkpoint

- [ ] I can recover from invalid stream states.
- [ ] I can enforce both type and range constraints.
- [ ] I can implement retry loops cleanly.
- [ ] I completed both exercises.
