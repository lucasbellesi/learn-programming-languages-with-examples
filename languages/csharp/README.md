# C# Track

## Scope and Status

This track currently covers `01-foundations`, `02-core`, and `03-advanced`, plus the first checkpoint layer in `projects` and `assessments`.

- 8/8 foundations modules implemented.
- 6/6 core modules implemented (`input-validation`, `algorithms-basics`, `file-io-basics`, `sorting-and-searching`, `maps-and-frequency-counting`, `error-handling-and-defensive-programming`).
- 5/5 advanced modules implemented (`structs-and-classes`, `constructors-and-invariants`, `copy-and-move-semantics`, `inheritance-and-polymorphism`, `templates-basics`).
- Experimental expert start: `04-expert/modularization-and-build-structure` is available while the rest of the level remains planned.
- 2/4 projects implemented (`01-foundations`, `02-core`).
- 2/4 assessments implemented (`01-foundations`, `02-core`).
- Same module naming as C++, Python, and Go for parity.

## Prerequisites

- .NET SDK 8.0+ (`dotnet` command available)
- Terminal (PowerShell or Bash)

## Quick Start

1. Open [01-foundations](./01-foundations/README.md).
2. Run one module example:

~~~bash
dotnet run --project 01-foundations/types-and-io/example/types-and-io-example.csproj
~~~

3. Solve:
- `01-foundations/types-and-io/exercises/01.cs`
- `01-foundations/types-and-io/exercises/02.cs`

## Level and Module Map

- [01-foundations](./01-foundations/README.md)
  - [types-and-io](./01-foundations/types-and-io/README.md)
  - [operators-and-expressions](./01-foundations/operators-and-expressions/README.md)
  - [control-flow](./01-foundations/control-flow/README.md)
  - [functions](./01-foundations/functions/README.md)
  - [arrays-and-vectors](./01-foundations/arrays-and-vectors/README.md)
  - [strings](./01-foundations/strings/README.md)
  - [scope-and-lifetime-basics](./01-foundations/scope-and-lifetime-basics/README.md)
  - [formatted-output-and-iomanip](./01-foundations/formatted-output-and-iomanip/README.md)
- [02-core](./02-core/README.md)
  - [input-validation](./02-core/input-validation/README.md)
  - [algorithms-basics](./02-core/algorithms-basics/README.md)
  - [file-io-basics](./02-core/file-io-basics/README.md)
  - [sorting-and-searching](./02-core/sorting-and-searching/README.md)
  - [maps-and-frequency-counting](./02-core/maps-and-frequency-counting/README.md)
  - [error-handling-and-defensive-programming](./02-core/error-handling-and-defensive-programming/README.md)
- [03-advanced](./03-advanced/README.md)
  - [structs-and-classes](./03-advanced/structs-and-classes/README.md)
  - [constructors-and-invariants](./03-advanced/constructors-and-invariants/README.md)
  - [copy-and-move-semantics](./03-advanced/copy-and-move-semantics/README.md)
  - [inheritance-and-polymorphism](./03-advanced/inheritance-and-polymorphism/README.md)
  - [templates-basics](./03-advanced/templates-basics/README.md)
- [04-expert](./04-expert/README.md)
  - [modularization-and-build-structure](./04-expert/modularization-and-build-structure/README.md)
- [projects](./projects/README.md)
  - [01-foundations](./projects/01-foundations/README.md)
  - [02-core](./projects/02-core/README.md)
- [assessments](./assessments/README.md)
  - [01-foundations](./assessments/01-foundations/README.md)
  - [02-core](./assessments/02-core/README.md)

## Progress Tracking

- [CHECKLIST.md](./CHECKLIST.md)

## Cross-Language Parity Strategy

- Complete one module or checkpoint in C# and then the same artifact in C++.
- Compare type inference, object model conventions, and runtime tooling.
- Document at least three implementation differences per module pair.
- Track next parity milestones in [LANGUAGE_PARITY_MATRIX.md](../../LANGUAGE_PARITY_MATRIX.md).
