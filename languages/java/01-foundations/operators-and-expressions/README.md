# Operators and Expressions (Java)

This module practices combining values through expressions and readable calculations.

## Learning Metadata

- Difficulty: Beginner.
- Estimated Time: 20-35 minutes.
- Prerequisites: Java 21 JDK and prior modules in this level.
- Cross-Language Lens: Compare Java's explicit class and type requirements with the same concept in C++, C#, Go, Python, and TypeScript.

## Quick Run

~~~bash
javac -d build/java languages/java/01-foundations/operators-and-expressions/example/Main.java
java -cp build/java Main
~~~

## Topics Covered

- Arithmetic expressions and precedence.
- Combining subtraction, multiplication, and division.
- Guarding division by zero.

## Common Pitfalls

- Relying on implicit precedence when parentheses would be clearer.
- Dividing by zero without checking first.

## Cross-Language Notes

- Java requires every runnable file to put `main` inside a class.
- The examples stay package-free so beginners can compile one file at a time.
- Java's static types make many mistakes visible before the program runs.

## Exercise Focus

- exercises/Exercise01.java: read two numbers and print sum, difference, product, and quotient.
- exercises/Exercise02.java: compute a discounted and taxed checkout total.

### Exercise Specs

1. exercises/Exercise01.java
- Input: two numeric values.
- Output: sum, difference, product, and quotient.
- Edge cases: missing values; boundary numeric values.

2. exercises/Exercise02.java
- Input: subtotal discountRate taxRate.
- Output: discount amount, tax amount, and final total.
- Edge cases: missing values; zero or repeated values where relevant.

## Checkpoint

- [ ] I can explain the core ideas of this module.
- [ ] I can compile and run example/Main.java.
- [ ] I completed exercises/Exercise01.java.
- [ ] I completed exercises/Exercise02.java.
- [ ] I validated at least one edge case for each exercise.
