# Control Flow (Java)

This module practices choosing between branches and repeating work with predictable control flow.

## Learning Metadata

- Difficulty: Beginner.
- Estimated Time: 20-35 minutes.
- Prerequisites: Java 21 JDK and prior modules in this level.
- Cross-Language Lens: Compare Java's `if` chains and counted loops with equivalent branching and iteration constructs in the other tracks.

## Learning Outcomes

- `FND-CFL-01`: Select branches that cover normal and boundary conditions.
- `FND-CFL-02`: Write terminating loops and reason about their invariants.

## Quick Run

Run from the repository root:

~~~bash
python scripts/automation.py run-module --module-path languages/java/01-foundations/control-flow
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
- Edge cases: grade boundary; score outside 0..100.

2. exercises/Exercise02.java
- Input: count N followed by N integers.
- Output: positive, negative, and zero counts.
- Edge cases: N = 0; all values are zero.

## Check Your Work

Run from the repository root after implementing a starter:

```bash
python scripts/automation.py check-exercise --language java --level 01-foundations --module control-flow --exercise 01
```

Change `--exercise 01` to `--exercise 02` for the second task. Consult `exercises/solutions/` only after making a complete attempt.

## Checkpoint

- [ ] I can explain the core ideas of this module.
- [ ] I can compile and run example/Main.java.
- [ ] I completed exercises/Exercise01.java.
- [ ] I completed exercises/Exercise02.java.
- [ ] I validated at least one edge case for each exercise.
