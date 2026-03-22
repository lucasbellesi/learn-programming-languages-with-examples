# Templates Basics (Python)

This module introduces generic programming with type hints and reusable classes.

## Quick Run

~~~bash
python example/main.py
~~~

## Topics Covered

- Generic functions through type variables.
- Generic classes with reusable element types.
- Type-independent logic with consistent interfaces.
- When type hints clarify constraints even in a dynamic language.

## Common Pitfalls

- Assuming type hints enforce runtime behavior by themselves.
- Replacing clear generic APIs with `Any` too early.
- Ignoring value constraints when writing supposedly reusable code.

## Exercise Focus

- exercises/01.py: generic swap function.
- exercises/02.py: generic average over numeric lists.

### Exercise Specs

1. exercises/01.py
- Input: two values of the same type.
- Output: values before and after swap.
- Edge cases: identical values; negative numbers.

2. exercises/02.py
- Input: numeric sequence.
- Output: arithmetic average.
- Edge cases: empty list should return `0`; mixed positive/negative values.

## Checkpoint

- [ ] I can write and call generic helper functions with type variables.
- [ ] I can create simple generic classes.
- [ ] I can identify where type hints help clarify generic code.
- [ ] I completed exercises/01.py.
- [ ] I completed exercises/02.py.
