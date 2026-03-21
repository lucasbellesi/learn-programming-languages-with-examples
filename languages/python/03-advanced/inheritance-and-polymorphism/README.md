# Inheritance and Polymorphism (Python)

This module models behavior variation with abstract base classes and overrides.

## Quick Run

~~~bash
python example/main.py
~~~

## Topics Covered

- Abstract base classes and required methods.
- Runtime polymorphism through shared base references.
- Overriding concrete behavior in subclasses.
- Aggregating mixed implementations in one list.

## Common Pitfalls

- Forgetting to implement required abstract methods.
- Accessing subclass-only state from generic iteration code.
- Replacing polymorphism with `if type(...)` checks.

## Exercise Focus

- exercises/01.py: extend shape model with `Triangle`.
- exercises/02.py: aggregate shapes in `list[Shape]`.

### Exercise Specs

1. exercises/01.py
- Input: triangle base and height.
- Output: computed area through overridden method.
- Edge cases: zero dimensions; decimal dimensions.

2. exercises/02.py
- Input: predefined shape objects.
- Output: total area through polymorphic iteration.
- Edge cases: empty shape list; mixed shape types.

## Checkpoint

- [ ] I can define abstract base classes with polymorphic methods.
- [ ] I can override behavior in derived classes.
- [ ] I can use polymorphic collections safely.
- [ ] I completed exercises/01.py.
- [ ] I completed exercises/02.py.
