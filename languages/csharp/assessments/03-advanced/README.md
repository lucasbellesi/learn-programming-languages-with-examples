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
```

## What To Check

- Polymorphic calls happen through base-type references.
- No raw ownership patterns are needed.
- Generic helper works for both `List<int>` and `List<double>`.
