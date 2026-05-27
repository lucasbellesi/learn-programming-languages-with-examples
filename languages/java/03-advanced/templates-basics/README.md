# Generics Basics (Java)

This module introduces reusable Java code with generic methods and generic classes.

## Learning Metadata

- Difficulty: Intermediate.
- Estimated Time: 35-50 minutes.
- Prerequisites: `01-foundations/functions`, `02-core/arrays-and-vectors`, `03-advanced/structs-and-classes`.
- Cross-Language Lens: Compare Java generics with C++ templates, C# generics, Go type parameters, Python's runtime flexibility, and TypeScript generics.

## Quick Run

~~~bash
javac -d build/java languages/java/03-advanced/templates-basics/example/Main.java
java -cp build/java Main
~~~

## Topics Covered

- Generic methods.
- Generic classes.
- Bounded type parameters with `extends`.
- Reusing algorithms without giving up compile-time type checks.

## Common Pitfalls

- Expecting Java generics to create separate runtime classes for each type.
- Forgetting that primitive types need wrapper types such as `Integer` and `Double`.
- Calling operations that the generic type bound does not guarantee.
- Using raw types instead of parameterized types.

## Cross-Language Notes

- Java generics are type checked at compile time and use type erasure at runtime.
- Compared with C++ templates, Java generics are less specialized but usually simpler for beginners.
- Compared with Python, Java asks for more type annotations but catches more generic misuse before execution.
- Compared with TypeScript, Java generics run on the JVM and do not depend on structural typing.

## Exercise Focus

- exercises/Exercise01.java: implement and swap a generic `Pair<T>`.
- exercises/Exercise02.java: compute an average from a generic list of numeric values.

### Exercise Specs

1. exercises/Exercise01.java
- Input: two words.
- Output: pair before and after swapping.
- Edge cases: identical words; words with different lengths.

2. exercises/Exercise02.java
- Input: count followed by decimal values.
- Output: arithmetic average.
- Edge cases: zero count; mixed positive and negative values.

## Checkpoint

- [ ] I can write and call a generic method.
- [ ] I can define a generic class with one type parameter.
- [ ] I can explain why `T extends Comparable<T>` allows comparison.
- [ ] I completed exercises/Exercise01.java.
- [ ] I completed exercises/Exercise02.java.
