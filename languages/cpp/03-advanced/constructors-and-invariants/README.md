# Constructors and Invariants

This module shows how constructors enforce valid object state.

## Learning Metadata

- Difficulty: Intermediate.
- Estimated Time: 35-50 minutes.
- Prerequisites: `03-advanced/structs-and-classes`.
- Cross-Language Lens: Compare constructor rules, validation points, and object setup guarantees in each track.

## Learning Outcomes

- `ADV-INV-01`: Construct objects only in valid states.
- `ADV-INV-02`: Keep mutations from violating established invariants.

## Quick Run

Run from the repository root:

~~~bash
python scripts/automation.py run-module --module-path languages/cpp/03-advanced/constructors-and-invariants
~~~

## More Examples

- `example/main.cpp` is the primary runnable sample for this module.
- Try one variation: copy it to `example/variation.cpp`, change one rule, and compare outputs.

## Topics Covered

- Constructor initialization.
- Invariants as always-true rules.
- Validation in constructors and setters.
- Safe update methods.

## Common Pitfalls

- Leaving objects in invalid states.
- Validating only at use-time, not construction-time.
- Ignoring boundary conditions.

## Exercise Focus

- `exercises/01.cpp`: bank account with non-negative balance.
- `exercises/02.cpp`: date class with month/day validation.

### Exercise Specs

1. `exercises/01.cpp`
- Input: initial balance and transaction values.
- Output: updated balance with validity checks.
- Edge cases: negative initial balance; withdrawal beyond balance.

2. `exercises/02.cpp`
- Input: month and day values.
- Output: valid/invalid date result.
- Edge cases: month out of range; day out of range for month.

## Check Your Work

Run from the repository root after implementing a starter:

```bash
python scripts/automation.py check-exercise --language cpp --level 03-advanced --module constructors-and-invariants --exercise 01
```

Change `--exercise 01` to `--exercise 02` for the second task. Consult `exercises/solutions/` only after making a complete attempt.

## Checkpoint

- [ ] I can define clear invariants for a class.
- [ ] I can enforce invariants in constructors and methods.
- [ ] I can reject invalid updates safely.
- [ ] I completed both exercises.
