# Formatted Output (Java)

This module practices formatting values so output is easier to read and compare.

## Learning Metadata

- Difficulty: Beginner.
- Estimated Time: 20-35 minutes.
- Prerequisites: Java 21 JDK and prior modules in this level.
- Cross-Language Lens: Compare Java's explicit class and type requirements with the same concept in C++, C#, Go, Python, and TypeScript.

## Quick Run

~~~bash
javac -d build/java languages/java/01-foundations/formatted-output-and-iomanip/example/Main.java
java -cp build/java Main
~~~

## Topics Covered

- printf formatting.
- Fixed decimal places.
- Aligned table-like output.

## Common Pitfalls

- Using locale-sensitive decimal output unintentionally.
- Formatting numbers before doing the calculation.

## Cross-Language Notes

- Java requires every runnable file to put `main` inside a class.
- The examples stay package-free so beginners can compile one file at a time.
- Java's static types make many mistakes visible before the program runs.

## Exercise Focus

- exercises/Exercise01.java: format a product row with aligned columns.
- exercises/Exercise02.java: format simple interest output with two decimal places.

### Exercise Specs

1. exercises/Exercise01.java
- Input: product price quantity.
- Output: aligned product, quantity, price, and total fields.
- Edge cases: missing values; boundary numeric values.

2. exercises/Exercise02.java
- Input: principal rate years.
- Output: interest and final amount with two decimals.
- Edge cases: missing values; zero or repeated values where relevant.

## Checkpoint

- [ ] I can explain the core ideas of this module.
- [ ] I can compile and run example/Main.java.
- [ ] I completed exercises/Exercise01.java.
- [ ] I completed exercises/Exercise02.java.
- [ ] I validated at least one edge case for each exercise.
