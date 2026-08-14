# Arrays and Lists (Java)

This module practices storing related values in ordered collections and iterating safely.

## Learning Metadata

- Difficulty: Beginner.
- Estimated Time: 20-35 minutes.
- Prerequisites: Java 21 JDK and prior modules in this level.
- Cross-Language Lens: Compare Java arrays with C++ vectors, C# arrays, Go slices, Python lists, and TypeScript arrays.

## Learning Outcomes

- `FND-SEQ-01`: Store and traverse ordered collections safely.
- `FND-SEQ-02`: Handle empty collections and index boundaries explicitly.

## Quick Run

Run from the repository root:

~~~bash
python scripts/automation.py run-module --module-path languages/java/01-foundations/arrays-and-vectors
~~~

## Topics Covered

- Arrays and ArrayList for ordered data.
- Index-based iteration.
- Searching and aggregation.

## Common Pitfalls

- Reading more values than the collection contains.
- Starting min/max from an arbitrary constant.

## Cross-Language Notes

- Java requires every runnable file to put `main` inside a class.
- The examples stay package-free so beginners can compile one file at a time.
- Java's static types make many mistakes visible before the program runs.

## Exercise Focus

- exercises/Exercise01.java: read N integers and print summary statistics.
- exercises/Exercise02.java: count how many times a target appears in a list.

### Exercise Specs

1. exercises/Exercise01.java
- Input: count N followed by N integers.
- Output: sum, average, minimum, and maximum.
- Edge cases: N = 0; negative and positive values.

2. exercises/Exercise02.java
- Input: count N, N integers, then target.
- Output: target occurrence count.
- Edge cases: N = 0; target absent.

## Check Your Work

Run from the repository root after implementing a starter:

```bash
python scripts/automation.py check-exercise --language java --level 01-foundations --module arrays-and-vectors --exercise 01
```

Change `--exercise 01` to `--exercise 02` for the second task. Consult `exercises/solutions/` only after making a complete attempt.

## Checkpoint

- [ ] I can explain the core ideas of this module.
- [ ] I can compile and run example/Main.java.
- [ ] I completed exercises/Exercise01.java.
- [ ] I completed exercises/Exercise02.java.
- [ ] I validated at least one edge case for each exercise.
