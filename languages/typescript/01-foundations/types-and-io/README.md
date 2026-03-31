# Types and Input/Output

This module introduces basic TypeScript types, text parsing, and console output for small programs.

## Learning Metadata

- Difficulty: Beginner.
- Estimated Time: 20-35 minutes.
- Prerequisites: None; this is the entry module for the track.
- Cross-Language Lens: Compare strongly typed console parsing in C++ and C# with explicit string-to-number conversion in TypeScript and Go.

## Quick Run

~~~bash
npm run build:typescript
node build/typescript/01-foundations/types-and-io/example/main.js
~~~

## Topics Covered

- number, string, and boolean basics.
- Parsing text with Number.parseInt and Number.parseFloat.
- Checking NaN before trusting parsed values.
- Printing readable summaries with console.log.

## Common Pitfalls

- Forgetting that all raw stdin data starts as text.
- Treating NaN as a valid number.
- Using Number() without explaining what invalid input does.

## Exercise Focus

- exercises/01.ts: read N numbers and print sum, average, minimum, and maximum.
- exercises/02.ts: parse product price quantity and print a formatted invoice line.

### Exercise Specs

1. exercises/01.ts
- Input: an integer N followed by N numeric values.
- Output: sum, average, minimum, and maximum.
- Edge cases: N <= 0 should print an error; decimal input should still work.

2. exercises/02.ts
- Input: one line with product price quantity.
- Output: product name, quantity, price, and total.
- Edge cases: quantity 0 should produce total 0; invalid price should print an error.

## Checkpoint

- [ ] I can explain the main TypeScript idea in this module.
- [ ] I can run the example and describe the output.
- [ ] I completed exercises/01.ts.
- [ ] I completed exercises/02.ts.
