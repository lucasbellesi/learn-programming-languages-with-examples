# Types and Input/Output (Java)

This module practices reading typed input carefully and turning raw text into values.

## Learning Metadata

- Difficulty: Beginner.
- Estimated Time: 20-35 minutes.
- Prerequisites: Java 21 JDK; no prior programming modules required.
- Cross-Language Lens: Compare Java's `Scanner` parsing and explicit numeric types with the console-input models used by the other tracks.

## Learning Outcomes

- `FND-TIO-01`: Choose suitable primitive values and variables for a small problem.
- `FND-TIO-02`: Read, validate, transform, and present console data.

## Quick Run

Run from the repository root:

~~~bash
python scripts/automation.py run-module --module-path languages/java/01-foundations/types-and-io
~~~

### Observe, Predict, Modify

This example uses fixed scores and does not wait for keyboard input. The exercises introduce `Scanner` input.

Look for these result lines (interactive prompts and the summary heading are omitted):

~~~text
Students: 3
Total: 256.00
Average: 85.33
~~~

Change `firstScore` from `91.0` to `94.0`: predict a total of `259.00` and an average of `86.33`. The total is a `double`, so division retains a fractional part before formatting.

Restore the original values before moving on to the exercises.

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
- Edge cases: N = 0; negative and decimal values.

2. exercises/Exercise02.java
- Input: single-line record: product price quantity.
- Output: parsed product name and computed total price.
- Edge cases: quantity = 0; decimal price.

## Check Your Work

Run from the repository root after implementing a starter:

```bash
python scripts/automation.py check-exercise --language java --level 01-foundations --module types-and-io --exercise 01
```

Change `--exercise 01` to `--exercise 02` for the second task. Consult `exercises/solutions/` only after making a complete attempt.

### Visible Practice Cases

These cases come from the exercise checker. Implement the general behavior; do not
hardcode these answers. Each input line below is a separate line of standard input.
The unmodified starters are incomplete, so a failed check before implementation is expected.

**Exercise 01**

Normal input:

~~~text
3
10
20
30
~~~

Expected result labels and values (prompts omitted; decimal formatting may add zeros):

~~~text
Sum: 60.00
Average: 20.00
Minimum: 10.00
Maximum: 30.00
~~~

Also check these boundary cases. The checker compares their full output, including
prompts and spaces. In this table, `\n` means a newline; input typed by the user is
not part of the program output.

| Case | Input lines (`\n` separates lines) | Exact program output |
| --- | --- | --- |
| edge: N = 0 | `0` | `Count must be positive.\n` |
| edge: negative and decimal values | `3\n-5.5\n0\n5.5` | `Sum: 0.00\nAverage: 0.00\nMinimum: -5.50\nMaximum: 5.50\n` |

**Exercise 02**

Normal input:

~~~text
Notebook 12.50 3
~~~

Expected result labels and values (prompts omitted; decimal formatting may add zeros):

~~~text
Product: Notebook
Quantity: 3
Total: 37.50
~~~

Also check these boundary cases. The checker compares their full output, including
prompts and spaces. In this table, `\n` means a newline; input typed by the user is
not part of the program output.

| Case | Input lines (`\n` separates lines) | Exact program output |
| --- | --- | --- |
| edge: quantity = 0 | `Notebook 12.50 0` | `Product: Notebook\nQuantity: 0\nTotal: 0.00\n` |
| edge: decimal price | `Notebook 0.99 3` | `Product: Notebook\nQuantity: 3\nTotal: 2.97\n` |

## Checkpoint

- [ ] I can explain the core ideas of this module.
- [ ] I can compile and run example/Main.java.
- [ ] I completed exercises/Exercise01.java.
- [ ] I completed exercises/Exercise02.java.
- [ ] I validated at least one edge case for each exercise.
