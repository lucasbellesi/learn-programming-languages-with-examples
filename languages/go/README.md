# Go Track

## Scope and Status

This track currently covers `01-foundations` and mirrors the C++ concept order.

- 8/8 foundations modules implemented.
- Same module naming as C++, Python, and C# for parity.

## Prerequisites

- Go 1.22+ (`go` command available)
- Terminal (PowerShell or Bash)

## Quick Start

1. Open [01-foundations](./01-foundations/README.md).
2. Run one module example:

~~~bash
go run 01-foundations/types-and-io/example/main.go
~~~

3. Solve:
- `01-foundations/types-and-io/exercises/01.go`
- `01-foundations/types-and-io/exercises/02.go`

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

## Progress Tracking

- [CHECKLIST.md](./CHECKLIST.md)

## Cross-Language Parity Strategy

- Complete one module in Go and then the same module in C++.
- Compare explicit error handling, type declarations, and control flow style.
- Document at least three implementation differences per module pair.
- Track next parity milestones in [LANGUAGE_PARITY_MATRIX.md](../../LANGUAGE_PARITY_MATRIX.md).
