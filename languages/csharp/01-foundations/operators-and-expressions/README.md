# Operators and Expressions (C#)

This module practices arithmetic operators, precedence, and derived calculations.

## Learning Metadata

- Difficulty: Beginner.
- Estimated Time: 20-35 minutes.
- Prerequisites: `01-foundations/types-and-io`.
- Cross-Language Lens: Compare integer division, boolean logic, and truthiness rules before assuming the same expression means the same thing in every language.

## Learning Outcomes

- `FND-OPE-01`: Build expressions with correct precedence and explicit intent.
- `FND-OPE-02`: Distinguish arithmetic, comparison, and logical operations.

## Quick Run

Run from the repository root:

~~~bash
python scripts/automation.py run-module --module-path languages/csharp/01-foundations/operators-and-expressions
~~~

## Topics Covered

- Integer division and modulo decomposition.
- Expression grouping for discount and tax pipelines.
- Order of operations in multi-step formulas.
- Formatting computed monetary outputs.

## Common Pitfalls

- Forgetting to reject negative totals for time conversion or subtotal.
- Applying tax before discount when the exercise requires the opposite.
- Losing precision by using integer arithmetic for percentages.

## Cross-Language Notes

- In C#, read this module through the native focus ?Operators and Expressions?; the shared folder name remains stable for side-by-side navigation.
- Use static types, .NET collections, and managed-resource patterns to demonstrate how to build expressions with correct precedence and explicit intent.
- Compare observable behavior with the other tracks when learning to distinguish arithmetic, comparison, and logical operations; equivalent evidence matters more than identical syntax.

## Exercise Focus

- exercises/01.cs: convert total seconds into hours, minutes, and seconds.
- exercises/02.cs: apply discount and tax percentages to compute final total.

### Exercise Specs

1. exercises/01.cs
- Input: single integer totalSeconds.
- Output: hours, minutes, and seconds components.
- Edge cases: negative input; boundary values under 60 seconds.

2. exercises/02.cs
- Input: subtotal, discountPercent, and taxPercent.
- Output: discount amount, tax amount, and final total.
- Edge cases: subtotal < 0; zero discount or zero tax.

## Check Your Work

Run from the repository root after implementing a starter:

```bash
python scripts/automation.py check-exercise --language csharp --level 01-foundations --module operators-and-expressions --exercise 01
```

Change `--exercise 01` to `--exercise 02` for the second task. Consult `exercises/solutions/` only after making a complete attempt.

## Checkpoint

- [ ] I can explain the core ideas of this module.
- [ ] I can run and modify example/main.cs.
- [ ] I completed exercises/01.cs.
- [ ] I completed exercises/02.cs.
- [ ] I validated at least one edge case for each exercise.
