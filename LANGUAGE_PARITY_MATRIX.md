# Language Parity Matrix

This matrix tracks module and checkpoint parity across C++, C#, Go, and Python.

- Canonical order is defined by the C++ track.
- Current priority is to extend checkpoint parity beyond `02-core` without fragmenting the curriculum.
- Status labels:
  - `Done`: module implemented with example, exercises, and README.
  - `Planned`: module not implemented yet, already queued in order.

## Foundations (`01-foundations`)

| Module | C++ | C# | Go | Python |
| --- | --- | --- | --- | --- |
| types-and-io | Done | Done | Done | Done |
| operators-and-expressions | Done | Done | Done | Done |
| control-flow | Done | Done | Done | Done |
| functions | Done | Done | Done | Done |
| arrays-and-vectors | Done | Done | Done | Done |
| strings | Done | Done | Done | Done |
| scope-and-lifetime-basics | Done | Done | Done | Done |
| formatted-output-and-iomanip | Done | Done | Done | Done |

## Core (`02-core`)

Current parity progress in non-C++ tracks:

- C#: `6/6` modules complete
- Go: `6/6` modules complete
- Python: `6/6` modules complete

| Order | Module | C++ | C# | Go | Python |
| --- | --- | --- | --- | --- | --- |
| 1 | input-validation | Done | Done | Done | Done |
| 2 | algorithms-basics | Done | Done | Done | Done |
| 3 | file-io-basics | Done | Done | Done | Done |
| 4 | sorting-and-searching | Done | Done | Done | Done |
| 5 | maps-and-frequency-counting | Done | Done | Done | Done |
| 6 | error-handling-and-defensive-programming | Done | Done | Done | Done |

## Advanced and Expert

Current parity progress in non-C++ tracks:

- C#: `5/5` modules complete in `03-advanced`
- Go: `5/5` modules complete in `03-advanced`
- Python: `5/5` modules complete in `03-advanced`

### Advanced (`03-advanced`) - Current Expansion Queue

| Order | Module | C++ | C# | Go | Python |
| --- | --- | --- | --- | --- | --- |
| 1 | structs-and-classes | Done | Done | Done | Done |
| 2 | constructors-and-invariants | Done | Done | Done | Done |
| 3 | copy-and-move-semantics | Done | Done | Done | Done |
| 4 | inheritance-and-polymorphism | Done | Done | Done | Done |
| 5 | templates-basics | Done | Done | Done | Done |

`04-expert` has started in C# with `modularization-and-build-structure`; broader expert parity is still planned.

### Expert (`04-expert`) - Early Expansion

| Order | Module | C++ | C# | Go | Python |
| --- | --- | --- | --- | --- | --- |
| 1 | memory-management-and-raii | Done | Planned | Planned | Planned |
| 2 | smart-pointers-in-depth | Done | Planned | Planned | Planned |
| 3 | concurrency-basics | Done | Planned | Planned | Planned |
| 4 | performance-and-profiling-basics | Done | Planned | Planned | Planned |
| 5 | modularization-and-build-structure | Done | Done | Planned | Planned |

## Checkpoint Parity

Status labels:

- `Done`: checkpoint implemented with README and runnable entrypoint.
- `Planned`: checkpoint not implemented yet.

### Projects

| Checkpoint | C++ | C# | Go | Python |
| --- | --- | --- | --- | --- |
| 01-foundations | Done | Done | Done | Done |
| 02-core | Done | Done | Done | Done |
| 03-advanced | Done | Planned | Planned | Planned |
| 04-expert | Done | Planned | Planned | Planned |

### Assessments

| Checkpoint | C++ | C# | Go | Python |
| --- | --- | --- | --- | --- |
| 01-foundations | Done | Done | Done | Done |
| 02-core | Done | Done | Done | Done |
| 03-advanced | Done | Planned | Planned | Planned |
| 04-expert | Done | Planned | Planned | Planned |
