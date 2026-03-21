# Copy and Move Semantics (Python)

This module introduces copying behavior and transfer-style updates with mutable objects.

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

## Checkpoint

- [ ] I can explain aliasing vs copying for mutable objects.
- [ ] I can model safe transfer-style ownership changes.
- [ ] I can avoid unintentional shared-state mutations.
- [ ] I completed exercises/01.py.
- [ ] I completed exercises/02.py.
