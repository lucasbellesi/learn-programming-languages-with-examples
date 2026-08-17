# Error Handling and Defensive Programming (Go)

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

Run from the repository root:

~~~bash
python scripts/automation.py run-module --module-path languages/go/02-core/error-handling-and-defensive-programming
~~~

## Topics Covered

- Defensive input validation with retry logic.
- Early returns for invalid states.
- Guard conditions before risky operations.
- Producing clear and actionable error messages.

## Common Pitfalls

- Continuing execution after detecting invalid input.
- Performing division without zero checks.
- Ignoring parse errors from numeric conversion.

## Cross-Language Notes

- In Go, read this module through the native focus ?Error Handling and Defensive Programming?; the shared folder name remains stable for side-by-side navigation.
- Use explicit errors, slices/maps, interfaces, and defer to demonstrate how to separate expected failures from programming defects.
- Compare observable behavior with the other tracks when learning to preserve valid state and useful diagnostics when operations fail; equivalent evidence matters more than identical syntax.

## Exercise Focus

- exercises/01.go: validate CSV-like row format.
- exercises/02.go: safe division utility with retries.

### Exercise Specs

1. exercises/01.go
- Input: one row with format `name,age,city`.
- Output: parsed fields or invalid format message.
- Edge cases: missing commas; empty fields.

2. exercises/02.go
- Input: pairs of numbers for division until valid.
- Output: quotient or error/retry message.
- Edge cases: divisor zero; non-numeric input.

## Check Your Work

Run from the repository root after implementing a starter:

```bash
python scripts/automation.py check-exercise --language go --level 02-core --module error-handling-and-defensive-programming --exercise 01
```

Change `--exercise 01` to `--exercise 02` for the second task. Consult `exercises/solutions/` only after making a complete attempt.

## Checkpoint

- [ ] I can guard risky operations with clear checks.
- [ ] I can stop invalid program paths early.
- [ ] I can produce useful error feedback for users.
- [ ] I completed exercises/01.go.
- [ ] I completed exercises/02.go.
