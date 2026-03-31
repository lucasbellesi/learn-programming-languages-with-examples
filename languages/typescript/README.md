# TypeScript Track

## Scope and Status

This track currently covers `01-foundations`, plus the first `projects` and `assessments` checkpoint for that level.

- 8/8 foundations modules implemented.
- 1/4 projects implemented (`01-foundations`).
- 1/4 assessments implemented (`01-foundations`).
- Same module naming as C++, C#, Go, and Python for parity.
- `02-core`, `03-advanced`, and `04-expert` are planned next.

## Prerequisites

- Node LTS with `npm` available
- Run `npm install` once at the repository root
- Terminal (PowerShell or Bash)

## Quick Start

1. Open [01-foundations](./01-foundations/README.md).
2. Build the TypeScript track:

~~~bash
npm run build:typescript
~~~

3. Run one module example:

~~~bash
node build/typescript/01-foundations/types-and-io/example/main.js
~~~

4. Solve:
- `01-foundations/types-and-io/exercises/01.ts`
- `01-foundations/types-and-io/exercises/02.ts`

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
- [projects](./projects/README.md)
  - [01-foundations](./projects/01-foundations/README.md)
- [assessments](./assessments/README.md)
  - [01-foundations](./assessments/01-foundations/README.md)

## Progress Tracking

- [CHECKLIST.md](./CHECKLIST.md)

## Cross-Language Parity Strategy

- Complete one TypeScript module or checkpoint and then the same artifact in C++.
- Compare explicit parsing, runtime flexibility, and static typing ergonomics.
- Document at least three implementation differences per module pair.
- Track next parity milestones in [LANGUAGE_PARITY_MATRIX.md](../../LANGUAGE_PARITY_MATRIX.md).
