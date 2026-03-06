# Modularization and Build Structure

This module introduces basic multi-file organization principles.

## Quick Run

```bash
g++ -std=c++17 -Wall -Wextra -pedantic example/main.cpp -o modularization_example
./modularization_example
```

## Topics Covered

- Splitting responsibilities by feature.
- Header declarations vs source definitions.
- Include guards / `#pragma once` concept.
- Reusable utility interfaces.

## Common Pitfalls

- Placing function definitions in multiple translation units.
- Circular includes.
- Missing declarations for used symbols.

## Exercise Focus

- `exercises/01.cpp`: refactor procedural code into module-like sections.
- `exercises/02.cpp`: build reusable utility functions for two callers.

### Exercise Specs

1. `exercises/01.cpp`
- Input: sample values.
- Output: calculations via separated helper functions.
- Edge cases: division by zero checks.

2. `exercises/02.cpp`
- Input: command choice and numbers.
- Output: reused utility operation results.
- Edge cases: unsupported command; negative values.

## Checkpoint

- [ ] I can separate interfaces from implementation responsibilities.
- [ ] I can design reusable helper utilities.
- [ ] I can explain how multi-file builds are assembled.
- [ ] I completed both exercises.
