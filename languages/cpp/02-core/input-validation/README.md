# Input Validation

This module teaches how to read user input safely and repeatedly until it is valid.

## Why It Matters

Real programs must handle invalid input without crashing or producing wrong results.

## Quick Run

```bash
g++ -std=c++17 -Wall -Wextra -pedantic example/main.cpp -o input_validation_example
./input_validation_example
```

On Windows (MSYS2 shell), run:

```bash
./input_validation_example.exe
```

## Topics Covered

### Stream Validation

- `std::cin >> value` can fail when input type is wrong.
- On failure, clear error state with `std::cin.clear()`.
- Remove bad input with `std::cin.ignore(...)`.

### Range Validation

- Validate business rules after extraction (for example, age must be between 1 and 120).
- Keep asking until the value is acceptable.

### Reusable Validation Functions

Use small helper functions to avoid repeating validation logic.

## Common Pitfalls

- Not clearing `std::cin` after invalid input.
- Accepting values outside expected ranges.
- Writing duplicate validation loops everywhere instead of reusable helpers.

## Exercise Focus

- `exercises/01.cpp`: read a valid integer in a range and print its square.
- `exercises/02.cpp`: read multiple valid scores and compute class average.

## Checkpoint

- [ ] I can detect extraction failure and recover safely.
- [ ] I can enforce numeric ranges.
- [ ] I can loop until valid data is entered.
- [ ] I completed both exercises.
