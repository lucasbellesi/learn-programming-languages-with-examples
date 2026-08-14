# Copy and Move Semantics (Python)

This module introduces copying behavior and transfer-style updates with mutable objects.

## Learning Metadata

- Difficulty: Intermediate.
- Estimated Time: 35-50 minutes.
- Prerequisites: `03-advanced/structs-and-classes`, `03-advanced/constructors-and-invariants`.
- Cross-Language Lens: Use this module to contrast C++ ownership transfer with reference-heavy behavior in C#, Go, and Python.

## Learning Outcomes

- `ADV-CPY-01`: Predict aliasing and independence after copying or sharing values.
- `ADV-CPY-02`: Choose an idiomatic ownership-transfer strategy for the language.

## Quick Run

~~~bash
python example/main.py
~~~

## Topics Covered

- Assignment aliasing vs explicit shallow/deep copies.
- Transfer-style state handoff between objects.
- Clone helpers for predictable object independence.
- Avoiding accidental shared-mutable-state bugs.

## Common Pitfalls

- Assuming `=` duplicates list contents.
- Mutating data through one name and surprising another caller.
- Forgetting to clear source state after transfer operations.

## Cross-Language Notes

- Python adapts the topic through aliasing, shallow copies, deep copies, and mutation boundaries rather than move semantics.
- Compared with C++ or Go, ownership is much less encoded in syntax and much more visible in object identity and shared state.
- The core comparison is accidental sharing versus deliberate copying.

## Exercise Focus

- exercises/01.py: resource-like buffer with clone and transfer operations.
- exercises/02.py: insertion flow that contrasts aliasing and copied lists.

### Exercise Specs

1. exercises/01.py
- Input: buffer size and values.
- Output: logs showing clone and transfer behavior.
- Edge cases: zero-size buffer; repeated transfers.

2. exercises/02.py
- Input: text values to store.
- Output: size and content checks after aliasing vs copying.
- Edge cases: empty strings; repeated insertions.

## Check Your Work

Run from the repository root after implementing a starter:

```bash
python scripts/automation.py check-exercise --language python --level 03-advanced --module copy-and-move-semantics --exercise 01
```

Change `--exercise 01` to `--exercise 02` for the second task. Consult `exercises/solutions/` only after making a complete attempt.

## Checkpoint

- [ ] I can explain aliasing vs copying for mutable objects.
- [ ] I can model safe transfer-style ownership changes.
- [ ] I can avoid unintentional shared-state mutations.
- [ ] I completed exercises/01.py.
- [ ] I completed exercises/02.py.
