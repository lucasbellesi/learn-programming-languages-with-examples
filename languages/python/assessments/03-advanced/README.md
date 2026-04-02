# Assessment 03: Advanced

## Goal

Combine class design, polymorphism, and generics-style type hints in one practical program.

## Task

Write a program that:

1. Defines a polymorphic `Shape` hierarchy (`Circle`, `Rectangle`).
2. Stores shapes in a list of base-class references.
3. Calculates each shape area and total area.
4. Uses a generic helper to print any numeric list.
5. Prints min and max area values.

## Learning Metadata

- Difficulty: Intermediate.
- Estimated Time: 45-60 minutes.
- Prerequisites: All `03-advanced` modules, especially `structs-and-classes`, `inheritance-and-polymorphism`, and `templates-basics`.
- Learning Focus: Prove you can model abstractions, use reusable helpers, and summarize derived values correctly.

## Quick Run

```bash
python main.py
```

## Expected Output (shape)

```text
Shape areas:
- Circle: ...
- Rectangle: ...
Total area: ...
Minimum area: ...
Maximum area: ...
Sample counts: [...]
Computed areas: [...]
```
## Cross-Language Notes

- Compared with the C++ assessment, this version preserves the same abstraction goal with much lighter syntax and weaker compile-time enforcement.
- Relative to C#, Go, and TypeScript, the shared contract is carried more by design intent than by the type system.
- The comparison to watch is expressive modeling versus static guarantees.

## What To Check

- abstraction or polymorphism is exercised through the language-appropriate shared interface
- derived numeric summaries come from computed values rather than hardcoded text
- the reusable helper works across more than one compatible input shape
