# Types and Input/Output (Java)

This module practices reading typed input carefully and turning raw text into values.

## Learning Metadata

- Difficulty: Beginner.
- Estimated Time: 20-35 minutes.
- Prerequisites: Java 21 JDK and prior modules in this level.
- Cross-Language Lens: Compare Java's explicit class and type requirements with the same concept in C++, C#, Go, Python, and TypeScript.

## Quick Run

~~~bash
javac -d build/java languages/java/01-foundations/types-and-io/example/Main.java
java -cp build/java Main
~~~

## Topics Covered

- Reading typed values with Scanner.
- Converting text into int and double values.
- Printing labeled numeric summaries.

## Common Pitfalls

- Forgetting that Scanner token reads stop at whitespace.
- Using integer division when an average needs decimals.

## Cross-Language Notes

- Java requires every runnable file to put `main` inside a class.
- The examples stay package-free so beginners can compile one file at a time.
- Java's static types make many mistakes visible before the program runs.

## Exercise Focus

- exercises/Exercise01.java: read N numeric values and print sum, average, minimum, and maximum.
- exercises/Exercise02.java: parse product price quantity and print the computed total price.

### Exercise Specs

1. exercises/Exercise01.java
- Input: integer N followed by N numeric values.
- Output: summary lines for sum, average, minimum, and maximum.
- Edge cases: missing values; boundary numeric values.

2. exercises/Exercise02.java
- Input: single-line record: product price quantity.
- Output: parsed product name and computed total price.
- Edge cases: missing values; zero or repeated values where relevant.

## Checkpoint

- [ ] I can explain the core ideas of this module.
- [ ] I can compile and run example/Main.java.
- [ ] I completed exercises/Exercise01.java.
- [ ] I completed exercises/Exercise02.java.
- [ ] I validated at least one edge case for each exercise.
