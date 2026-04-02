# Copy and Move Semantics

This module introduces value copying and ownership transfer through moves.

## Learning Metadata

- Difficulty: Intermediate.
- Estimated Time: 35-50 minutes.
- Prerequisites: `03-advanced/structs-and-classes`, `03-advanced/constructors-and-invariants`.
- Cross-Language Lens: Use this module to contrast C++ ownership transfer with reference-heavy behavior in C#, Go, and Python.

## Quick Run

```bash
g++ -std=c++17 -Wall -Wextra -pedantic example/main.cpp -o copy_move_example
./copy_move_example
```

## More Examples

- `example/main.cpp` is the primary runnable sample for this module.
- Try one variation: copy it to `example/variation.cpp`, change one rule, and compare outputs.

## Topics Covered

- Copy constructor and copy assignment.
- Move constructor and move assignment.
- `std::move` semantics.
- Avoiding unnecessary copies.

## Common Pitfalls

- Using moved-from objects without reinitialization.
- Implementing custom resource types without rule-of-five awareness.
- Accidental copies in performance-sensitive paths.

## Cross-Language Notes

- C++ is the canonical version: copy and move are real language-level semantics with direct performance and ownership consequences.
- Other tracks adapt this topic because most of them do not have true move semantics in the same sense.
- Use this module as the anchor for every later comparison about aliasing and transfer.

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
