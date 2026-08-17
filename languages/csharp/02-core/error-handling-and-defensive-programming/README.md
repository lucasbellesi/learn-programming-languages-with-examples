# Error Handling and Defensive Programming (C#)

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
python scripts/automation.py run-module --module-path languages/csharp/02-core/error-handling-and-defensive-programming
~~~

## Topics Covered

- Defensive input validation with retry loops.
- Early returns for invalid states.
- Guard conditions before risky operations.
- Producing clear and actionable error messages.

## Common Pitfalls

- Continuing execution after detecting an invalid state.
- Performing division without zero checks.
- Printing vague errors that do not help recovery.

## Cross-Language Notes

- In C#, read this module through the native focus ?Error Handling and Defensive Programming?; the shared folder name remains stable for side-by-side navigation.
- Use static types, .NET collections, and managed-resource patterns to demonstrate how to separate expected failures from programming defects.
- Compare observable behavior with the other tracks when learning to preserve valid state and useful diagnostics when operations fail; equivalent evidence matters more than identical syntax.

## Exercise Focus

- exercises/01.cs: validate CSV-like row format.
- exercises/02.cs: safe division utility with retries.

### Exercise Specs

1. exercises/01.cs
- Input: one row with format `name,age,city`.
- Output: parsed fields or invalid format message.
- Edge cases: missing commas; empty fields.

2. exercises/02.cs
- Input: pairs of numbers for division until valid.
- Output: quotient or error/retry message.
- Edge cases: divisor zero; non-numeric input.

## Check Your Work

Run from the repository root after implementing a starter:

```bash
python scripts/automation.py check-exercise --language csharp --level 02-core --module error-handling-and-defensive-programming --exercise 01
```

Change `--exercise 01` to `--exercise 02` for the second task. Consult `exercises/solutions/` only after making a complete attempt.

## Checkpoint

- [ ] I can guard risky operations with clear checks.
- [ ] I can stop invalid program paths early.
- [ ] I can produce useful error feedback for users.
- [ ] I completed exercises/01.cs.
- [ ] I completed exercises/02.cs.
