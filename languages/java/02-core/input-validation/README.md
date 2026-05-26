# Input Validation (Java)

This module practices rejecting invalid values while keeping the program flow predictable.

## Learning Metadata

- Difficulty: Intermediate.
- Estimated Time: 30-45 minutes.
- Prerequisites: `01-foundations/control-flow`, `01-foundations/types-and-io`.
- Cross-Language Lens: Compare Java's explicit parsing exceptions with validation loops in C++, C#, Go, Python, and TypeScript.

## Quick Run

~~~bash
javac -d build/java languages/java/02-core/input-validation/example/Main.java
java -cp build/java Main
~~~

## Topics Covered

- Parsing integers from text.
- Rejecting out-of-range values.
- Counting accepted and skipped records.
- Reporting deterministic validation summaries.

## Common Pitfalls

- Assuming successful parsing also means the value is valid.
- Letting one invalid value stop the entire program.
- Repeating range checks instead of isolating them in a helper.

## Cross-Language Notes

- Java's `Integer.parseInt` throws when text is not numeric.
- Validation should handle both parse errors and domain errors.
- Single-file examples stay package-free so `javac` usage remains visible.

## Exercise Focus

- exercises/Exercise01.java: keep reading until an integer from 1 to 100 is accepted, then print its square.
- exercises/Exercise02.java: read a valid score count and valid scores, then print the average.

### Exercise Specs

1. exercises/Exercise01.java
- Input: repeated tokens until a valid integer in range 1..100 is entered.
- Output: validation messages and the accepted value's square.
- Edge cases: non-integer text; values below 1 or above 100.

2. exercises/Exercise02.java
- Input: score count in range 1..50, followed by scores in range 0..100.
- Output: average score.
- Edge cases: invalid count; invalid score in the middle of entry.

## Checkpoint

- [ ] I can recover from parsing errors.
- [ ] I can validate numeric ranges after parsing.
- [ ] I completed exercises/Exercise01.java.
- [ ] I completed exercises/Exercise02.java.
- [ ] I tested at least one invalid input path.
