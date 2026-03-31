# Constructors and Invariants (Python)

This module shows how constructors enforce valid object state.

## Learning Metadata

- Difficulty: Intermediate.
- Estimated Time: 35-50 minutes.
- Prerequisites: `03-advanced/structs-and-classes`.
- Cross-Language Lens: Compare constructor rules, validation points, and object setup guarantees in each track.

## Quick Run

~~~bash
python example/main.py
~~~

## Topics Covered

- Constructor guards that normalize invalid values.
- Defining invariants as always-true object rules.
- Safe update methods that reject invalid transitions.
- Returning explicit operation success values.

## Common Pitfalls

- Accepting invalid constructor values and fixing later.
- Writing directly into internal fields from outside methods.
- Ignoring failed updates and assuming state changed.

## Exercise Focus

- exercises/01.py: bank account with non-negative balance invariant.
- exercises/02.py: date model with month/day validation.

### Exercise Specs

1. exercises/01.py
- Input: initial balance and transaction values.
- Output: updated balance with validity checks.
- Edge cases: negative initial balance; withdrawal beyond balance.

2. exercises/02.py
- Input: month and day values.
- Output: valid/invalid date result.
- Edge cases: month out of range; day out of range for month.

## Checkpoint

- [ ] I can define clear invariants for a class.
- [ ] I can enforce invariants in constructors and methods.
- [ ] I can reject invalid updates safely.
- [ ] I completed exercises/01.py.
- [ ] I completed exercises/02.py.
