# Constructors and Invariants (C#)

This module shows how constructors enforce valid object state.

## Learning Metadata

- Difficulty: Intermediate.
- Estimated Time: 35-50 minutes.
- Prerequisites: `03-advanced/structs-and-classes`.
- Cross-Language Lens: Compare constructor rules, validation points, and object setup guarantees in each track.

## Quick Run

~~~bash
dotnet run --project example/constructors-and-invariants-example.csproj
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

## Checkpoint

- [ ] I can define clear invariants for a class.
- [ ] I can enforce invariants in constructors and methods.
- [ ] I can reject invalid updates safely.
- [ ] I completed exercises/01.cs.
- [ ] I completed exercises/02.cs.
