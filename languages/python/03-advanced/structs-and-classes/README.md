# Structs and Classes (Python)

This module introduces object modeling with dataclass-style structures and classes.

## Quick Run

~~~bash
python example/main.py
~~~

## Topics Covered

- Lightweight value modeling with `@dataclass`.
- Stateful behavior using classes and private-by-convention fields.
- Constructor guards to preserve valid object state.
- Method-based updates for controlled mutations.

## Common Pitfalls

- Placing mutable shared defaults directly on class definitions.
- Letting invalid constructor inputs propagate through the object lifecycle.
- Updating internal state from outside helper methods.

## Exercise Focus

- exercises/01.py: model a rectangle using a class with methods.
- exercises/02.py: build an encapsulated `Counter` class with commands.

### Exercise Specs

1. exercises/01.py
- Input: width and height.
- Output: area and perimeter.
- Edge cases: non-positive dimensions should stop with a message; decimal values should work.

2. exercises/02.py
- Input: sequence of commands (`inc`, `dec`, `reset`, `stop`).
- Output: counter value updates and final value.
- Edge cases: unknown commands; immediate `stop`.

## Checkpoint

- [ ] I can explain when `@dataclass` is enough and when a class with methods is better.
- [ ] I can enforce simple invariants in constructors.
- [ ] I can keep state updates inside well-named methods.
- [ ] I completed exercises/01.py.
- [ ] I completed exercises/02.py.
