# Constructors and Invariants

This module shows how constructors enforce valid object state.

## Quick Run

```bash
g++ -std=c++17 -Wall -Wextra -pedantic example/main.cpp -o constructors_invariants_example
./constructors_invariants_example
```

## Topics Covered

- Constructor initialization.
- Invariants as always-true rules.
- Validation in constructors and setters.
- Safe update methods.

## Common Pitfalls

- Leaving objects in invalid states.
- Validating only at use-time, not construction-time.
- Ignoring boundary conditions.

## Exercise Focus

- `exercises/01.cpp`: bank account with non-negative balance.
- `exercises/02.cpp`: date class with month/day validation.

### Exercise Specs

1. `exercises/01.cpp`
- Input: initial balance and transaction values.
- Output: updated balance with validity checks.
- Edge cases: negative initial balance; withdrawal beyond balance.

2. `exercises/02.cpp`
- Input: month and day values.
- Output: valid/invalid date result.
- Edge cases: month out of range; day out of range for month.

## Checkpoint

- [ ] I can define clear invariants for a class.
- [ ] I can enforce invariants in constructors and methods.
- [ ] I can reject invalid updates safely.
- [ ] I completed both exercises.
