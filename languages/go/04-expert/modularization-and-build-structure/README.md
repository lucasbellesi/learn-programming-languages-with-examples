# Modularization and Build Structure (Go)

This module introduces separation of responsibilities and package-oriented design in Go.

## Quick Run

~~~bash
go run example/main.go example/pricing.go example/formatting.go
~~~

## Topics Covered

- Separating calculation, formatting, and orchestration responsibilities across files.
- Keeping `main` thin and coordination-focused.
- Designing helper functions and types that live outside the entrypoint.
- Treating file and package layout as part of program design.

## Common Pitfalls

- Putting every concern directly into `main`.
- Mixing formatting and business rules in one function.
- Designing helpers with hidden side effects.
- Treating module structure as an afterthought.

## Exercise Focus

- exercises/01.go: separate invoice calculations into focused helpers.
- exercises/02.go: build reusable command operations consumed by one caller.

### Exercise Specs

1. exercises/01.go
- Input: subtotal, discount percent, tax percent.
- Output: subtotal breakdown and final total.
- Edge cases: negative subtotal; percentages outside valid ranges.

2. exercises/02.go
- Input: command name and integer operands.
- Output: result from a reusable operation registry.
- Edge cases: unsupported command; division by zero.

## Checkpoint

- [ ] I can separate coordination code from reusable helpers.
- [ ] I can describe why a helper type or function exists.
- [ ] I can keep `main` focused on flow, not every implementation detail.
- [ ] I completed exercises/01.go.
- [ ] I completed exercises/02.go.
