# Java Track

## Scope and Status

This track currently covers `01-foundations`, `02-core`, and `03-advanced` as a Java 21 MVP, including projects through `03-advanced` and assessments through `02-core`. Expert modules and later checkpoints are planned for future iterations.

- 8/8 foundations modules implemented.
- 6/6 core modules implemented.
- 5/5 advanced modules implemented (`structs-and-classes`, `constructors-and-invariants`, `copy-and-move-semantics`, `inheritance-and-polymorphism`, `templates-basics`).
- 0/5 expert modules implemented.
- 3/4 projects implemented (`01-foundations`, `02-core`, `03-advanced`).
- 2/4 assessments implemented (`01-foundations`, `02-core`).
- Uses Java 21 LTS with direct `javac` and `java` commands; no Maven or Gradle yet.

## Prerequisites

- Java 21 JDK available as `javac` and `java`
- Terminal (PowerShell or Bash)

## Quick Start

1. Open [01-foundations](./01-foundations/README.md), then continue with [02-core](./02-core/README.md).
2. Run one module example:

~~~bash
javac -d build/java languages/java/01-foundations/types-and-io/example/Main.java
java -cp build/java Main
~~~

3. Solve:
- `01-foundations/types-and-io/exercises/Exercise01.java`
- `01-foundations/types-and-io/exercises/Exercise02.java`

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
- Projects
  - [01-foundations](./projects/01-foundations/README.md)
  - [02-core](./projects/02-core/README.md)
  - [03-advanced](./projects/03-advanced/README.md)
- Assessments
  - [01-foundations](./assessments/01-foundations/README.md)
  - [02-core](./assessments/02-core/README.md)

## Progress Tracking

- [CHECKLIST.md](./CHECKLIST.md)

## Cross-Language Parity Strategy

- Start by comparing Java foundations and core modules with the C#, Go, Python, TypeScript, and C++ tracks.
- Keep Java examples single-file until the learner has practiced classes, methods, and compilation basics.
- Defer Maven, Gradle, packages, and project layout until a later Java-specific expansion.
