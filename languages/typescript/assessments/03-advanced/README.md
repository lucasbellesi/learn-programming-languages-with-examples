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

## Learning Outcomes

- `ADV-MOD-01`
- `ADV-INV-02`
- `ADV-POL-01`
- `ADV-GEN-01`

## Quick Run

Run the checkpoint checker from the repository root. The starter is intentionally incomplete, so the first run establishes the work still to do:

~~~bash
python scripts/automation.py check-checkpoint --language typescript --kind assessment --level 03-advanced
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

## Check Your Work

Implement the task in `starter/`, then run from the repository root:

```bash
python scripts/automation.py check-checkpoint --language typescript --kind assessment --level 03-advanced
```

Use `--solution` only after completing a full attempt. Each failed case reports targeted feedback without exposing the implementation.

## What To Check

- polymorphism is exercised through the shared base type
- derived numeric summaries come from computed values rather than hardcoded text
- the generic helper works across more than one compatible input shape
