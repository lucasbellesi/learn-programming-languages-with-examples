# Input Validation

This module teaches defensive input handling in interactive programs.

## Learning Metadata

- Difficulty: Intermediate.
- Estimated Time: 30-45 minutes.
- Prerequisites: `01-foundations/control-flow`, `01-foundations/types-and-io`.
- Cross-Language Lens: Compare loop-driven validation in all six active languages and notice where parsing APIs are strict versus forgiving.

## Learning Outcomes

- `COR-VAL-01`: Reject malformed and out-of-domain input without corrupting state.
- `COR-VAL-02`: Design retry and termination behavior that cannot loop accidentally.

## Quick Run

Run from the repository root:

~~~bash
python scripts/automation.py run-module --module-path languages/cpp/02-core/input-validation
~~~

## More Examples

- `example/main.cpp` is the primary runnable sample for this module.
- Try one variation: copy it to `example/variation.cpp`, change one rule, and compare outputs.

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

## Check Your Work

Run from the repository root after implementing a starter:

```bash
python scripts/automation.py check-exercise --language cpp --level 02-core --module input-validation --exercise 01
```

Change `--exercise 01` to `--exercise 02` for the second task. Consult `exercises/solutions/` only after making a complete attempt.

## Checkpoint

- [ ] I can recover from invalid stream states.
- [ ] I can enforce both type and range constraints.
- [ ] I can implement retry loops cleanly.
- [ ] I completed both exercises.
