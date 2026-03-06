# Error Handling and Defensive Programming

This module teaches robust error checks and safe failure behavior.

## Quick Run

```bash
g++ -std=c++17 -Wall -Wextra -pedantic example/main.cpp -o defensive_programming_example
./defensive_programming_example
```

## Topics Covered

- Defensive input validation.
- Early returns for invalid states.
- Guard conditions before risky operations.
- Reporting clear error messages.

## Common Pitfalls

- Continuing after a known invalid state.
- Performing division without zero checks.
- Hiding errors with vague messages.

## Exercise Focus

- `exercises/01.cpp`: validate CSV-like row format.
- `exercises/02.cpp`: safe division utility with retries.

### Exercise Specs

1. `exercises/01.cpp`
- Input: one row with format `name,age,city`.
- Output: parsed fields or invalid format message.
- Edge cases: missing commas; empty fields.

2. `exercises/02.cpp`
- Input: pairs of numbers for division until valid.
- Output: quotient or error/retry message.
- Edge cases: divisor zero; non-numeric input.

## Checkpoint

- [ ] I can guard risky operations with clear checks.
- [ ] I can stop invalid program paths early.
- [ ] I can produce useful error feedback for users.
- [ ] I completed both exercises.
