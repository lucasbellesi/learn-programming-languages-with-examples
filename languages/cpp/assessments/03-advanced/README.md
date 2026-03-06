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

## Quick Run

```bash
g++ -std=c++17 -Wall -Wextra -pedantic main.cpp -o assessment_03_advanced
./assessment_03_advanced
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

- Polymorphic calls happen through base pointers.
- No raw owning pointers are used.
- Template helper works for both `vector<int>` and `vector<double>`.
