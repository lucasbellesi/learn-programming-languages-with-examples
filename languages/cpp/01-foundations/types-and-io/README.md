# Types and Input/Output

This module covers basic data types and console input/output in C++.

## Quick Run

```bash
g++ -std=c++17 -Wall -Wextra -pedantic example/main.cpp -o types_and_io_example
./types_and_io_example
```

## More Examples

- `example/input-validation-loop.cpp`:

```bash
g++ -std=c++17 -Wall -Wextra -pedantic example/input-validation-loop.cpp -o types_and_io_validation_loop
./types_and_io_validation_loop
```

## Topics Covered

- `int`, `double`, `char`, `bool`, `std::string`.
- Formatted extraction with `std::cin`.
- Output formatting with `std::cout`.
- Full-line input using `std::getline`.

## Common Pitfalls

- Mixing `cin >>` and `getline` without clearing newline.
- Assuming numeric input always succeeds.
- Forgetting to check ranges for user input.

## Exercise Focus

- `exercises/01.cpp`: read `N` numbers and compute sum, average, min, max.
- `exercises/02.cpp`: parse `product price quantity` and compute total price.

### Exercise Specs

1. `exercises/01.cpp`
- Input: integer `N` followed by `N` numeric values.
- Output: sum, average, minimum, maximum.
- Edge cases: `N <= 0` should exit with message; all equal values should produce equal min/max.

2. `exercises/02.cpp`
- Input: single line: `product price quantity`.
- Output: parsed fields and total price.
- Edge cases: quantity `0` should give total `0`; decimal price should keep precision.

## Checkpoint

- [ ] I can read and print typed values.
- [ ] I can safely use `getline` after formatted extraction.
- [ ] I can compute simple statistics from input.
- [ ] I completed both exercises.
