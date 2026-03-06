# Structs and Classes

This module introduces object modeling with `struct` and `class`.

## Quick Run

```bash
g++ -std=c++17 -Wall -Wextra -pedantic example/main.cpp -o structs_and_classes_example
./structs_and_classes_example
```

## More Examples

- `example/class-with-validation.cpp`:

```bash
g++ -std=c++17 -Wall -Wextra -pedantic example/class-with-validation.cpp -o structs_class_with_validation
./structs_class_with_validation
```

## Topics Covered

- Default access: `struct` public, `class` private.
- Constructors for initialization.
- Encapsulation with private fields and public methods.
- `const` member functions.

## Common Pitfalls

- Exposing mutable state publicly without reason.
- Forgetting to validate constructor inputs.
- Missing `const` on read-only methods.

## Exercise Focus

- `exercises/01.cpp`: model rectangle using `struct` and methods.
- `exercises/02.cpp`: create encapsulated `Counter` class.

### Exercise Specs

1. `exercises/01.cpp`
- Input: width and height.
- Output: area and perimeter.
- Edge cases: non-positive dimensions should stop with message; decimal values should work.

2. `exercises/02.cpp`
- Input: sequence of commands (`inc`, `dec`, `reset`, `stop`).
- Output: counter value updates and final value.
- Edge cases: unknown commands; immediate `stop`.

## Checkpoint

- [ ] I can explain `struct` vs `class`.
- [ ] I can initialize objects with constructors.
- [ ] I can protect state through methods.
- [ ] I completed both exercises.
