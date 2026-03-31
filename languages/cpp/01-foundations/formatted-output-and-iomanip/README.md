# Formatted Output and iomanip

This module teaches readable numeric and table output formatting.

## Learning Metadata

- Difficulty: Beginner.
- Estimated Time: 20-35 minutes.
- Prerequisites: `01-foundations/types-and-io`, `01-foundations/operators-and-expressions`.
- Cross-Language Lens: Compare stream manipulators, format strings, `fmt`, and Python formatting for the same reporting task.

## Quick Run

```bash
g++ -std=c++17 -Wall -Wextra -pedantic example/main.cpp -o iomanip_example
./iomanip_example
```

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

## Checkpoint

- [ ] I can produce aligned columns with `setw`.
- [ ] I can control decimal display with `setprecision`.
- [ ] I can build readable reports for numeric data.
- [ ] I completed both exercises.
