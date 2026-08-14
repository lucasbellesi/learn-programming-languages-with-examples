# Assessment 03: Advanced

## Goal

Combine class design, polymorphism, and templates in one practical program.

## Task

Write a program that:

1. Defines a polymorphic `Shape` hierarchy (`Circle`, `Rectangle`).
2. Stores shapes in `vector<unique_ptr<Shape>>`.
3. Calculates each shape area and total area.
4. Uses a template helper to print any numeric vector.
5. Prints min and max area values.

## Learning Metadata

- Difficulty: Intermediate.
- Estimated Time: 45-60 minutes.
- Prerequisites: All `03-advanced` modules, especially `structs-and-classes`, `inheritance-and-polymorphism`, and `templates-basics`.
- Learning Focus: Prove you can model abstractions, use reusable helpers, and summarize derived values correctly.

## Learning Outcomes

- `ADV-MOD-01`
- `ADV-INV-02`
- `ADV-POL-01`
- `ADV-GEN-01`

## Quick Run

Run the reference solution from the repository root:

```bash
python scripts/automation.py check-checkpoint --language cpp --kind assessment --level 03-advanced --solution
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

- This is the canonical advanced assessment for abstraction, polymorphism, and generic reuse in one program.
- Compared with the other tracks, it ties those ideas most directly to explicit ownership and compile-time templates.
- Use it as the baseline when comparing what advanced abstraction looks like in each language.

## Check Your Work

Implement the task in `starter/`, then run from the repository root:

```bash
python scripts/automation.py check-checkpoint --language cpp --kind assessment --level 03-advanced
```

Use `--solution` only after completing a full attempt. Each failed case reports targeted feedback without exposing the implementation.

## What To Check

- abstraction or polymorphism is exercised through the language-appropriate shared interface
- derived numeric summaries come from computed values rather than hardcoded text
- the reusable helper works across more than one compatible input shape
