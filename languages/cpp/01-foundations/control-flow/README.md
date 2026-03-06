# Control Flow

This module teaches branching and repetition in C++ programs.

## Quick Run

```bash
g++ -std=c++17 -Wall -Wextra -pedantic example/main.cpp -o control_flow_example
./control_flow_example
```

## More Examples

- `example/menu-loop.cpp`:

```bash
g++ -std=c++17 -Wall -Wextra -pedantic example/menu-loop.cpp -o control_flow_menu_loop
./control_flow_menu_loop
```

## Topics Covered

- `if`, `else if`, `else`.
- `switch` with `case` and `default`.
- `for` and `while` loops.
- Loop control with `break` and `continue`.

## Common Pitfalls

- Missing braces in multi-line branches.
- Infinite loops due to missing updates.
- Missing `break` in `switch` cases.

## Exercise Focus

- `exercises/01.cpp`: implement FizzBuzz.
- `exercises/02.cpp`: read numbers until `-1` and compute average.

### Exercise Specs

1. `exercises/01.cpp`
- Input: integer `N`.
- Output: numbers `1..N` with FizzBuzz substitutions.
- Edge cases: `N <= 0` should print a friendly message; multiples of both 3 and 5 should print `FizzBuzz`.

2. `exercises/02.cpp`
- Input: sequence of integers ending with `-1`.
- Output: average of entered numbers before sentinel.
- Edge cases: immediate `-1` should print "no values"; negative values other than `-1` are valid inputs.

## Checkpoint

- [ ] I can choose between `if` and `switch`.
- [ ] I can write safe, terminating loops.
- [ ] I can reason about branch and loop edge cases.
- [ ] I completed both exercises.
