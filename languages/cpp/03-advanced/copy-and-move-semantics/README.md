# Copy and Move Semantics

This module introduces value copying and ownership transfer through moves.

## Quick Run

```bash
g++ -std=c++17 -Wall -Wextra -pedantic example/main.cpp -o copy_move_example
./copy_move_example
```

## Topics Covered

- Copy constructor and copy assignment.
- Move constructor and move assignment.
- `std::move` semantics.
- Avoiding unnecessary copies.

## Common Pitfalls

- Using moved-from objects without reinitialization.
- Implementing custom resource types without rule-of-five awareness.
- Accidental copies in performance-sensitive paths.

## Exercise Focus

- `exercises/01.cpp`: resource-owning buffer with copy and move.
- `exercises/02.cpp`: vector insertion with move optimization.

### Exercise Specs

1. `exercises/01.cpp`
- Input: buffer size and values.
- Output: logs showing copy and move operations.
- Edge cases: zero-size buffer; self-assignment safety.

2. `exercises/02.cpp`
- Input: string values to store.
- Output: size/capacity growth while using move insertion.
- Edge cases: empty strings; repeated insertions.

## Checkpoint

- [ ] I can explain copy vs move behavior.
- [ ] I can use `std::move` intentionally.
- [ ] I understand moved-from object expectations.
- [ ] I completed both exercises.
