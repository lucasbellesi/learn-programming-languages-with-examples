# Control Flow (Java)

This module practices choosing between branches and repeating work with predictable control flow.

## Learning Metadata

- Difficulty: Beginner.
- Estimated Time: 20-35 minutes.
- Prerequisites: Java 21 JDK and prior modules in this level.
- Cross-Language Lens: Compare Java's explicit class and type requirements with the same concept in C++, C#, Go, Python, and TypeScript.

## Quick Run

~~~bash
javac -d build/java languages/java/01-foundations/control-flow/example/Main.java
java -cp build/java Main
~~~

## Topics Covered

- if/else chains for decisions.
- Loops for repeated classification.
- Counters for grouped results.

## Common Pitfalls

- Letting boundary values fall into the wrong branch.
- Forgetting to update counters inside loops.

## Cross-Language Notes

- Java requires every runnable file to put `main` inside a class.
- The examples stay package-free so beginners can compile one file at a time.
- Java's static types make many mistakes visible before the program runs.

## Exercise Focus

- exercises/Exercise01.java: read a score and print the matching letter grade.
- exercises/Exercise02.java: count positive, negative, and zero values.

### Exercise Specs

1. exercises/Exercise01.java
- Input: one integer score.
- Output: letter grade label.
- Edge cases: missing values; boundary numeric values.

2. exercises/Exercise02.java
- Input: count N followed by N integers.
- Output: positive, negative, and zero counts.
- Edge cases: missing values; zero or repeated values where relevant.

## Checkpoint

- [ ] I can explain the core ideas of this module.
- [ ] I can compile and run example/Main.java.
- [ ] I completed exercises/Exercise01.java.
- [ ] I completed exercises/Exercise02.java.
- [ ] I validated at least one edge case for each exercise.
