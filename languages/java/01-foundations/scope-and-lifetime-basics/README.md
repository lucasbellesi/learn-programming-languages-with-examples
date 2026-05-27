# Scope and Lifetime Basics (Java)

This module practices how names stay visible only inside the blocks that own them.

## Learning Metadata

- Difficulty: Beginner.
- Estimated Time: 20-35 minutes.
- Prerequisites: Java 21 JDK and prior modules in this level.
- Cross-Language Lens: Compare Java's explicit class and type requirements with the same concept in C++, C#, Go, Python, and TypeScript.

## Quick Run

~~~bash
javac -d build/java languages/java/01-foundations/scope-and-lifetime-basics/example/Main.java
java -cp build/java Main
~~~

## Topics Covered

- Block scope for local variables.
- Method-local values.
- Static fields for shared state.

## Common Pitfalls

- Trying to use a variable outside the block that declared it.
- Confusing method-local variables with shared static state.

## Cross-Language Notes

- Java requires every runnable file to put `main` inside a class.
- The examples stay package-free so beginners can compile one file at a time.
- Java's static types make many mistakes visible before the program runs.

## Exercise Focus

- exercises/Exercise01.java: show how a value changes inside and outside a nested block.
- exercises/Exercise02.java: call a method repeatedly and report a shared counter.

### Exercise Specs

1. exercises/Exercise01.java
- Input: one integer base value.
- Output: outer, inner, and final values.
- Edge cases: missing values; boundary numeric values.

2. exercises/Exercise02.java
- Input: one integer count.
- Output: number of method calls recorded by shared state.
- Edge cases: missing values; zero or repeated values where relevant.

## Checkpoint

- [ ] I can explain the core ideas of this module.
- [ ] I can compile and run example/Main.java.
- [ ] I completed exercises/Exercise01.java.
- [ ] I completed exercises/Exercise02.java.
- [ ] I validated at least one edge case for each exercise.
