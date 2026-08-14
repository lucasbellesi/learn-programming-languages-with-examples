# Input Validation (C#)

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
python scripts/automation.py run-module --module-path languages/csharp/02-core/input-validation
~~~

## Topics Covered

- Validating integers and decimals using `TryParse`.
- Enforcing value ranges before consuming input.
- Reusing helper methods for consistent validation logic.
- Keeping console applications stable when users provide invalid data.

## Common Pitfalls

- Using `int.Parse` or `double.Parse` directly for user-entered text.
- Accepting out-of-range values after successful parsing.
- Duplicating similar validation loops instead of extracting helpers.

## Exercise Focus

- exercises/01.cs: read an integer in range 1 to 100 and print its square.
- exercises/02.cs: read a valid score count and valid scores, then print average.

### Exercise Specs

1. exercises/01.cs
- Input: repeated attempts until a valid integer in range 1..100 is entered.
- Output: square of the accepted value.
- Edge cases: non-numeric text; values below 1 or above 100.

2. exercises/02.cs
- Input: score count in range 1..50, followed by scores in range 0..100.
- Output: average score.
- Edge cases: invalid score entered mid-sequence; boundary values 0 and 100.

## Check Your Work

Run from the repository root after implementing a starter:

```bash
python scripts/automation.py check-exercise --language csharp --level 02-core --module input-validation --exercise 01
```

Change `--exercise 01` to `--exercise 02` for the second task. Consult `exercises/solutions/` only after making a complete attempt.

## Checkpoint

- [ ] I can validate input with `TryParse` and range checks.
- [ ] I can recover from invalid entries without terminating the program.
- [ ] I can structure reusable input helper methods.
- [ ] I completed exercises/01.cs.
- [ ] I completed exercises/02.cs.
