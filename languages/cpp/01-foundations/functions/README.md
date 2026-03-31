# Functions

This module introduces reusable logic through function design.

## Learning Metadata

- Difficulty: Beginner.
- Estimated Time: 20-35 minutes.
- Prerequisites: `01-foundations/control-flow`, `01-foundations/operators-and-expressions`.
- Cross-Language Lens: Compare helper-function design, argument passing defaults, and overloading support across the four tracks.

## Quick Run

```bash
g++ -std=c++17 -Wall -Wextra -pedantic example/main.cpp -o functions_example
./functions_example
```

## More Examples

- `example/function-overload-basics.cpp`:

```bash
g++ -std=c++17 -Wall -Wextra -pedantic example/function-overload-basics.cpp -o functions_overload_basics
./functions_overload_basics
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
