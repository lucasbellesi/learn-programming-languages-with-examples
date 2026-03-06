# Algorithms Basics

This module introduces essential algorithmic patterns using loops and vectors.

## Why It Matters

Many programming problems reduce to a few patterns: search, count, and min/max scanning.

## Quick Run

```bash
g++ -std=c++17 -Wall -Wextra -pedantic example/main.cpp -o algorithms_basics_example
./algorithms_basics_example
```

On Windows (MSYS2 shell), run:

```bash
./algorithms_basics_example.exe
```

## Topics Covered

### Linear Search

Find the first position of a target by scanning from left to right.

### Counting Pattern

Count how many values match a condition (for example, equal to a target).

### Min/Max Scan

Track smallest and largest values while iterating once through data.

## Common Pitfalls

- Forgetting to handle empty input.
- Using uninitialized `min`/`max` values.
- Doing extra loops when one pass is enough.

## Exercise Focus

- `exercises/01.cpp`: implement linear search over user-provided values.
- `exercises/02.cpp`: compute min, max, and count of even numbers in one pass.

## Checkpoint

- [ ] I can implement linear search.
- [ ] I can count values matching a condition.
- [ ] I can compute min and max safely.
- [ ] I completed both exercises.
