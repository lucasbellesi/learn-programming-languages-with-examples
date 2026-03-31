# Modularization and Build Structure (C#)

This module introduces multi-file organization and project references in C#.

## Learning Metadata

- Difficulty: Expert.
- Estimated Time: 30-45 minutes.
- Prerequisites: `02-core/file-io-basics`, `03-advanced/structs-and-classes`.
- Cross-Language Lens: Compare headers and source files, project references, packages, and Python modules as ways to separate responsibilities.
## Quick Run

~~~bash
dotnet run --project example/modularization-and-build-structure-example.csproj
~~~

## Topics Covered

- Splitting domain logic, formatting, and application flow across separate files.
- Grouping reusable code under a namespace.
- Referencing one project from another with `ProjectReference`.
- Keeping console entrypoints thin and coordination-focused.

## Common Pitfalls

- Putting every class into `main.cs` even when responsibilities diverge.
- Mixing formatting, calculations, and input flow in one method.
- Forgetting to include files explicitly when default compile items are disabled.
- Treating project layout as an afterthought instead of part of design.

## Exercise Focus

- exercises/01.cs: separate invoice calculations into focused helper types.
- exercises/02.cs: build reusable command operations consumed by two callers.

### Exercise Specs

1. exercises/01.cs
- Input: subtotal, discount percent, tax percent.
- Output: subtotal breakdown and final total.
- Edge cases: negative subtotal; percentages outside valid ranges.

2. exercises/02.cs
- Input: command name and integer operands.
- Output: result from a reusable operation registry.
- Edge cases: unsupported command; division by zero.

## Checkpoint

- [ ] I can explain why a namespace or project boundary exists.
- [ ] I can separate coordination code from reusable services.
- [ ] I can describe how `ProjectReference` affects a build.
- [ ] I completed exercises/01.cs.
- [ ] I completed exercises/02.cs.
