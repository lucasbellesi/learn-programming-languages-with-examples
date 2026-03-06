# Inheritance and Polymorphism

This module models behavior variation with virtual functions.

## Quick Run

```bash
g++ -std=c++17 -Wall -Wextra -pedantic example/main.cpp -o inheritance_polymorphism_example
./inheritance_polymorphism_example
```

## More Examples

- `example/polymorphic-menu.cpp`:

```bash
g++ -std=c++17 -Wall -Wextra -pedantic example/polymorphic-menu.cpp -o inheritance_polymorphic_menu
./inheritance_polymorphic_menu
```

## Topics Covered

- Base and derived classes.
- Virtual functions and override.
- Runtime polymorphism through base pointers/references.
- Abstract interfaces.

## Common Pitfalls

- Forgetting virtual destructors in polymorphic bases.
- Calling derived-only APIs through base interfaces.
- Object slicing with pass-by-value base types.

## Exercise Focus

- `exercises/01.cpp`: extend shape hierarchy with `Triangle`.
- `exercises/02.cpp`: aggregate shapes in `vector<unique_ptr<Shape>>`.

### Exercise Specs

1. `exercises/01.cpp`
- Input: triangle base and height.
- Output: computed area through overridden method.
- Edge cases: zero dimensions; decimal dimensions.

2. `exercises/02.cpp`
- Input: predefined shape objects.
- Output: total area through polymorphic iteration.
- Edge cases: empty shape list; mixed shape types.

## Checkpoint

- [ ] I can define abstract base classes with virtual methods.
- [ ] I can override behavior in derived classes.
- [ ] I can use polymorphic containers safely.
- [ ] I completed both exercises.
