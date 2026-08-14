# Functions

This module introduces reusable logic through function design.

## Learning Metadata

- Difficulty: Beginner.
- Estimated Time: 20-35 minutes.
- Prerequisites: `01-foundations/control-flow`, `01-foundations/operators-and-expressions`.
- Cross-Language Lens: Compare helper-function design, argument passing defaults, and overloading support across the six active tracks.

## Learning Outcomes

- `FND-FUN-01`: Decompose a problem into focused functions with explicit contracts.
- `FND-FUN-02`: Use parameters and return values without hidden state changes.

## Quick Run

Run from the repository root:

~~~bash
python scripts/automation.py run-module --module-path languages/cpp/01-foundations/functions
~~~

## More Examples

- `example/function-overload-basics.cpp`:

```bash
g++ -std=c++17 -Wall -Wextra -pedantic example/function-overload-basics.cpp -o functions_overload_basics
./functions_overload_basics
```

- `example/parameter-passing.cpp` contrasts pass-by-value and pass-by-reference.

## Topics Covered

- Pass by value.
- Pass by reference.
- Pass by const reference.
- Returning values.

## Common Pitfalls

- Unnecessary copies of large objects.
- Missing `const` in read-only reference parameters.
- Missing return values in non-`void` functions.

## Cross-Language Notes

- C++ is the baseline for overloads, parameter passing choices, and return-type declarations as distinct language features.
- Compared with Python, Go, and TypeScript, function signatures carry more control over value and reference behavior.
- The main comparison is how much semantic weight each language puts on a function declaration.

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

## Check Your Work

Run from the repository root after implementing a starter:

```bash
python scripts/automation.py check-exercise --language cpp --level 01-foundations --module functions --exercise 01
```

Change `--exercise 01` to `--exercise 02` for the second task. Consult `exercises/solutions/` only after making a complete attempt.

## Checkpoint

- [ ] I can select parameter passing style intentionally.
- [ ] I can write read-only APIs using `const`.
- [ ] I can return computed results from helper functions.
- [ ] I completed both exercises.
