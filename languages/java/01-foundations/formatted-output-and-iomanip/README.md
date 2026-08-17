# Formatted Console Output (Java)

This module practices formatting values so output is easier to read and compare.

## Learning Metadata

- Difficulty: Beginner.
- Estimated Time: 20-35 minutes.
- Prerequisites: Java 21 JDK and prior modules in this level.
- Cross-Language Lens: Compare Java `printf` width and precision controls with each track's formatting APIs.

## Learning Outcomes

- `FND-FMT-01`: Produce stable human-readable tabular and numeric output.
- `FND-FMT-02`: Choose precision, alignment, and labels appropriate to the data.

## Quick Run

Run from the repository root:

~~~bash
python scripts/automation.py run-module --module-path languages/java/01-foundations/formatted-output-and-iomanip
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
- Edge cases: quantity = 0; price with many decimal places.

2. exercises/Exercise02.java
- Input: principal rate years.
- Output: interest and final amount with two decimals.
- Edge cases: zero principal; zero interest rate.

## Check Your Work

Run from the repository root after implementing a starter:

```bash
python scripts/automation.py check-exercise --language java --level 01-foundations --module formatted-output-and-iomanip --exercise 01
```

Change `--exercise 01` to `--exercise 02` for the second task. Consult `exercises/solutions/` only after making a complete attempt.

## Checkpoint

- [ ] I can explain the core ideas of this module.
- [ ] I can compile and run example/Main.java.
- [ ] I completed exercises/Exercise01.java.
- [ ] I completed exercises/Exercise02.java.
- [ ] I validated at least one edge case for each exercise.
