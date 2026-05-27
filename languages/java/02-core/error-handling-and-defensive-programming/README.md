# Error Handling and Defensive Programming (Java)

This module practices handling invalid operations and malformed records explicitly.

## Learning Metadata

- Difficulty: Intermediate.
- Estimated Time: 35-50 minutes.
- Prerequisites: `02-core/input-validation`, `02-core/file-io-basics`.
- Cross-Language Lens: Compare Java exceptions and guard clauses with defensive patterns in C++, C#, Go, Python, and TypeScript.

## Quick Run

~~~bash
javac -d build/java languages/java/02-core/error-handling-and-defensive-programming/example/Main.java
java -cp build/java Main
~~~

## Topics Covered

- Guarding invalid operations.
- Catching parsing failures.
- Continuing after malformed records.
- Reporting accepted and skipped data.

## Common Pitfalls

- Catching exceptions too broadly and hiding the real problem.
- Dividing before checking for zero.
- Treating malformed rows as valid default values.

## Cross-Language Notes

- Java uses exceptions for many parse and I/O failures.
- Guard clauses keep the happy path easier to read.
- Defensive programs should explain what was skipped and why.

## Exercise Focus

- exercises/Exercise01.java: divide two integers defensively.
- exercises/Exercise02.java: parse name-score rows until EOF and summarize accepted rows.

### Exercise Specs

1. exercises/Exercise01.java
- Input: two integer tokens.
- Output: integer division result or a clear error message.
- Edge cases: non-integer input; division by zero.

2. exercises/Exercise02.java
- Input: rows shaped as `name score` until EOF.
- Output: accepted row count, skipped row count, and average score.
- Edge cases: malformed rows; score outside 0..100.

## Checkpoint

- [ ] I can use guard clauses before risky operations.
- [ ] I can catch parsing errors without masking valid data.
- [ ] I completed exercises/Exercise01.java.
- [ ] I completed exercises/Exercise02.java.
- [ ] I tested at least one malformed input row.
