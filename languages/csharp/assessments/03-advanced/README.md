# Assessment 03: Advanced

## Goal

Combine class design, polymorphism, and generics in one practical program.

## Task

Write a program that:

1. Defines a polymorphic `Shape` hierarchy (`Circle`, `Rectangle`).
2. Stores shapes in `List<Shape>`.
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
dotnet run --project assessment-03-advanced.csproj
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

- Compared with the C++ assessment, this version keeps the same abstraction target with a smoother managed object model and generics.
- Relative to Go and TypeScript, class-based polymorphism stays the most direct here.
- The useful comparison is advanced design with less ownership ceremony but similar conceptual weight.

## What To Check

- abstraction or polymorphism is exercised through the language-appropriate shared interface
- derived numeric summaries come from computed values rather than hardcoded text
- the reusable helper works across more than one compatible input shape
