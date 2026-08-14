# Functions (Java)

This module practices breaking behavior into reusable functions with clear inputs and outputs.

## Learning Metadata

- Difficulty: Beginner.
- Estimated Time: 20-35 minutes.
- Prerequisites: Java 21 JDK and prior modules in this level.
- Cross-Language Lens: Compare Java's static methods with free functions, package-level functions, and module functions in the other tracks.

## Learning Outcomes

- `FND-FUN-01`: Decompose a problem into focused functions with explicit contracts.
- `FND-FUN-02`: Use parameters and return values without hidden state changes.

## Quick Run

Run from the repository root:

~~~bash
python scripts/automation.py run-module --module-path languages/java/01-foundations/functions
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
- Edge cases: radius = 0; decimal radius.

2. exercises/Exercise02.java
- Input: three integers.
- Output: minimum and maximum values.
- Edge cases: repeated values; all values are negative.

## Check Your Work

Run from the repository root after implementing a starter:

```bash
python scripts/automation.py check-exercise --language java --level 01-foundations --module functions --exercise 01
```

Change `--exercise 01` to `--exercise 02` for the second task. Consult `exercises/solutions/` only after making a complete attempt.

## Checkpoint

- [ ] I can explain the core ideas of this module.
- [ ] I can compile and run example/Main.java.
- [ ] I completed exercises/Exercise01.java.
- [ ] I completed exercises/Exercise02.java.
- [ ] I validated at least one edge case for each exercise.
