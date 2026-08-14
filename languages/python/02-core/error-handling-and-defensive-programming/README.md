# Error Handling and Defensive Programming (Python)

This module teaches robust validation checks and safe failure behavior.

## Learning Metadata

- Difficulty: Intermediate.
- Estimated Time: 30-45 minutes.
- Prerequisites: `02-core/input-validation`, `02-core/file-io-basics`.
- Cross-Language Lens: Compare exceptions, error returns, and guard-style validation as different ways to keep programs safe.

## Learning Outcomes

- `COR-ERR-01`: Separate expected failures from programming defects.
- `COR-ERR-02`: Preserve valid state and useful diagnostics when operations fail.

## Quick Run

~~~bash
python example/main.py
~~~

## Topics Covered

- Defensive input validation with retry logic.
- Early returns for invalid states.
- Guard conditions before risky operations.
- Producing clear and actionable error messages.

## Common Pitfalls

- Continuing execution after detecting invalid input.
- Performing division without zero checks.
- Catching errors without giving useful user feedback.

## Exercise Focus

- exercises/01.py: validate CSV-like row format.
- exercises/02.py: safe division utility with retries.

### Exercise Specs

1. exercises/01.py
- Input: one row with format `name,age,city`.
- Output: parsed fields or invalid format message.
- Edge cases: missing commas; empty fields.

2. exercises/02.py
- Input: pairs of numbers for division until valid.
- Output: quotient or error/retry message.
- Edge cases: divisor zero; non-numeric input.

## Check Your Work

Run from the repository root after implementing a starter:

```bash
python scripts/automation.py check-exercise --language python --level 02-core --module error-handling-and-defensive-programming --exercise 01
```

Change `--exercise 01` to `--exercise 02` for the second task. Consult `exercises/solutions/` only after making a complete attempt.

## Checkpoint

- [ ] I can guard risky operations with clear checks.
- [ ] I can stop invalid program paths early.
- [ ] I can produce useful error feedback for users.
- [ ] I completed exercises/01.py.
- [ ] I completed exercises/02.py.
