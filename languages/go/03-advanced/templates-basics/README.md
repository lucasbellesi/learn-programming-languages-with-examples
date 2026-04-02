# Templates Basics (Go)

This module introduces generic programming with type parameters.

## Learning Metadata

- Difficulty: Intermediate.
- Estimated Time: 35-50 minutes.
- Prerequisites: `01-foundations/functions`, `03-advanced/structs-and-classes`.
- Cross-Language Lens: Compare C++ templates with C# generics, Go type parameters, and Python's runtime flexibility.

## Quick Run

~~~bash
go run example/main.go
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

- Compared with C++, this concept broadens from templates into each language's own reusable generic abstraction model.
- Relative to Go and C#, TypeScript generics stay expressive without runtime specialization, while Python treats the same idea more informally.
- The useful comparison is how each language generalizes logic without abandoning type clarity.

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

## Checkpoint

- [ ] I can write and call generic functions.
- [ ] I can create simple generic structs.
- [ ] I can identify where constraints are required.
- [ ] I completed exercises/01.go.
- [ ] I completed exercises/02.go.
