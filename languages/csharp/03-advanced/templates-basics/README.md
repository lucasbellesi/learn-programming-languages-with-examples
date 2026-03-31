# Templates Basics (C#)

This module introduces generic programming with methods and classes.

## Learning Metadata

- Difficulty: Intermediate.
- Estimated Time: 35-50 minutes.
- Prerequisites: `01-foundations/functions`, `03-advanced/structs-and-classes`.
- Cross-Language Lens: Compare C++ templates with C# generics, Go type parameters, and Python's runtime flexibility.

## Quick Run

~~~bash
dotnet run --project example/templates-basics-example.csproj
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

## Checkpoint

- [ ] I can write and call generic methods.
- [ ] I can create simple generic classes.
- [ ] I can identify where generic constraints are required.
- [ ] I completed exercises/01.cs.
- [ ] I completed exercises/02.cs.
