# Constructors and Invariants (C#)

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
python scripts/automation.py run-module --module-path languages/csharp/03-advanced/constructors-and-invariants
~~~

## Topics Covered

- Constructor guards that normalize invalid inputs.
- Defining invariants as always-true class rules.
- Safe update methods that reject invalid transitions.
- Reporting operation success without breaking object state.

## Common Pitfalls

- Accepting invalid constructor values and fixing later.
- Updating private state directly from callers.
- Returning success when an invalid update was ignored.

## Exercise Focus

- exercises/01.cs: bank account with non-negative balance invariant.
- exercises/02.cs: date model with month/day validation.

### Exercise Specs

1. exercises/01.cs
- Input: initial balance and transaction values.
- Output: updated balance with validity checks.
- Edge cases: negative initial balance; withdrawal beyond balance.

2. exercises/02.cs
- Input: month and day values.
- Output: valid/invalid date result.
- Edge cases: month out of range; day out of range for month.

## Check Your Work

Run from the repository root after implementing a starter:

```bash
python scripts/automation.py check-exercise --language csharp --level 03-advanced --module constructors-and-invariants --exercise 01
```

Change `--exercise 01` to `--exercise 02` for the second task. Consult `exercises/solutions/` only after making a complete attempt.

## Checkpoint

- [ ] I can define clear invariants for a class.
- [ ] I can enforce invariants in constructors and methods.
- [ ] I can reject invalid updates safely.
- [ ] I completed exercises/01.cs.
- [ ] I completed exercises/02.cs.
