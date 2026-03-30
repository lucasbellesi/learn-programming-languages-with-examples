# Assessment 03: Advanced

## Goal

Combine struct design, interfaces, and generics in one practical program.

## Task

Write a program that:

1. Defines a polymorphic `Shape` interface with `Circle` and `Rectangle`.
2. Stores shapes in a slice of interface values.
3. Calculates each shape area and total area.
4. Uses a generic helper to print any numeric slice.
5. Prints min and max area values.

## Quick Run

```bash
go run main.go
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

- Dynamic dispatch happens through the interface slice.
- Shape implementations stay focused on their own area logic.
- Generic helper works for both `[]int` and `[]float64`.
