# Strings

This module practices cleanup, search, and tokenization with immutable TypeScript strings.

## Learning Metadata

- Difficulty: Beginner.
- Estimated Time: 20-35 minutes.
- Prerequisites: 01-foundations/types-and-io and 01-foundations/control-flow.
- Cross-Language Lens: Compare immutable string handling, indexing rules, and tokenization helpers across all five tracks.

## Quick Run

~~~bash
npm run build:typescript
node build/typescript/01-foundations/strings/example/main.js
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

- Compared with C++, the other tracks usually hide more of the low-level string-management cost while keeping the same parsing goals.
- Relative to Python and TypeScript, C# and Go keep more explicit API choices around splitting, trimming, and rebuilding text.
- The main comparison is text-processing convenience versus how visible allocation and mutation remain.

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

## Checkpoint

- [ ] I can explain the main TypeScript idea in this module.
- [ ] I can run the example and describe the output.
- [ ] I completed exercises/01.ts.
- [ ] I completed exercises/02.ts.
