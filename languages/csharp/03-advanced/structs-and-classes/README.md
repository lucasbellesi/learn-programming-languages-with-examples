# Structs and Classes (C#)

This module introduces object modeling with `struct` and `class`.

## Learning Metadata

- Difficulty: Intermediate.
- Estimated Time: 35-50 minutes.
- Prerequisites: `01-foundations/functions`, `01-foundations/scope-and-lifetime-basics`.
- Cross-Language Lens: Compare lightweight records, full classes, and method receivers to see how each language models data plus behavior.

## Quick Run

~~~bash
dotnet run --project example/structs-and-classes-example.csproj
~~~

## Topics Covered

- Modeling simple immutable values with `struct`.
- Modeling stateful behavior with `class` and private fields.
- Constructor guards to enforce valid initial state.
- Instance methods that preserve object invariants.

## Common Pitfalls

- Using mutable structs for shared state.
- Exposing class fields directly instead of validating through methods.
- Accepting invalid constructor values and fixing bugs later.

## Exercise Focus

- exercises/01.cs: model a rectangle using `struct` and methods.
- exercises/02.cs: build an encapsulated `Counter` class with commands.

### Exercise Specs

1. exercises/01.cs
- Input: width and height.
- Output: area and perimeter.
- Edge cases: non-positive dimensions should stop with a message; decimal values should work.

2. exercises/02.cs
- Input: sequence of commands (`inc`, `dec`, `reset`, `stop`).
- Output: counter value updates and final value.
- Edge cases: unknown commands; immediate `stop`.

## Checkpoint

- [ ] I can explain value type (`struct`) vs reference type (`class`) basics.
- [ ] I can model invariants with constructors and method guards.
- [ ] I can choose where mutable state should live.
- [ ] I completed exercises/01.cs.
- [ ] I completed exercises/02.cs.
