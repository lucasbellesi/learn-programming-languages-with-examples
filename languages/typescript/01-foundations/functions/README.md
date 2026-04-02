# Functions

This module introduces reusable logic through typed function design.

## Learning Metadata

- Difficulty: Beginner.
- Estimated Time: 20-35 minutes.
- Prerequisites: 01-foundations/control-flow and 01-foundations/operators-and-expressions.
- Cross-Language Lens: Compare helper-function design and overload signatures in TypeScript with overloads, templates, and simpler function models in the other tracks.

## Quick Run

~~~bash
npm run build:typescript
node build/typescript/01-foundations/functions/example/main.js
~~~

## Topics Covered

- Declaring parameter and return types.
- Separating small computations into named helpers.
- Using overload signatures for readable APIs.
- Returning values instead of mutating hidden state.

## Common Pitfalls

- Writing helpers that do too many unrelated things.
- Forgetting to declare the return type when the function deserves one.
- Using overloads when a union type would be simpler.

## Cross-Language Notes

- TypeScript sits between Python and C#: functions feel lightweight, but overload signatures and typed returns still shape the API.
- Compared with Go, the language offers richer declaration-time modeling without going fully C++-style.
- The main comparison is how type annotations add structure while the JavaScript runtime keeps calls flexible.

## Exercise Focus

- exercises/01.ts: return the maximum of three integers.
- exercises/02.ts: count vowels in one line of text.

### Exercise Specs

1. exercises/01.ts
- Input: three integers.
- Output: the largest value.
- Edge cases: repeated maximum values should still return the right answer; negative values should still work.

2. exercises/02.ts
- Input: one line of text.
- Output: the vowel count.
- Edge cases: an empty string should return 0; uppercase vowels should be counted.

## Checkpoint

- [ ] I can explain the main TypeScript idea in this module.
- [ ] I can run the example and describe the output.
- [ ] I completed exercises/01.ts.
- [ ] I completed exercises/02.ts.
