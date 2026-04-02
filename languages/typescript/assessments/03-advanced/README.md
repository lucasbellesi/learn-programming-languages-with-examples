# Assessment 03: Advanced

## Goal

Combine class design, polymorphism, and generics in one practical TypeScript program.

## Task

Write a program that:

1. Defines a polymorphic `Shape` hierarchy (`Circle`, `Rectangle`).
2. Stores shapes in an array of base-type references.
3. Calculates each shape area and total area.
4. Uses a generic helper to print any list.
5. Prints minimum and maximum area values.

## Learning Metadata

- Difficulty: Advanced.
- Estimated Time: 45-60 minutes.
- Prerequisites: All `03-advanced` modules, especially `structs-and-classes`, `inheritance-and-polymorphism`, and `templates-basics`.
- Learning Focus: Prove you can model abstractions, use reusable helpers, and summarize derived values correctly.

## Quick Run

~~~bash
npm run build:typescript
node build/typescript/assessments/03-advanced/main.js
~~~

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

- Compared with the C++ assessment, this version maps the same advanced abstraction challenge onto classes plus structural typing and generics.
- Relative to Python, more of the shared contract is visible before runtime; relative to C#, less is tied to a strictly nominal class system.
- The useful comparison is how a typed JavaScript language balances flexibility and abstraction discipline.

## What To Check

- polymorphism is exercised through the shared base type
- derived numeric summaries come from computed values rather than hardcoded text
- the generic helper works across more than one compatible input shape
