# Input Validation (Python)

This module teaches defensive input handling for interactive programs.

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
python scripts/automation.py run-module --module-path languages/python/02-core/input-validation
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

## Cross-Language Notes

- In Python, read this module through the native focus ?Input Validation?; the shared folder name remains stable for side-by-side navigation.
- Use dynamic values, collection protocols, and context managers to demonstrate how to reject malformed and out-of-domain input without corrupting state.
- Compare observable behavior with the other tracks when learning to design retry and termination behavior that cannot loop accidentally; equivalent evidence matters more than identical syntax.

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

## Check Your Work

Run from the repository root after implementing a starter:

```bash
python scripts/automation.py check-exercise --language python --level 02-core --module input-validation --exercise 01
```

Change `--exercise 01` to `--exercise 02` for the second task. Consult `exercises/solutions/` only after making a complete attempt.

## Checkpoint

- [ ] I can recover from type parsing errors without crashing.
- [ ] I can validate numeric ranges with retry loops.
- [ ] I can reuse helper functions for multiple validated inputs.
- [ ] I completed exercises/01.py.
- [ ] I completed exercises/02.py.
