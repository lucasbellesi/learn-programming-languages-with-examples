# Operators and Expressions

This module uses arithmetic, comparisons, and boolean expressions to build small TypeScript decisions.

## Learning Metadata

- Difficulty: Beginner.
- Estimated Time: 20-35 minutes.
- Prerequisites: 01-foundations/types-and-io.
- Cross-Language Lens: Compare integer division, remainder, and boolean expressions before assuming the same operator behaves identically across languages.

## Learning Outcomes

- `FND-OPE-01`: Build expressions with correct precedence and explicit intent.
- `FND-OPE-02`: Distinguish arithmetic, comparison, and logical operations.

## Quick Run

Run from the repository root:

~~~bash
python scripts/automation.py run-module --module-path languages/typescript/01-foundations/operators-and-expressions
~~~

## Topics Covered

- Arithmetic with +, -, *, /, and %.
- Comparison operators and boolean combinations.
- Short conditional expressions with the ternary operator.
- Using expressions to build readable decisions.

## Common Pitfalls

- Forgetting that / always produces a floating-point result in JavaScript and TypeScript.
- Mixing string concatenation and arithmetic accidentally.
- Writing compact expressions that hide the business rule.

## Cross-Language Notes

- In TypeScript, read this module through the native focus ?Operators and Expressions?; the shared folder name remains stable for side-by-side navigation.
- Use structural types, Node APIs, and explicit reference conventions to demonstrate how to build expressions with correct precedence and explicit intent.
- Compare observable behavior with the other tracks when learning to distinguish arithmetic, comparison, and logical operations; equivalent evidence matters more than identical syntax.

## Exercise Focus

- exercises/01.ts: compute quotient, remainder, and parity from two integers.
- exercises/02.ts: evaluate a discount rule from subtotal and loyalty status.

### Exercise Specs

1. exercises/01.ts
- Input: two integers.
- Output: quotient, remainder, and whether the first integer is even.
- Edge cases: division by zero should print an error; negative values should still work.

2. exercises/02.ts
- Input: subtotal and loyalty flag (true or false).
- Output: final price after the discount rule.
- Edge cases: subtotal 0 should remain 0; invalid loyalty text should print an error.

## Check Your Work

Run from the repository root after implementing a starter:

```bash
python scripts/automation.py check-exercise --language typescript --level 01-foundations --module operators-and-expressions --exercise 01
```

Change `--exercise 01` to `--exercise 02` for the second task. Consult `exercises/solutions/` only after making a complete attempt.

## Checkpoint

- [ ] I can explain the main TypeScript idea in this module.
- [ ] I can run the example and describe the output.
- [ ] I completed exercises/01.ts.
- [ ] I completed exercises/02.ts.
