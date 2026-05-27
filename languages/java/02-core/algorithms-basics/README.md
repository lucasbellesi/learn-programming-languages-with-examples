# Algorithms Basics (Java)

This module practices small search and counting algorithms over arrays.

## Learning Metadata

- Difficulty: Intermediate.
- Estimated Time: 30-45 minutes.
- Prerequisites: `01-foundations/arrays-and-vectors`, `01-foundations/control-flow`.
- Cross-Language Lens: Compare Java loops and helper methods with the same algorithmic patterns in C++, C#, Go, Python, and TypeScript.

## Quick Run

~~~bash
javac -d build/java languages/java/02-core/algorithms-basics/example/Main.java
java -cp build/java Main
~~~

## Topics Covered

- Linear search.
- Counting matching values.
- Aggregating minimum, maximum, and even counts.
- Returning sentinel values such as `-1`.

## Common Pitfalls

- Returning the last match when the task asks for the first.
- Forgetting to handle empty input.
- Mixing index positions with values.

## Cross-Language Notes

- Java arrays expose `.length`, not a `size()` method.
- Helper methods make algorithm intent easier to test.
- Sentinel values should be documented in output labels and exercise specs.

## Exercise Focus

- exercises/Exercise01.java: find the first index and occurrence count for a target value.
- exercises/Exercise02.java: summarize minimum, maximum, and even values.

### Exercise Specs

1. exercises/Exercise01.java
- Input: count, that many integers, then target integer.
- Output: first index and occurrence count.
- Edge cases: target missing; target at index 0.

2. exercises/Exercise02.java
- Input: count followed by that many integers.
- Output: minimum, maximum, and count of even numbers.
- Edge cases: single value; negative values; all odd values.

## Checkpoint

- [ ] I can write a linear search.
- [ ] I can count matches in one pass.
- [ ] I completed exercises/Exercise01.java.
- [ ] I completed exercises/Exercise02.java.
- [ ] I tested a missing-target case.
