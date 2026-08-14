# Inheritance and Polymorphism

This module models behavior variation with virtual functions.

## Learning Metadata

- Difficulty: Intermediate.
- Estimated Time: 35-50 minutes.
- Prerequisites: `03-advanced/structs-and-classes`, `03-advanced/constructors-and-invariants`.
- Cross-Language Lens: Compare virtual dispatch, interfaces, and duck-typed behavior to see how polymorphism changes by language.

## Learning Outcomes

- `ADV-POL-01`: Program against a shared behavioral abstraction.
- `ADV-POL-02`: Use dynamic dispatch without unsafe type assumptions.

## Quick Run

Run from the repository root:

~~~bash
python scripts/automation.py run-module --module-path languages/cpp/03-advanced/inheritance-and-polymorphism
~~~

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

## Cross-Language Notes

- C++ is the baseline for virtual dispatch, abstract interfaces, and explicit ownership of polymorphic objects.
- Other tracks keep the same idea of common behavior through a shared contract, but often reduce the amount of machinery required.
- The comparison to watch is how each language balances power, safety, and ceremony in polymorphic design.

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

## Check Your Work

Run from the repository root after implementing a starter:

```bash
python scripts/automation.py check-exercise --language cpp --level 03-advanced --module inheritance-and-polymorphism --exercise 01
```

Change `--exercise 01` to `--exercise 02` for the second task. Consult `exercises/solutions/` only after making a complete attempt.

## Checkpoint

- [ ] I can define abstract base classes with virtual methods.
- [ ] I can override behavior in derived classes.
- [ ] I can use polymorphic containers safely.
- [ ] I completed both exercises.
