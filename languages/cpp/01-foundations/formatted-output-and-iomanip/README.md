# Formatted Output and iomanip (C++)

This module teaches readable numeric and table output formatting.

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
python scripts/automation.py run-module --module-path languages/cpp/01-foundations/formatted-output-and-iomanip
~~~

## More Examples

- `example/main.cpp` is the primary runnable sample for this module.
- Try one variation: copy it to `example/variation.cpp`, change one rule, and compare outputs.

## Topics Covered

- `std::fixed` and `std::setprecision`.
- `std::setw` for column alignment.
- Left/right alignment with `std::left` and `std::right`.
- Building simple text tables.

## Common Pitfalls

- Forgetting `<iomanip>` include.
- Mixing inconsistent precision across rows.
- Not reserving enough width for long labels.

## Cross-Language Notes

- In C++, read this module through the native focus ?Formatted Output and iomanip?; the shared folder name remains stable for side-by-side navigation.
- Use explicit value/reference semantics and standard-library types to demonstrate how to produce stable human-readable tabular and numeric output.
- Compare observable behavior with the other tracks when learning to choose precision, alignment, and labels appropriate to the data; equivalent evidence matters more than identical syntax.

## Exercise Focus

- `exercises/01.cpp`: print invoice table with aligned columns.
- `exercises/02.cpp`: print statistics with configurable precision.

### Exercise Specs

1. `exercises/01.cpp`
- Input: three item lines (`name unitPrice quantity`).
- Output: aligned invoice table and grand total.
- Edge cases: quantity `0`; unit price with many decimals.

2. `exercises/02.cpp`
- Input: precision value and a list of numbers.
- Output: average/min/max with chosen decimal precision.
- Edge cases: precision `0`; negative numbers.

## Check Your Work

Run from the repository root after implementing a starter:

```bash
python scripts/automation.py check-exercise --language cpp --level 01-foundations --module formatted-output-and-iomanip --exercise 01
```

Change `--exercise 01` to `--exercise 02` for the second task. Consult `exercises/solutions/` only after making a complete attempt.

## Checkpoint

- [ ] I can produce aligned columns with `setw`.
- [ ] I can control decimal display with `setprecision`.
- [ ] I can build readable reports for numeric data.
- [ ] I completed both exercises.
