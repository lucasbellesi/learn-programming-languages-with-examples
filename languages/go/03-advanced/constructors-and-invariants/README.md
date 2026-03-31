# Constructors and Invariants (Go)

This module shows how constructors enforce valid object state.

## Learning Metadata

- Difficulty: Intermediate.
- Estimated Time: 35-50 minutes.
- Prerequisites: `03-advanced/structs-and-classes`.
- Cross-Language Lens: Compare constructor rules, validation points, and object setup guarantees in each track.

## Quick Run

~~~bash
go run example/main.go
~~~

## Topics Covered

- Constructor-style functions that normalize invalid values.
- Defining invariants as always-true struct rules.
- Safe update methods with explicit success/failure booleans.
- Keeping state transitions behind methods.

## Common Pitfalls

- Building structs directly and bypassing constructor guards.
- Mutating invariant-critical fields from outside methods.
- Ignoring failed updates and assuming state changed.

## Exercise Focus

- exercises/01.go: bank account with non-negative balance invariant.
- exercises/02.go: date model with month/day validation.

### Exercise Specs

1. exercises/01.go
- Input: initial balance and transaction values.
- Output: updated balance with validity checks.
- Edge cases: negative initial balance; withdrawal beyond balance.

2. exercises/02.go
- Input: month and day values.
- Output: valid/invalid date result.
- Edge cases: month out of range; day out of range for month.

## Checkpoint

- [ ] I can define clear invariants for a type.
- [ ] I can enforce invariants in constructor functions and methods.
- [ ] I can reject invalid updates safely.
- [ ] I completed exercises/01.go.
- [ ] I completed exercises/02.go.
