# Sorting and Searching (Java)

This module practices ordering values before searching them.

## Learning Metadata

- Difficulty: Intermediate.
- Estimated Time: 30-45 minutes.
- Prerequisites: `02-core/algorithms-basics`.
- Cross-Language Lens: Compare Java's `Arrays.sort` with sorting helpers in C++, C#, Go, Python, and TypeScript.

## Quick Run

~~~bash
javac -d build/java languages/java/02-core/sorting-and-searching/example/Main.java
java -cp build/java Main
~~~

## Topics Covered

- Sorting arrays with `Arrays.sort`.
- Searching sorted data.
- Returning `-1` for missing values.
- Printing arrays in stable, readable formats.

## Common Pitfalls

- Searching before sorting when the algorithm expects sorted data.
- Misreading Java's `Arrays.binarySearch` negative insertion-point result.
- Forgetting that sorting mutates the original array.

## Cross-Language Notes

- `Arrays.sort` mutates primitive arrays in place.
- A small helper can hide Java's binary-search insertion-point convention for beginners.
- Sorting is often paired with validation and reporting in later modules.

## Exercise Focus

- exercises/Exercise01.java: sort integers and print them in ascending order.
- exercises/Exercise02.java: sort integers, search for a target, and report its sorted index.

### Exercise Specs

1. exercises/Exercise01.java
- Input: count followed by that many integers.
- Output: sorted values.
- Edge cases: duplicates; already sorted input.

2. exercises/Exercise02.java
- Input: count, values, then target.
- Output: sorted values and the target's sorted index or `-1`.
- Edge cases: duplicate target; missing target.

## Checkpoint

- [ ] I can sort an `int[]` in place.
- [ ] I can search sorted values and handle missing targets.
- [ ] I completed exercises/Exercise01.java.
- [ ] I completed exercises/Exercise02.java.
- [ ] I tested duplicate values.
