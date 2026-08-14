# Types and Input/Output

This module introduces basic TypeScript types, text parsing, and console output for small programs.

## Learning Metadata

- Difficulty: Beginner.
- Estimated Time: 20-35 minutes.
- Prerequisites: None; this is the entry module for the track.
- Cross-Language Lens: Compare strongly typed console parsing in C++ and C# with explicit string-to-number conversion in TypeScript and Go.

## Learning Outcomes

- `FND-TIO-01`: Choose suitable primitive values and variables for a small problem.
- `FND-TIO-02`: Read, validate, transform, and present console data.

## Quick Run

Run from the repository root:

~~~bash
python scripts/automation.py run-module --module-path languages/typescript/01-foundations/types-and-io
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

## Cross-Language Notes

- TypeScript also starts from strings, but Node console programs make parsing feel closer to Python than to C++ stream extraction.
- Compared with Python, compile-time types help organize downstream logic even though the runtime values still need explicit conversion.
- The comparison to watch is typed program structure versus JavaScript-style runtime input handling.

## Exercise Focus

- exercises/01.ts: read N numbers and print sum, average, minimum, and maximum.
- exercises/02.ts: parse product name, price, and quantity and print a formatted invoice line.

### Exercise Specs

1. exercises/01.ts
- Input: an integer N followed by N numeric values.
- Output: sum, average, minimum, and maximum.
- Edge cases: N <= 0 should print an error; decimal input should still work.

2. exercises/02.ts
- Input: one line with product name, price, and quantity.
- Output: product name, quantity, price, and total.
- Edge cases: quantity 0 should produce total 0; invalid price should print an error.

## Check Your Work

Run from the repository root after implementing a starter:

```bash
python scripts/automation.py check-exercise --language typescript --level 01-foundations --module types-and-io --exercise 01
```

Change `--exercise 01` to `--exercise 02` for the second task. Consult `exercises/solutions/` only after making a complete attempt.

## Checkpoint

- [ ] I can explain the main TypeScript idea in this module.
- [ ] I can run the example and describe the output.
- [ ] I completed exercises/01.ts.
- [ ] I completed exercises/02.ts.
