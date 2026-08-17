# Operators and Expressions

This module covers arithmetic, relational, and logical expressions in C++.

## Learning Metadata

- Difficulty: Beginner.
- Estimated Time: 20-35 minutes.
- Prerequisites: `01-foundations/types-and-io`.
- Cross-Language Lens: Compare integer division, boolean logic, and truthiness rules before assuming the same expression means the same thing in every language.

## Learning Outcomes

- `FND-OPE-01`: Build expressions with correct precedence and explicit intent.
- `FND-OPE-02`: Distinguish arithmetic, comparison, and logical operations.

## Quick Run

Run from the repository root:

~~~bash
python scripts/automation.py run-module --module-path languages/cpp/01-foundations/operators-and-expressions
~~~

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

## Cross-Language Notes

- In C++, read this module through the native focus ?Operators and Expressions?; the shared folder name remains stable for side-by-side navigation.
- Use explicit value/reference semantics and standard-library types to demonstrate how to build expressions with correct precedence and explicit intent.
- Compare observable behavior with the other tracks when learning to distinguish arithmetic, comparison, and logical operations; equivalent evidence matters more than identical syntax.

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

## Check Your Work

Run from the repository root after implementing a starter:

```bash
python scripts/automation.py check-exercise --language cpp --level 01-foundations --module operators-and-expressions --exercise 01
```

Change `--exercise 01` to `--exercise 02` for the second task. Consult `exercises/solutions/` only after making a complete attempt.

## Checkpoint

- [ ] I can predict expression results with precedence.
- [ ] I can use logical expressions in real conditions.
- [ ] I can format computed output clearly.
- [ ] I completed both exercises.
