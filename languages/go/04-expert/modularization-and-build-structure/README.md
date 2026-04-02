# Modularization and Build Structure (Go)

This module introduces separation of responsibilities and package-oriented design in Go.

## Learning Metadata

- Difficulty: Advanced.
- Estimated Time: 45-60 minutes.
- Prerequisites: `02-core/file-io-basics`, `03-advanced/structs-and-classes`.
- Cross-Language Lens: Compare packages, projects, modules, and compilation units as different ways to scale beyond one file.

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

## Cross-Language Notes

- Go makes modularity feel lighter than C++ or C#, but package and file boundaries still encode real design choices.
- Compared with Python or TypeScript, build and import rules are simpler but more opinionated.
- The useful comparison is how much ceremony each language needs before reuse becomes natural.

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

