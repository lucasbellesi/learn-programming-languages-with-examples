# Structs and Classes (Go)

This module introduces object modeling with `struct` and methods.

## Learning Metadata

- Difficulty: Intermediate.
- Estimated Time: 35-50 minutes.
- Prerequisites: `01-foundations/functions`, `01-foundations/scope-and-lifetime-basics`.
- Cross-Language Lens: Compare lightweight records, full classes, and method receivers to see how each language models data plus behavior.

## Learning Outcomes

- `ADV-MOD-01`: Model data and behavior with cohesive domain types.
- `ADV-MOD-02`: Protect invariants through constructors and methods.

## Quick Run

Run from the repository root:

~~~bash
python scripts/automation.py run-module --module-path languages/go/03-advanced/structs-and-classes
~~~

## Topics Covered

- Modeling data with `struct` values.
- Pointer receiver methods for controlled state updates.
- Constructor-style helper functions with guard logic.
- Keeping state changes inside methods.

## Common Pitfalls

- Mutating shared state without clear method boundaries.
- Skipping constructor guards for invalid initial values.
- Mixing value and pointer receivers without intent.

## Cross-Language Notes

- In Go, read this module through the native focus ?Structs and Classes?; the shared folder name remains stable for side-by-side navigation.
- Use explicit errors, slices/maps, interfaces, and defer to demonstrate how to model data and behavior with cohesive domain types.
- Compare observable behavior with the other tracks when learning to protect invariants through constructors and methods; equivalent evidence matters more than identical syntax.

## Exercise Focus

- exercises/01.go: model a rectangle using a `struct` and methods.
- exercises/02.go: build an encapsulated `Counter` type with commands.

### Exercise Specs

1. exercises/01.go
- Input: width and height.
- Output: area and perimeter.
- Edge cases: non-positive dimensions should stop with a message; decimal values should work.

2. exercises/02.go
- Input: sequence of commands (`inc`, `dec`, `reset`, `stop`).
- Output: counter value updates and final value.
- Edge cases: unknown commands; immediate `stop`.

## Check Your Work

Run from the repository root after implementing a starter:

```bash
python scripts/automation.py check-exercise --language go --level 03-advanced --module structs-and-classes --exercise 01
```

Change `--exercise 01` to `--exercise 02` for the second task. Consult `exercises/solutions/` only after making a complete attempt.

## Checkpoint

- [ ] I can explain struct fields and method receivers.
- [ ] I can model invariants with constructor-style functions and guards.
- [ ] I can isolate state changes behind methods.
- [ ] I completed exercises/01.go.
- [ ] I completed exercises/02.go.
