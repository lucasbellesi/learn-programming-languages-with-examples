# Formatted Output

This module shows how TypeScript can format aligned text and numeric summaries without stream manipulators.

## Learning Metadata

- Difficulty: Beginner.
- Estimated Time: 20-35 minutes.
- Prerequisites: 01-foundations/types-and-io and 01-foundations/operators-and-expressions.
- Cross-Language Lens: Compare stream manipulators, interpolated strings, format verbs, and template-string helpers for the same reporting task.

## Quick Run

~~~bash
npm run build:typescript
node build/typescript/01-foundations/formatted-output-and-iomanip/example/main.js
~~~

## Topics Covered

- Formatting decimals with toFixed.
- Padding labels with padStart and padEnd.
- Template strings for readable reports.
- Keeping formatting logic in small helpers.

## Common Pitfalls

- Formatting too early and losing the numeric value for later math.
- Hardcoding spacing instead of using helper methods.
- Mixing alignment and business logic in the same long expression.

## Exercise Focus

- exercises/01.ts: print one aligned invoice line from item, quantity, and unit price.
- exercises/02.ts: print a two-column leaderboard row with padded names and scores.

### Exercise Specs

1. exercises/01.ts
- Input: item name, quantity, and unit price.
- Output: a padded line with total value.
- Edge cases: quantity 0 should still print cleanly; invalid numbers should print an error.

2. exercises/02.ts
- Input: name and score pairs on one line.
- Output: one formatted row per pair.
- Edge cases: odd token counts should print an error; decimal scores should still align.

## Checkpoint

- [ ] I can explain the main TypeScript idea in this module.
- [ ] I can run the example and describe the output.
- [ ] I completed exercises/01.ts.
- [ ] I completed exercises/02.ts.
