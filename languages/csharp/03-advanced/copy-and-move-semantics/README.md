# Reference Copies and Ownership Conventions (C#)

This module introduces copying behavior and transfer-style updates with reference types.

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
python scripts/automation.py run-module --module-path languages/csharp/03-advanced/copy-and-move-semantics
~~~

## Topics Covered

- Difference between copying references and copying object data.
- Explicit transfer of ownership-like responsibilities between objects.
- Designing safe clone methods for deep copies.
- Avoiding accidental shared-mutable-state bugs.

## Common Pitfalls

- Assuming assignment duplicates object contents for classes.
- Mutating data through one reference and surprising another caller.
- Forgetting to clear or invalidate source state after transfer operations.

## Cross-Language Notes

- C# keeps the comparison close to C++ conceptually, but the runtime turns many ownership questions into reference-versus-copy decisions instead of move semantics.
- Compared with Go, Python, and TypeScript, the object model still makes it natural to discuss explicit clone patterns.
- The important comparison is when copying is value-like and when references keep sharing the same state.

## Exercise Focus

- exercises/01.cs: resource-like buffer with clone and transfer operations.
- exercises/02.cs: list insertion flow that shows shared vs copied values.

### Exercise Specs

1. exercises/01.cs
- Input: buffer size and values.
- Output: logs showing clone and transfer behavior.
- Edge cases: zero-size buffer; transferred source becomes empty.

2. exercises/02.cs
- Input: text values to store.
- Output: size and content checks after copy vs shared assignment.
- Edge cases: empty strings; repeated insertions.

## Check Your Work

Run from the repository root after implementing a starter:

```bash
python scripts/automation.py check-exercise --language csharp --level 03-advanced --module copy-and-move-semantics --exercise 01
```

Change `--exercise 01` to `--exercise 02` for the second task. Consult `exercises/solutions/` only after making a complete attempt.

## Checkpoint

- [ ] I can explain reference copy vs deep copy.
- [ ] I can model safe transfer-style ownership changes.
- [ ] I can avoid unintentional shared-state mutations.
- [ ] I completed exercises/01.cs.
- [ ] I completed exercises/02.cs.
