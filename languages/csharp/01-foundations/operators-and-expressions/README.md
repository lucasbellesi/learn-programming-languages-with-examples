# Operators and Expressions (C#)

This module practices arithmetic operators, precedence, and derived calculations.

## Quick Run

~~~bash
dotnet run --project example/operators-and-expressions-example.csproj
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

## Checkpoint

- [ ] I can explain the core ideas of this module.
- [ ] I can run and modify example/main.cs.
- [ ] I completed exercises/01.cs.
- [ ] I completed exercises/02.cs.
- [ ] I validated at least one edge case for each exercise.