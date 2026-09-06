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

### Observe, Predict, Modify

This example uses fixed strings and does not wait for keyboard input. The exercises read from standard input.

Look for these result lines (interactive prompts and the summary heading are omitted):

~~~text
Age: 27
Original price: 14.50
Member discount applied: true
Final price: 13.05
~~~

Change `rawMemberFlag` to `"false"` and predict a final price of `14.50`. Then try `rawAge = "hello"`: the example reports invalid sample input. Numeric parsing can accept a numeric prefix such as `"27years"`; it is not complete input validation.

Restore the original values before moving on to the exercises.

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

### Visible Practice Cases

These cases come from the exercise checker. Implement the general behavior; do not
hardcode these answers. Each input line below is a separate line of standard input.
The unmodified starters are incomplete, so a failed check before implementation is expected.

**Exercise 01**

Normal input:

~~~text
3
10
20
30
~~~

Expected result labels and values (prompts omitted; decimal formatting may add zeros):

~~~text
Sum: 60
Average: 20.00
Minimum: 10
Maximum: 30
~~~

Also check these boundary cases. The checker compares their full output, including
prompts and spaces. In this table, `\n` means a newline; input typed by the user is
not part of the program output.

| Case | Input lines (`\n` separates lines) | Exact program output |
| --- | --- | --- |
| edge: N <= 0 should print an error | `0\n10\n20\n30` | `Count must be a positive integer.\n` |
| edge: decimal input should still work | `3\n1.5\n2.5\n3` | `Sum: 7\nAverage: 2.33\nMinimum: 1.5\nMaximum: 3\n` |

**Exercise 02**

Normal input:

~~~text
notebook 2.50 4
~~~

Expected result labels and values (prompts omitted; decimal formatting may add zeros):

~~~text
Product: notebook
Quantity: 4
Price: 2.50
Total: 10.00
~~~

Also check these boundary cases. The checker compares their full output, including
prompts and spaces. In this table, `\n` means a newline; input typed by the user is
not part of the program output.

| Case | Input lines (`\n` separates lines) | Exact program output |
| --- | --- | --- |
| edge: quantity 0 should produce total 0 | `notebook 2.50 0` | `Product: notebook\nQuantity: 0\nPrice: 2.50\nTotal: 0.00\n` |
| edge: invalid price should print an error | `notebook invalid 4` | `Invalid invoice data.\n` |

## Checkpoint

- [ ] I can explain the main TypeScript idea in this module.
- [ ] I can run the example and describe the output.
- [ ] I completed exercises/01.ts.
- [ ] I completed exercises/02.ts.
