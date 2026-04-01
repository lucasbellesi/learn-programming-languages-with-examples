# Error Handling and Defensive Programming

This module teaches TypeScript programs to reject bad data cleanly without losing control flow.

## Learning Metadata

- Difficulty: Intermediate.
- Estimated Time: 30-45 minutes.
- Prerequisites: `02-core/input-validation` and `02-core/file-io-basics`.
- Cross-Language Lens: Compare guard clauses, nullable parse results, and selective `try/catch` with the defensive styles used in the other tracks.

## Quick Run

~~~bash
npm run build:typescript
node build/typescript/02-core/error-handling-and-defensive-programming/example/main.js
~~~

## Topics Covered

- Guard clauses that stop unsafe work early.
- Parse helpers that return `null` instead of half-valid data.
- Catching only the errors you actually expect.
- Preserving valid work even when part of the input is malformed.

## Common Pitfalls

- Catching every error without improving the message.
- Pushing invalid data forward just to avoid returning early.
- Mixing user-facing errors with internal debugging details.

## Exercise Focus

- exercises/01.ts: safely parse one `name score` record.
- exercises/02.ts: ignore invalid numeric tokens and summarize the valid ones.

### Exercise Specs

1. exercises/01.ts
- Input: one line shaped like `Full Name Score`.
- Output: accepted record or an error message.
- Edge cases: missing name; non-integer score; score outside `0..100`.

2. exercises/02.ts
- Input: one line of mixed tokens.
- Output: valid count and average of accepted integers.
- Edge cases: no valid integers; malformed tokens between valid numbers.

## Checkpoint

- [ ] I can stop bad input before it pollutes later steps.
- [ ] I can return safe parse results instead of throwing for routine validation.
- [ ] I can keep useful work even when some rows fail.
- [ ] I completed exercises/01.ts.
- [ ] I completed exercises/02.ts.
