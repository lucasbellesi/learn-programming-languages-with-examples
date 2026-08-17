# Strings (C#)

This module practices splitting text, normalizing characters, and basic text analysis.

## Learning Metadata

- Difficulty: Beginner.
- Estimated Time: 20-35 minutes.
- Prerequisites: `01-foundations/types-and-io`, `01-foundations/control-flow`.
- Cross-Language Lens: Compare immutable string handling, indexing rules, and tokenization helpers in each language.

## Learning Outcomes

- `FND-STR-01`: Normalize, inspect, and transform textual data.
- `FND-STR-02`: Handle empty input and character boundaries safely.

## Quick Run

Run from the repository root:

~~~bash
python scripts/automation.py run-module --module-path languages/csharp/01-foundations/strings
~~~

## Topics Covered

- Tokenizing text into words.
- Character filtering and normalization.
- Case-insensitive comparisons.
- Simple palindrome checks on sanitized text.

## Common Pitfalls

- Counting words without removing extra spaces.
- Comparing palindromes before removing punctuation and case differences.
- Failing to handle inputs without alphabetic characters.

## Cross-Language Notes

- In C#, read this module through the native focus ?Strings?; the shared folder name remains stable for side-by-side navigation.
- Use static types, .NET collections, and managed-resource patterns to demonstrate how to normalize, inspect, and transform textual data.
- Compare observable behavior with the other tracks when learning to handle empty input and character boundaries safely; equivalent evidence matters more than identical syntax.

## Exercise Focus

- exercises/01.cs: count words in an input line using robust whitespace handling.
- exercises/02.cs: normalize input and detect whether it is a palindrome.

### Exercise Specs

1. exercises/01.cs
- Input: single line of text.
- Output: word count.
- Edge cases: empty or blank line; multiple spaces between words.

2. exercises/02.cs
- Input: single line that may contain spaces or punctuation.
- Output: Palindrome or Not palindrome style result.
- Edge cases: input with no letters; mixed upper/lower case.

## Check Your Work

Run from the repository root after implementing a starter:

```bash
python scripts/automation.py check-exercise --language csharp --level 01-foundations --module strings --exercise 01
```

Change `--exercise 01` to `--exercise 02` for the second task. Consult `exercises/solutions/` only after making a complete attempt.

## Checkpoint

- [ ] I can explain the core ideas of this module.
- [ ] I can run and modify example/main.cs.
- [ ] I completed exercises/01.cs.
- [ ] I completed exercises/02.cs.
- [ ] I validated at least one edge case for each exercise.
