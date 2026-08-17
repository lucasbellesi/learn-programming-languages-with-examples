# Generics Basics (C#)

This module introduces generic programming with methods and classes.

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
python scripts/automation.py run-module --module-path languages/csharp/03-advanced/templates-basics
~~~

## Topics Covered

- Generic methods with type constraints.
- Generic classes for reusable containers.
- Type-independent logic with `T`.
- When constraints are required for comparisons and arithmetic-like behavior.

## Common Pitfalls

- Assuming all generic types support comparison automatically.
- Using `object` instead of generics and losing type safety.
- Hiding constraints until compile errors become confusing.

## Cross-Language Notes

- In C#, read this module through the native focus ?Generics Basics?; the shared folder name remains stable for side-by-side navigation.
- Use static types, .NET collections, and managed-resource patterns to demonstrate how to express reusable type-safe behavior with language generics.
- Compare observable behavior with the other tracks when learning to apply constraints when an operation requires specific capabilities; equivalent evidence matters more than identical syntax.

## Exercise Focus

- exercises/01.cs: generic swap function.
- exercises/02.cs: generic average over numeric lists.

### Exercise Specs

1. exercises/01.cs
- Input: two values of the same type.
- Output: values before and after swap.
- Edge cases: identical values; negative numbers.

2. exercises/02.cs
- Input: numeric sequence.
- Output: arithmetic average.
- Edge cases: empty list should return `0`; mixed positive/negative values.

## Check Your Work

Run from the repository root after implementing a starter:

```bash
python scripts/automation.py check-exercise --language csharp --level 03-advanced --module templates-basics --exercise 01
```

Change `--exercise 01` to `--exercise 02` for the second task. Consult `exercises/solutions/` only after making a complete attempt.

## Checkpoint

- [ ] I can write and call generic methods.
- [ ] I can create simple generic classes.
- [ ] I can identify where generic constraints are required.
- [ ] I completed exercises/01.cs.
- [ ] I completed exercises/02.cs.
