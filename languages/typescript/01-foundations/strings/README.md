# Strings

This module practices cleanup, search, and tokenization with immutable TypeScript strings.

## Learning Metadata

- Difficulty: Beginner.
- Estimated Time: 20-35 minutes.
- Prerequisites: 01-foundations/types-and-io and 01-foundations/control-flow.
- Cross-Language Lens: Compare immutable string handling, indexing rules, and tokenization helpers across all five tracks.

## Learning Outcomes

- `FND-STR-01`: Normalize, inspect, and transform textual data.
- `FND-STR-02`: Handle empty input and character boundaries safely.

## Quick Run

Run from the repository root:

~~~bash
python scripts/automation.py run-module --module-path languages/typescript/01-foundations/strings
~~~

## Topics Covered

- Trimming and normalizing text.
- Splitting strings into tokens.
- Lowercasing for case-insensitive checks.
- Building new strings from cleaned parts.

## Common Pitfalls

- Assuming strings can be changed in place.
- Forgetting to trim before splitting user text.
- Using case-sensitive comparisons by accident.

## Cross-Language Notes

- In TypeScript, read this module through the native focus ?Strings?; the shared folder name remains stable for side-by-side navigation.
- Use structural types, Node APIs, and explicit reference conventions to demonstrate how to normalize, inspect, and transform textual data.
- Compare observable behavior with the other tracks when learning to handle empty input and character boundaries safely; equivalent evidence matters more than identical syntax.

## Exercise Focus

- exercises/01.ts: count words in one line of text.
- exercises/02.ts: normalize an email-like token to lowercase and mask the domain.

### Exercise Specs

1. exercises/01.ts
- Input: one line of text.
- Output: the number of non-empty words.
- Edge cases: empty input should return 0; repeated spaces should not create extra words.

2. exercises/02.ts
- Input: one token shaped like name@domain.
- Output: the normalized token with the domain replaced by ***.
- Edge cases: missing @ should print an error; uppercase letters should be normalized.

## Check Your Work

Run from the repository root after implementing a starter:

```bash
python scripts/automation.py check-exercise --language typescript --level 01-foundations --module strings --exercise 01
```

Change `--exercise 01` to `--exercise 02` for the second task. Consult `exercises/solutions/` only after making a complete attempt.

## Checkpoint

- [ ] I can explain the main TypeScript idea in this module.
- [ ] I can run the example and describe the output.
- [ ] I completed exercises/01.ts.
- [ ] I completed exercises/02.ts.
