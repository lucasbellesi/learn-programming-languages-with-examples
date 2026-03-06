# Operators and Expressions

This module covers arithmetic, relational, and logical expressions in C++.

## Quick Run

```bash
g++ -std=c++17 -Wall -Wextra -pedantic example/main.cpp -o operators_example
./operators_example
```

## More Examples

- `example/main.cpp` is the primary runnable sample for this module.
- Try one variation: copy it to `example/variation.cpp`, change one rule, and compare outputs.

## Topics Covered

- Arithmetic operators (`+`, `-`, `*`, `/`, `%`).
- Comparison operators (`==`, `!=`, `<`, `>`, `<=`, `>=`).
- Logical operators (`&&`, `||`, `!`).
- Parentheses and precedence.

## Common Pitfalls

- Integer division when a decimal result is expected.
- Complex expressions without parentheses.
- Forgetting `%` only works with integers.

## Exercise Focus

- `exercises/01.cpp`: convert seconds into hours/minutes/seconds.
- `exercises/02.cpp`: compute final price with discount and tax rules.

### Exercise Specs

1. `exercises/01.cpp`
- Input: total seconds as integer.
- Output: formatted `H:M:S` conversion.
- Edge cases: `0` seconds; values under one minute.

2. `exercises/02.cpp`
- Input: base price, discount eligibility (`0` or `1`), tax rate.
- Output: final price after discount and tax.
- Edge cases: no discount case; zero tax case.

## Checkpoint

- [ ] I can predict expression results with precedence.
- [ ] I can use logical expressions in real conditions.
- [ ] I can format computed output clearly.
- [ ] I completed both exercises.
