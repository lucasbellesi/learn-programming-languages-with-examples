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
```

## What To Check

- Polymorphic calls happen through base-class references.
- Shape implementations keep their own area logic.
- Generic helper works for both `list[int]` and `list[float]`.
