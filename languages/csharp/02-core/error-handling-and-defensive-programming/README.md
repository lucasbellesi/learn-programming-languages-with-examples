# Error Handling and Defensive Programming (C#)

This module teaches robust validation checks and safe failure behavior.

## Quick Run

~~~bash
dotnet run --project example/error-handling-and-defensive-programming-example.csproj
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

## Checkpoint

- [ ] I can guard risky operations with clear checks.
- [ ] I can stop invalid program paths early.
- [ ] I can produce useful error feedback for users.
- [ ] I completed exercises/01.cs.
- [ ] I completed exercises/02.cs.
