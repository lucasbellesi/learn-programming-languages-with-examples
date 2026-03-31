# Language Parity Matrix

This matrix tracks module and checkpoint parity across C++, C#, Go, Python, and TypeScript.

- Canonical order is defined by the C++ track.
- C++, C#, Go, and Python now reach module and checkpoint parity through `04-expert`.
- TypeScript is the newest incremental track with `01-foundations` implemented first.
- Status labels:
  - `Done`: module implemented with example, exercises, and README.
  - `Planned`: module not implemented yet, already queued in order.

## Foundations (`01-foundations`)

| Module | C++ | C# | Go | Python | TypeScript |
| --- | --- | --- | --- | --- | --- |
| types-and-io | Done | Done | Done | Done | Done |
| operators-and-expressions | Done | Done | Done | Done | Done |
| control-flow | Done | Done | Done | Done | Done |
| functions | Done | Done | Done | Done | Done |
| arrays-and-vectors | Done | Done | Done | Done | Done |
| strings | Done | Done | Done | Done | Done |
| scope-and-lifetime-basics | Done | Done | Done | Done | Done |
| formatted-output-and-iomanip | Done | Done | Done | Done | Done |

## Core (`02-core`)

Current parity progress in non-C++ tracks:

- C#: `6/6` modules complete
- Go: `6/6` modules complete
- Python: `6/6` modules complete
- TypeScript: `0/6` modules complete, foundations delivered first

| Order | Module | C++ | C# | Go | Python | TypeScript |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | input-validation | Done | Done | Done | Done | Planned |
| 2 | algorithms-basics | Done | Done | Done | Done | Planned |
| 3 | file-io-basics | Done | Done | Done | Done | Planned |
| 4 | sorting-and-searching | Done | Done | Done | Done | Planned |
| 5 | maps-and-frequency-counting | Done | Done | Done | Done | Planned |
| 6 | error-handling-and-defensive-programming | Done | Done | Done | Done | Planned |

## Advanced and Expert

Current parity progress in non-C++ tracks:

- C#: `5/5` modules complete in `03-advanced`, `5/5` in `04-expert`
- Go: `5/5` modules complete in `03-advanced`, `5/5` in `04-expert`
- Python: `5/5` modules complete in `03-advanced`, `5/5` in `04-expert`
- TypeScript: `03-advanced` and `04-expert` planned after foundations and core

### Advanced (`03-advanced`) - Current Expansion Queue

| Order | Module | C++ | C# | Go | Python | TypeScript |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | structs-and-classes | Done | Done | Done | Done | Planned |
| 2 | constructors-and-invariants | Done | Done | Done | Done | Planned |
| 3 | copy-and-move-semantics | Done | Done | Done | Done | Planned |
| 4 | inheritance-and-polymorphism | Done | Done | Done | Done | Planned |
| 5 | templates-basics | Done | Done | Done | Done | Planned |

`04-expert` projects and assessments are now implemented across C#, Go, and Python.

### Expert (`04-expert`)

| Order | Module | C++ | C# | Go | Python | TypeScript |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | memory-management-and-raii | Done | Done | Done | Done | Planned |
| 2 | smart-pointers-in-depth | Done | Done | Done | Done | Planned |
| 3 | concurrency-basics | Done | Done | Done | Done | Planned |
| 4 | performance-and-profiling-basics | Done | Done | Done | Done | Planned |
| 5 | modularization-and-build-structure | Done | Done | Done | Done | Planned |

## Checkpoint Parity

Status labels:

- `Done`: checkpoint implemented with README and runnable entrypoint.
- `Planned`: checkpoint not implemented yet.

### Projects

| Checkpoint | C++ | C# | Go | Python | TypeScript |
| --- | --- | --- | --- | --- | --- |
| 01-foundations | Done | Done | Done | Done | Done |
| 02-core | Done | Done | Done | Done | Planned |
| 03-advanced | Done | Done | Done | Done | Planned |
| 04-expert | Done | Done | Done | Done | Planned |

### Assessments

| Checkpoint | C++ | C# | Go | Python | TypeScript |
| --- | --- | --- | --- | --- | --- |
| 01-foundations | Done | Done | Done | Done | Done |
| 02-core | Done | Done | Done | Done | Planned |
| 03-advanced | Done | Done | Done | Done | Planned |
| 04-expert | Done | Done | Done | Done | Planned |
