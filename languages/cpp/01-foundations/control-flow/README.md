# Control Flow

This module teaches branching and repetition in C++ programs.

## Learning Metadata

- Difficulty: Beginner.
- Estimated Time: 20-35 minutes.
- Prerequisites: `01-foundations/types-and-io`, `01-foundations/operators-and-expressions`.
- Cross-Language Lens: Compare braces-and-loops in C++, C#, and Go with Python indentation while keeping the underlying branching logic identical.

## Learning Outcomes

- `FND-CFL-01`: Select branches that cover normal and boundary conditions.
- `FND-CFL-02`: Write terminating loops and reason about their invariants.

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

- `example/factorial.cpp` isolates a guarded accumulation loop.

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

## Check Your Work

Run from the repository root after implementing a starter:

```bash
python scripts/automation.py check-exercise --language cpp --level 01-foundations --module control-flow --exercise 01
```

Change `--exercise 01` to `--exercise 02` for the second task. Consult `exercises/solutions/` only after making a complete attempt.

## Checkpoint

- [ ] I can choose between `if` and `switch`.
- [ ] I can write safe, terminating loops.
- [ ] I can reason about branch and loop edge cases.
- [ ] I completed both exercises.
