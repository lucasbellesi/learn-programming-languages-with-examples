# Algorithms Basics

This module introduces core algorithm patterns over arrays in plain TypeScript.

## Learning Metadata

- Difficulty: Intermediate.
- Estimated Time: 30-45 minutes.
- Prerequisites: `01-foundations/arrays-and-vectors` and `01-foundations/functions`.
- Cross-Language Lens: Compare explicit loops with library helpers and notice when beginner-friendly code is clearer than a dense chain of methods.

## Quick Run

~~~bash
npm run build:typescript
node build/typescript/02-core/algorithms-basics/example/main.js
~~~

## Topics Covered

- Linear search for the first matching item.
- One-pass minimum and maximum updates.
- Counting matches while scanning once.
- Combining several statistics in a single traversal.

## Common Pitfalls

- Assuming arrays are non-empty before min/max logic.
- Using multiple passes when one traversal is enough.
- Hiding simple logic inside clever but unreadable helpers.

## Cross-Language Notes

- Compared with the C++ baseline, the same traversal and aggregation ideas are expressed with different defaults for loops, collections, and helper functions.
- Relative to Python, the statically typed tracks make intermediate state and accumulator types more explicit.
- The useful comparison is algorithm shape staying constant while the surrounding syntax and safety rails change.

## Exercise Focus

- exercises/01.ts: find the first index of a target value.
- exercises/02.ts: compute minimum, maximum, and even count in one pass.

### Exercise Specs

1. exercises/01.ts
- Input: integer `n`, then `n` values, then a target.
- Output: first index of target or `-1`.
- Edge cases: `n <= 0`; target not present.

2. exercises/02.ts
- Input: integer `n`, then `n` values.
- Output: minimum, maximum, and even count.
- Edge cases: all odd numbers; all equal values; `n <= 0`.

## Checkpoint

- [ ] I can implement linear search without relying on hidden helpers.
- [ ] I can compute multiple statistics in a single traversal.
- [ ] I can protect min/max logic against empty input.
- [ ] I completed exercises/01.ts.
- [ ] I completed exercises/02.ts.
