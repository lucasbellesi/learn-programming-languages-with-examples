# Type Parameters and Constraints (Go)

This module introduces generic programming with type parameters.

## Learning Metadata

- Difficulty: Intermediate.
- Estimated Time: 35-50 minutes.
- Prerequisites: `01-foundations/functions`, `03-advanced/structs-and-classes`.
- Cross-Language Lens: Compare C++ templates with C# generics, Go type parameters, and Python's runtime flexibility.

## Learning Outcomes

- `ADV-GEN-01`: Express reusable type-safe behavior with language generics.
- `ADV-GEN-02`: Apply constraints when an operation requires specific capabilities.

## Quick Run

Run from the repository root:

~~~bash
python scripts/automation.py run-module --module-path languages/go/03-advanced/templates-basics
~~~

## Topics Covered

- Generic functions with type constraints.
- Generic structs with reusable field types.
- Type-independent algorithms using type parameters.
- When ordered or numeric constraints are required.

## Common Pitfalls

- Assuming every type supports comparison or addition.
- Replacing type parameters with `interface{}` and losing type safety.
- Overcomplicating small examples that do not need generics.

## Cross-Language Notes

- In Go, read this module through the native focus ?Type Parameters and Constraints?; the shared folder name remains stable for side-by-side navigation.
- Use explicit errors, slices/maps, interfaces, and defer to demonstrate how to express reusable type-safe behavior with language generics.
- Compare observable behavior with the other tracks when learning to apply constraints when an operation requires specific capabilities; equivalent evidence matters more than identical syntax.

## Exercise Focus

- exercises/01.go: generic swap function.
- exercises/02.go: generic average over numeric slices.

### Exercise Specs

1. exercises/01.go
- Input: two values of the same type.
- Output: values before and after swap.
- Edge cases: identical values; negative numbers.

2. exercises/02.go
- Input: numeric sequence.
- Output: arithmetic average.
- Edge cases: empty slice should return `0`; mixed positive/negative values.

## Check Your Work

Run from the repository root after implementing a starter:

```bash
python scripts/automation.py check-exercise --language go --level 03-advanced --module templates-basics --exercise 01
```

Change `--exercise 01` to `--exercise 02` for the second task. Consult `exercises/solutions/` only after making a complete attempt.

## Checkpoint

- [ ] I can write and call generic functions.
- [ ] I can create simple generic structs.
- [ ] I can identify where constraints are required.
- [ ] I completed exercises/01.go.
- [ ] I completed exercises/02.go.
