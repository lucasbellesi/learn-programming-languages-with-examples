# Templates Basics

This module introduces generic programming with templates.

## Quick Run

```bash
g++ -std=c++17 -Wall -Wextra -pedantic example/main.cpp -o templates_basics_example
./templates_basics_example
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
