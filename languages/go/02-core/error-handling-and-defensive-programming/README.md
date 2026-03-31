# Error Handling and Defensive Programming (Go)

This module teaches robust validation checks and safe failure behavior.

## Learning Metadata

- Difficulty: Intermediate.
- Estimated Time: 30-45 minutes.
- Prerequisites: `02-core/input-validation`, `02-core/file-io-basics`.
- Cross-Language Lens: Compare exceptions, error returns, and guard-style validation as different ways to keep programs safe.

## Quick Run

~~~bash
go run example/main.go
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

## Checkpoint

- [ ] I can guard risky operations with clear checks.
- [ ] I can stop invalid program paths early.
- [ ] I can produce useful error feedback for users.
- [ ] I completed exercises/01.go.
- [ ] I completed exercises/02.go.
