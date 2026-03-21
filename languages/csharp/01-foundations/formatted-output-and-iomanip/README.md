# Formatted Output and I/O Manipulators (C#)

This module practices table-style output, alignment, and precision control.

## Quick Run

~~~bash
dotnet run --project example/formatted-output-and-iomanip-example.csproj
~~~

## Topics Covered

- Column alignment for tabular output.
- Fixed precision for monetary and statistical values.
- Building readable reports from structured input.
- Controlling output format based on user precision input.

## Common Pitfalls

- Producing unreadable tables with inconsistent widths.
- Not validating precision ranges before formatting.
- Forgetting to maintain numeric precision in totals and averages.

## Exercise Focus

- exercises/01.cs: collect product rows and print an aligned invoice table with totals.
- exercises/02.cs: compute summary metrics and print them using user-selected precision.

### Exercise Specs

1. exercises/01.cs
- Input: product count, then name, price, and quantity for each product.
- Output: formatted table with line totals and grand total.
- Edge cases: non-positive product count; long product names affecting alignment.

2. exercises/02.cs
- Input: numeric list plus precision value from 0 to 6.
- Output: count, sum, average, minimum, and maximum with selected precision.
- Edge cases: empty numeric input; precision outside 0..6.

## Checkpoint

- [ ] I can explain the core ideas of this module.
- [ ] I can run and modify example/main.cs.
- [ ] I completed exercises/01.cs.
- [ ] I completed exercises/02.cs.
- [ ] I validated at least one edge case for each exercise.