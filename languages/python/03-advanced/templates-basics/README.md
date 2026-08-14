# Templates Basics (Python)

This module introduces generic programming with type hints and reusable classes.

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
python scripts/automation.py run-module --module-path languages/python/03-advanced/templates-basics
~~~

## Topics Covered

- Generic functions through type variables.
- Generic classes with reusable element types.
- Type-independent logic with consistent interfaces.
- When type hints clarify constraints even in a dynamic language.

## Common Pitfalls

- Assuming type hints enforce runtime behavior by themselves.
- Replacing clear generic APIs with `Any` too early.
- Ignoring value constraints when writing supposedly reusable code.

## Cross-Language Notes

- Compared with C++, this concept broadens from templates into each language's own reusable generic abstraction model.
- Relative to Go and C#, TypeScript generics stay expressive without runtime specialization, while Python treats the same idea more informally.
- The useful comparison is how each language generalizes logic without abandoning type clarity.

## Exercise Focus

- exercises/01.py: generic swap function.
- exercises/02.py: generic average over numeric lists.

### Exercise Specs

1. exercises/01.py
- Input: two values of the same type.
- Output: values before and after swap.
- Edge cases: identical values; negative numbers.

2. exercises/02.py
- Input: numeric sequence.
- Output: arithmetic average.
- Edge cases: empty list should return `0`; mixed positive/negative values.

## Check Your Work

Run from the repository root after implementing a starter:

```bash
python scripts/automation.py check-exercise --language python --level 03-advanced --module templates-basics --exercise 01
```

Change `--exercise 01` to `--exercise 02` for the second task. Consult `exercises/solutions/` only after making a complete attempt.

## Checkpoint

- [ ] I can write and call generic helper functions with type variables.
- [ ] I can create simple generic classes.
- [ ] I can identify where type hints help clarify generic code.
- [ ] I completed exercises/01.py.
- [ ] I completed exercises/02.py.
