# Functions (Java)

This module practices breaking behavior into reusable functions with clear inputs and outputs.

## Learning Metadata

- Difficulty: Beginner.
- Estimated Time: 20-35 minutes.
- Prerequisites: Java 21 JDK and prior modules in this level.
- Cross-Language Lens: Compare Java's explicit class and type requirements with the same concept in C++, C#, Go, Python, and TypeScript.

## Quick Run

~~~bash
javac -d build/java languages/java/01-foundations/functions/example/Main.java
java -cp build/java Main
~~~

## Topics Covered

- Static helper methods.
- Parameters and return values.
- Keeping main focused on orchestration.

## Common Pitfalls

- Mixing input code into every helper.
- Returning the wrong type from numeric helpers.

## Cross-Language Notes

- Java requires every runnable file to put `main` inside a class.
- The examples stay package-free so beginners can compile one file at a time.
- Java's static types make many mistakes visible before the program runs.

## Exercise Focus

- exercises/Exercise01.java: compute circle area and circumference with helper methods.
- exercises/Exercise02.java: read three integers and report minimum and maximum with helper methods.

### Exercise Specs

1. exercises/Exercise01.java
- Input: one radius value.
- Output: area and circumference.
- Edge cases: missing values; boundary numeric values.

2. exercises/Exercise02.java
- Input: three integers.
- Output: minimum and maximum values.
- Edge cases: missing values; zero or repeated values where relevant.

## Checkpoint

- [ ] I can explain the core ideas of this module.
- [ ] I can compile and run example/Main.java.
- [ ] I completed exercises/Exercise01.java.
- [ ] I completed exercises/Exercise02.java.
- [ ] I validated at least one edge case for each exercise.
