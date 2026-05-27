# Structs and Classes (Java)

This module introduces object modeling with records and classes.

## Learning Metadata

- Difficulty: Intermediate.
- Estimated Time: 35-50 minutes.
- Prerequisites: `01-foundations/functions`, `01-foundations/scope-and-lifetime-basics`, and `02-core/input-validation`.
- Cross-Language Lens: Compare Java records and classes with structs, dataclasses, interfaces, and class-style patterns in the other tracks.

## Quick Run

~~~bash
javac -d build/java languages/java/03-advanced/structs-and-classes/example/Main.java
java -cp build/java Main
~~~

## Topics Covered

- Lightweight value modeling with `record`.
- Stateful behavior using classes and private fields.
- Constructor cleanup to preserve valid object state.
- Method-based updates for controlled mutations.

## Common Pitfalls

- Using public mutable fields when methods should protect object state.
- Letting invalid constructor inputs propagate through the object lifecycle.
- Choosing a full class when a record would communicate immutable data more clearly.

## Exercise Focus

- exercises/Exercise01.java: model a rectangle using a class with methods.
- exercises/Exercise02.java: build an encapsulated `Counter` class with commands.

### Exercise Specs

1. exercises/Exercise01.java
- Input: width and height.
- Output: area and perimeter.
- Edge cases: non-positive dimensions should stop with a message; decimal values should work.

2. exercises/Exercise02.java
- Input: sequence of commands (`inc`, `dec`, `reset`, `stop`).
- Output: counter value updates and final value.
- Edge cases: unknown commands; immediate `stop`.

## Checkpoint

- [ ] I can explain when `record` is enough and when a class with methods is better.
- [ ] I can enforce simple invariants in constructors.
- [ ] I can keep state updates inside well-named methods.
- [ ] I completed exercises/Exercise01.java.
- [ ] I completed exercises/Exercise02.java.
