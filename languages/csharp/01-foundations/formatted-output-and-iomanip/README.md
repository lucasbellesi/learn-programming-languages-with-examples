# Formatted Console Output (C#)

This module practices table-style output, alignment, and precision control.

## Learning Metadata

- Difficulty: Beginner.
- Estimated Time: 20-35 minutes.
- Prerequisites: `01-foundations/types-and-io`, `01-foundations/operators-and-expressions`.
- Cross-Language Lens: Compare stream manipulators, format strings, `fmt`, and Python formatting for the same reporting task.

## Learning Outcomes

- `FND-FMT-01`: Produce stable human-readable tabular and numeric output.
- `FND-FMT-02`: Choose precision, alignment, and labels appropriate to the data.

## Quick Run

Run from the repository root:

~~~bash
python scripts/automation.py run-module --module-path languages/csharp/01-foundations/formatted-output-and-iomanip
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

## Cross-Language Notes

- In C#, read this module through the native focus ?Formatted Console Output?; the shared folder name remains stable for side-by-side navigation.
- Use static types, .NET collections, and managed-resource patterns to demonstrate how to produce stable human-readable tabular and numeric output.
- Compare observable behavior with the other tracks when learning to choose precision, alignment, and labels appropriate to the data; equivalent evidence matters more than identical syntax.

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

## Check Your Work

Run from the repository root after implementing a starter:

```bash
python scripts/automation.py check-exercise --language csharp --level 01-foundations --module formatted-output-and-iomanip --exercise 01
```

Change `--exercise 01` to `--exercise 02` for the second task. Consult `exercises/solutions/` only after making a complete attempt.

## Checkpoint

- [ ] I can explain the core ideas of this module.
- [ ] I can run and modify example/main.cs.
- [ ] I completed exercises/01.cs.
- [ ] I completed exercises/02.cs.
- [ ] I validated at least one edge case for each exercise.
