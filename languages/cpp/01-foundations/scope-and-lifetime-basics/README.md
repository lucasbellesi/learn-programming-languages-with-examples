# Scope and Lifetime Basics

This module explains where variables are visible and how long they live.

## Learning Metadata

- Difficulty: Beginner.
- Estimated Time: 20-35 minutes.
- Prerequisites: `01-foundations/functions`, `01-foundations/control-flow`.
- Cross-Language Lens: Compare block scope everywhere, then contrast deterministic destruction in C++ with garbage-collected lifetime in the other tracks.

## Quick Run

```bash
g++ -std=c++17 -Wall -Wextra -pedantic example/main.cpp -o scope_lifetime_example
./scope_lifetime_example
```

## More Examples

- `example/main.cpp` is the primary runnable sample for this module.
- Try one variation: copy it to `example/variation.cpp`, change one rule, and compare outputs.

## Topics Covered

- Block scope (`{ ... }`).
- Variable shadowing.
- Local variable lifetime.
- Function parameter scope.

## Common Pitfalls

- Using variables outside their scope.
- Confusing shadowed variables with the original variable.
- Declaring variables too early and keeping them alive unnecessarily.

## Exercise Focus

- `exercises/01.cpp`: identify and fix a shadowing bug in grading logic.
- `exercises/02.cpp`: reduce variable lifetime and print clear scope boundaries.

### Exercise Specs

1. `exercises/01.cpp`
- Input: one exam score.
- Output: grade label (`A`, `B`, `C`, `D`, `F`).
- Edge cases: boundary scores like `90`, `80`, `70`, `60`.

2. `exercises/02.cpp`
- Input: an integer `N`.
- Output: sum of `1..N` with scoped helper blocks.
- Edge cases: `N <= 0`; `N = 1`.

## Checkpoint

- [ ] I can explain block scope with examples.
- [ ] I can detect and fix variable shadowing.
- [ ] I can limit variable lifetime to where it is needed.
- [ ] I completed both exercises.
