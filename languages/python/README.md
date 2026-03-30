# Python Track

## Scope and Status

This track currently covers `01-foundations`, `02-core`, `03-advanced`, and `04-expert`, plus the first checkpoint layer in `projects` and `assessments`.

- 8/8 foundations modules implemented.
- 6/6 core modules implemented (`input-validation`, `algorithms-basics`, `file-io-basics`, `sorting-and-searching`, `maps-and-frequency-counting`, `error-handling-and-defensive-programming`).
- 5/5 advanced modules implemented (`structs-and-classes`, `constructors-and-invariants`, `copy-and-move-semantics`, `inheritance-and-polymorphism`, `templates-basics`).
- 5/5 expert modules implemented (`memory-management-and-raii`, `smart-pointers-in-depth`, `concurrency-basics`, `performance-and-profiling-basics`, `modularization-and-build-structure`).
- 3/4 projects implemented (`01-foundations`, `02-core`, `03-advanced`).
- 2/4 assessments implemented (`01-foundations`, `02-core`).
- Same module naming as C++, Go, and C# for parity.

## Prerequisites

- Python 3.10+ available as `python`
- Terminal (PowerShell or Bash)

## Quick Start

1. Open [01-foundations](./01-foundations/README.md).
2. Run one module example:

~~~bash
python 01-foundations/types-and-io/example/main.py
~~~

3. Solve:
- `01-foundations/types-and-io/exercises/01.py`
- `01-foundations/types-and-io/exercises/02.py`

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
  - [memory-management-and-raii](./04-expert/memory-management-and-raii/README.md)
  - [smart-pointers-in-depth](./04-expert/smart-pointers-in-depth/README.md)
  - [concurrency-basics](./04-expert/concurrency-basics/README.md)
  - [performance-and-profiling-basics](./04-expert/performance-and-profiling-basics/README.md)
  - [modularization-and-build-structure](./04-expert/modularization-and-build-structure/README.md)
- [projects](./projects/README.md)
  - [01-foundations](./projects/01-foundations/README.md)
  - [02-core](./projects/02-core/README.md)
  - [03-advanced](./projects/03-advanced/README.md)
- [assessments](./assessments/README.md)
  - [01-foundations](./assessments/01-foundations/README.md)
  - [02-core](./assessments/02-core/README.md)

## Progress Tracking

- [CHECKLIST.md](./CHECKLIST.md)

## Cross-Language Parity Strategy

- Complete one module or checkpoint in Python and then the same artifact in C++.
- Compare readability, typing, and standard library approaches.
- Document at least three implementation differences per module pair.
- Track next parity milestones in [LANGUAGE_PARITY_MATRIX.md](../../LANGUAGE_PARITY_MATRIX.md).
