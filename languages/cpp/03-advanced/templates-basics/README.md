# Templates Basics

This module introduces generic programming with templates.

## Learning Metadata

- Difficulty: Intermediate.
- Estimated Time: 35-50 minutes.
- Prerequisites: `01-foundations/functions`, `03-advanced/structs-and-classes`.
- Cross-Language Lens: Compare C++ templates with C# generics, Go type parameters, and Python's runtime flexibility.

## Quick Run

```bash
g++ -std=c++17 -Wall -Wextra -pedantic example/main.cpp -o templates_basics_example
./templates_basics_example
```

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

- Compared with C++, this concept broadens from templates into each language's own reusable generic abstraction model.
- Relative to Go and C#, TypeScript generics stay expressive without runtime specialization, while Python treats the same idea more informally.
- The useful comparison is how each language generalizes logic without abandoning type clarity.

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

## Checkpoint

- [ ] I can write and call function templates.
- [ ] I can create simple class templates.
- [ ] I can identify type constraints in template code.
- [ ] I completed both exercises.
