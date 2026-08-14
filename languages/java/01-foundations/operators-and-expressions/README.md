# Operators and Expressions (Java)

This module practices combining values through expressions and readable calculations.

## Learning Metadata

- Difficulty: Beginner.
- Estimated Time: 20-35 minutes.
- Prerequisites: Java 21 JDK and prior modules in this level.
- Cross-Language Lens: Compare Java's numeric promotion and explicit zero-divisor branch with division behavior in the other tracks.

## Learning Outcomes

- `FND-OPE-01`: Build expressions with correct precedence and explicit intent.
- `FND-OPE-02`: Distinguish arithmetic, comparison, and logical operations.

## Quick Run

Run from the repository root:

~~~bash
python scripts/automation.py run-module --module-path languages/java/01-foundations/operators-and-expressions
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
- Edge cases: divisor = 0; negative operands.

2. exercises/Exercise02.java
- Input: subtotal discountRate taxRate.
- Output: discount amount, tax amount, and final total.
- Edge cases: zero subtotal; zero discount and tax rates.

## Check Your Work

Run from the repository root after implementing a starter:

```bash
python scripts/automation.py check-exercise --language java --level 01-foundations --module operators-and-expressions --exercise 01
```

Change `--exercise 01` to `--exercise 02` for the second task. Consult `exercises/solutions/` only after making a complete attempt.

## Checkpoint

- [ ] I can explain the core ideas of this module.
- [ ] I can compile and run example/Main.java.
- [ ] I completed exercises/Exercise01.java.
- [ ] I completed exercises/Exercise02.java.
- [ ] I validated at least one edge case for each exercise.
