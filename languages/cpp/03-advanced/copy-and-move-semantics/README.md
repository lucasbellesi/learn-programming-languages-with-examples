# Copy and Move Semantics (C++)

This module introduces value copying and ownership transfer through moves.

## Learning Metadata

- Difficulty: Intermediate.
- Estimated Time: 35-50 minutes.
- Prerequisites: `03-advanced/structs-and-classes`, `03-advanced/constructors-and-invariants`.
- Cross-Language Lens: Use this module to contrast C++ ownership transfer with reference-heavy behavior in C#, Go, and Python.

## Learning Outcomes

- `ADV-CPY-01`: Predict aliasing and independence after copying or sharing values.
- `ADV-CPY-02`: Choose an idiomatic ownership-transfer strategy for the language.

## Quick Run

Run from the repository root:

~~~bash
python scripts/automation.py run-module --module-path languages/cpp/03-advanced/copy-and-move-semantics
~~~

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

## Check Your Work

Run from the repository root after implementing a starter:

```bash
python scripts/automation.py check-exercise --language cpp --level 03-advanced --module copy-and-move-semantics --exercise 01
```

Change `--exercise 01` to `--exercise 02` for the second task. Consult `exercises/solutions/` only after making a complete attempt.

## Checkpoint

- [ ] I can explain copy vs move behavior.
- [ ] I can use `std::move` intentionally.
- [ ] I understand moved-from object expectations.
- [ ] I completed both exercises.
