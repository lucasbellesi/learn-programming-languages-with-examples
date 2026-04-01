# Input Validation

This module teaches defensive validation patterns for TypeScript console programs.

## Learning Metadata

- Difficulty: Intermediate.
- Estimated Time: 30-45 minutes.
- Prerequisites: `01-foundations/types-and-io` and `01-foundations/control-flow`.
- Cross-Language Lens: Compare retry-loop validation in TypeScript with the same logic in C++, C#, Go, and Python, especially where parsing APIs fail differently.

## Quick Run

~~~bash
npm run build:typescript
node build/typescript/02-core/input-validation/example/main.js
~~~

## Topics Covered

- Centralizing validation in helper functions.
- Separating parse failures from range failures.
- Keeping programs stable after invalid attempts.
- Reusing validation rules across prompts or datasets.

## Common Pitfalls

- Accepting parsed values before checking range constraints.
- Returning vague errors that hide why validation failed.
- Repeating the same checks inline instead of extracting helpers.

## Exercise Focus

- exercises/01.ts: validate one integer in range `1..100` and print its square.
- exercises/02.ts: validate a score count and matching scores, then print the average.

### Exercise Specs

1. exercises/01.ts
- Input: one integer attempt.
- Output: square of the accepted value.
- Edge cases: non-numeric text; values below `1` or above `100`.

2. exercises/02.ts
- Input: score count in range `1..50`, followed by that many scores in range `0..100`.
- Output: average score.
- Edge cases: missing scores; invalid score values; boundary values `0` and `100`.

## Checkpoint

- [ ] I can validate both parsing and range constraints before using a value.
- [ ] I can keep error messages specific enough to explain what failed.
- [ ] I can reuse one helper across multiple validation points.
- [ ] I completed exercises/01.ts.
- [ ] I completed exercises/02.ts.
