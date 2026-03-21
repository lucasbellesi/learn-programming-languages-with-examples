# C# Track

## Scope and Status

This track currently covers `01-foundations` and has started `02-core`.

- 8/8 foundations modules implemented.
- 4/6 core modules implemented (`input-validation`, `algorithms-basics`, `file-io-basics`, `sorting-and-searching`).
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

## Progress Tracking

- [CHECKLIST.md](./CHECKLIST.md)

## Cross-Language Parity Strategy

- Complete one module in C# and then the same module in C++.
- Compare type inference, object model conventions, and runtime tooling.
- Document at least three implementation differences per module pair.
- Track next parity milestones in [LANGUAGE_PARITY_MATRIX.md](../../LANGUAGE_PARITY_MATRIX.md).
