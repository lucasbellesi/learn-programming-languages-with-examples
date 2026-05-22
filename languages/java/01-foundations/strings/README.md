# Strings (Java)

This module practices cleaning and combining text while preserving readable string logic.

## Learning Metadata

- Difficulty: Beginner.
- Estimated Time: 20-35 minutes.
- Prerequisites: Java 21 JDK and prior modules in this level.
- Cross-Language Lens: Compare Java's explicit class and type requirements with the same concept in C++, C#, Go, Python, and TypeScript.

## Quick Run

~~~bash
javac -d build/java languages/java/01-foundations/strings/example/Main.java
java -cp build/java Main
~~~

## Topics Covered

- Trimming and normalizing text.
- Splitting text into words.
- Counting characters and words.

## Common Pitfalls

- Forgetting that strings are immutable.
- Counting leading and trailing spaces as meaningful text.

## Cross-Language Notes

- Java requires every runnable file to put `main` inside a class.
- The examples stay package-free so beginners can compile one file at a time.
- Java's static types make many mistakes visible before the program runs.

## Exercise Focus

- exercises/Exercise01.java: normalize one line of text and report its length.
- exercises/Exercise02.java: split a sentence and report word and character counts.

### Exercise Specs

1. exercises/Exercise01.java
- Input: one line of text.
- Output: trimmed and lowercase text plus length.
- Edge cases: missing values; boundary numeric values.

2. exercises/Exercise02.java
- Input: one sentence.
- Output: word count and non-space character count.
- Edge cases: missing values; zero or repeated values where relevant.

## Checkpoint

- [ ] I can explain the core ideas of this module.
- [ ] I can compile and run example/Main.java.
- [ ] I completed exercises/Exercise01.java.
- [ ] I completed exercises/Exercise02.java.
- [ ] I validated at least one edge case for each exercise.
