# Maps and Frequency Counting (Java)

This module practices using maps to count repeated values.

## Learning Metadata

- Difficulty: Intermediate.
- Estimated Time: 30-45 minutes.
- Prerequisites: `01-foundations/strings`, `02-core/algorithms-basics`.
- Cross-Language Lens: Compare Java's `Map` APIs with dictionaries, maps, and objects in C++, C#, Go, Python, and TypeScript.

## Quick Run

~~~bash
javac -d build/java languages/java/02-core/maps-and-frequency-counting/example/Main.java
java -cp build/java Main
~~~

## Topics Covered

- Counting words with `Map`.
- Using `getOrDefault`.
- Choosing `TreeMap` for sorted output.
- Counting numeric frequencies.

## Common Pitfalls

- Forgetting to normalize text before counting.
- Producing nondeterministic output when iteration order matters.
- Updating a map entry without preserving the previous count.

## Cross-Language Notes

- `HashMap` is useful for speed, while `TreeMap` keeps keys sorted for stable reports.
- Java generics make key and value types explicit.
- Frequency counting is a common bridge from arrays and strings into collections.

## Exercise Focus

- exercises/Exercise01.java: count words from one input line.
- exercises/Exercise02.java: count integer frequencies from numeric input.

### Exercise Specs

1. exercises/Exercise01.java
- Input: one line of text.
- Output: lowercase word frequencies sorted by word.
- Edge cases: repeated words; different capitalization.

2. exercises/Exercise02.java
- Input: count followed by that many integers.
- Output: numeric frequencies sorted by value.
- Edge cases: duplicates; negative numbers; single value.

## Checkpoint

- [ ] I can update map counts with `getOrDefault`.
- [ ] I can choose a sorted map when output order matters.
- [ ] I completed exercises/Exercise01.java.
- [ ] I completed exercises/Exercise02.java.
- [ ] I tested repeated keys.
