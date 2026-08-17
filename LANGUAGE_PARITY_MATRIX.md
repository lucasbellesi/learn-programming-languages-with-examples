# Language Parity Matrix

This matrix tracks module and checkpoint parity across C++, C#, Go, Java, Python, and TypeScript.

- Canonical order is defined by the C++ track.
- All six tracks have structural parity through `04-expert`.
- Parity has four independent dimensions: `S` structure, `G` guided starter,
  `C` mature contracts, and `I` idiomatic adaptation.
- `Done` is reserved for `S+G+C+I`; file presence alone is `S`.

The current migration status is `S+G+I` for modules. Contract maturity is tracked
separately because legacy solution-oracle cases are being replaced by explicit,
mutation-resistant assertions. Projects are guided; assessments intentionally remain
independent.

## Foundations (`01-foundations`)

| Module | C++ | C# | Go | Java | Python | TypeScript |
| --- | --- | --- | --- | --- | --- | --- |
| types-and-io | Done | Done | Done | Done | Done | Done |
| operators-and-expressions | Done | Done | Done | Done | Done | Done |
| control-flow | Done | Done | Done | Done | Done | Done |
| functions | Done | Done | Done | Done | Done | Done |
| arrays-and-vectors | Done | Done | Done | Done | Done | Done |
| strings | Done | Done | Done | Done | Done | Done |
| scope-and-lifetime-basics | Done | Done | Done | Done | Done | Done |
| formatted-output-and-iomanip | Done | Done | Done | Done | Done | Done |

## Core (`02-core`)

Current parity progress in non-C++ tracks:

- C#: `6/6` modules complete
- Go: `6/6` modules complete
- Java: `6/6` modules complete
- Python: `6/6` modules complete
- TypeScript: `6/6` modules complete

| Order | Module | C++ | C# | Go | Java | Python | TypeScript |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | input-validation | Done | Done | Done | Done | Done | Done |
| 2 | algorithms-basics | Done | Done | Done | Done | Done | Done |
| 3 | file-io-basics | Done | Done | Done | Done | Done | Done |
| 4 | sorting-and-searching | Done | Done | Done | Done | Done | Done |
| 5 | maps-and-frequency-counting | Done | Done | Done | Done | Done | Done |
| 6 | error-handling-and-defensive-programming | Done | Done | Done | Done | Done | Done |

## Advanced and Expert

Current parity progress in non-C++ tracks:

- C#: `5/5` modules complete in `03-advanced`, `5/5` in `04-expert`
- Go: `5/5` modules complete in `03-advanced`, `5/5` in `04-expert`
- Java: `5/5` modules complete in `03-advanced`, `5/5` in `04-expert`
- Python: `5/5` modules complete in `03-advanced`, `5/5` in `04-expert`
- TypeScript: `5/5` modules complete in `03-advanced`, `5/5` in `04-expert`

### Advanced (`03-advanced`)

| Order | Module | C++ | C# | Go | Java | Python | TypeScript |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | structs-and-classes | Done | Done | Done | Done | Done | Done |
| 2 | constructors-and-invariants | Done | Done | Done | Done | Done | Done |
| 3 | copy-and-move-semantics | Done | Done | Done | Done | Done | Done |
| 4 | inheritance-and-polymorphism | Done | Done | Done | Done | Done | Done |
| 5 | templates-basics | Done | Done | Done | Done | Done | Done |

`04-expert` projects and assessments are now implemented across all six active tracks.

### Expert (`04-expert`)

| Order | Module | C++ | C# | Go | Java | Python | TypeScript |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | memory-management-and-raii | Done | Done | Done | Done | Done | Done |
| 2 | smart-pointers-in-depth | Done | Done | Done | Done | Done | Done |
| 3 | concurrency-basics | Done | Done | Done | Done | Done | Done |
| 4 | performance-and-profiling-basics | Done | Done | Done | Done | Done | Done |
| 5 | modularization-and-build-structure | Done | Done | Done | Done | Done | Done |

## Checkpoint Parity

`Done` means the checkpoint has a README plus runnable starter and solution trees.

### Projects

| Checkpoint | C++ | C# | Go | Java | Python | TypeScript |
| --- | --- | --- | --- | --- | --- | --- |
| 01-foundations | Done | Done | Done | Done | Done | Done |
| 02-core | Done | Done | Done | Done | Done | Done |
| 03-advanced | Done | Done | Done | Done | Done | Done |
| 04-expert | Done | Done | Done | Done | Done | Done |

### Assessments

| Checkpoint | C++ | C# | Go | Java | Python | TypeScript |
| --- | --- | --- | --- | --- | --- | --- |
| 01-foundations | Done | Done | Done | Done | Done | Done |
| 02-core | Done | Done | Done | Done | Done | Done |
| 03-advanced | Done | Done | Done | Done | Done | Done |
| 04-expert | Done | Done | Done | Done | Done | Done |
