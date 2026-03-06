# Functions

This module introduces reusable logic through function design.

## Quick Run

```bash
g++ -std=c++17 -Wall -Wextra -pedantic example/main.cpp -o functions_example
./functions_example
```

## Topics Covered

- Pass by value.
- Pass by reference.
- Pass by const reference.
- Returning values.

## Common Pitfalls

- Unnecessary copies of large objects.
- Missing `const` in read-only reference parameters.
- Missing return values in non-`void` functions.

## Exercise Focus

- `exercises/01.cpp`: return max of three integers.
- `exercises/02.cpp`: count vowels in a string.

### Exercise Specs

1. `exercises/01.cpp`
- Input: three integers.
- Output: largest integer.
- Edge cases: repeated max values should still return correct max; all negative values should still work.

2. `exercises/02.cpp`
- Input: one line of text.
- Output: vowel count.
- Edge cases: empty string returns `0`; uppercase vowels should be counted.

## Checkpoint

- [ ] I can select parameter passing style intentionally.
- [ ] I can write read-only APIs using `const`.
- [ ] I can return computed results from helper functions.
- [ ] I completed both exercises.
