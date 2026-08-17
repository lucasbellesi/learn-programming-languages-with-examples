# Templates Basics (C++)

This module introduces generic programming with templates.

## Learning Metadata

- Difficulty: Intermediate.
- Estimated Time: 35-50 minutes.
- Prerequisites: `01-foundations/functions`, `03-advanced/structs-and-classes`.
- Cross-Language Lens: Compare C++ templates with C# generics, Go type parameters, and Python's runtime flexibility.

## Learning Outcomes

- `ADV-GEN-01`: Express reusable type-safe behavior with language generics.
- `ADV-GEN-02`: Apply constraints when an operation requires specific capabilities.

## Quick Run

Run from the repository root:

~~~bash
python scripts/automation.py run-module --module-path languages/cpp/03-advanced/templates-basics
~~~

## More Examples

- `example/generic-print-and-sum.cpp`:

```bash
g++ -std=c++17 -Wall -Wextra -pedantic example/generic-print-and-sum.cpp -o templates_generic_print_sum
./templates_generic_print_sum
```

## Topics Covered

- Function templates.
- Class templates.
- Type-independent algorithms.
- Compile-time type substitution.

## Common Pitfalls

- Defining template implementations only in `.cpp` files.
- Assuming all types support required operators.
- Confusing template type deduction behavior.

## Cross-Language Notes

- In C++, read this module through the native focus ?Templates Basics?; the shared folder name remains stable for side-by-side navigation.
- Use explicit value/reference semantics and standard-library types to demonstrate how to express reusable type-safe behavior with language generics.
- Compare observable behavior with the other tracks when learning to apply constraints when an operation requires specific capabilities; equivalent evidence matters more than identical syntax.

## Exercise Focus

- `exercises/01.cpp`: template swap function.
- `exercises/02.cpp`: template average over numeric vectors.

### Exercise Specs

1. `exercises/01.cpp`
- Input: two values of same type.
- Output: values before and after swap.
- Edge cases: identical values; negative numbers.

2. `exercises/02.cpp`
- Input: numeric sequence.
- Output: arithmetic average.
- Edge cases: empty vector should return `0`; mixed positive/negative values.

## Check Your Work

Run from the repository root after implementing a starter:

```bash
python scripts/automation.py check-exercise --language cpp --level 03-advanced --module templates-basics --exercise 01
```

Change `--exercise 01` to `--exercise 02` for the second task. Consult `exercises/solutions/` only after making a complete attempt.

## Checkpoint

- [ ] I can write and call function templates.
- [ ] I can create simple class templates.
- [ ] I can identify type constraints in template code.
- [ ] I completed both exercises.
