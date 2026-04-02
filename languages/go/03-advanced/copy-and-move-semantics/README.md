# Copy and Move Semantics (Go)

This module introduces copying behavior and transfer-style updates with slices and pointers.

## Learning Metadata

- Difficulty: Intermediate.
- Estimated Time: 35-50 minutes.
- Prerequisites: `03-advanced/structs-and-classes`, `03-advanced/constructors-and-invariants`.
- Cross-Language Lens: Use this module to contrast C++ ownership transfer with reference-heavy behavior in C#, Go, and Python.

## Quick Run

~~~bash
go run example/main.go
~~~

## Topics Covered

- Difference between copying slice headers and copying underlying data.
- Transfer-style state handoff between struct instances.
- Deep-copy helpers to avoid shared mutable backing arrays.
- Intentional mutation boundaries with pointer receivers.

## Common Pitfalls

- Assuming `=` creates an independent deep copy for slices.
- Mutating a shared backing array by accident.
- Forgetting to reset source state after transfer operations.

## Cross-Language Notes

- Go reframes this topic around values, pointers, and assignment behavior instead of true move semantics.
- Compared with C++ and C#, there is less special syntax and more emphasis on choosing simple data ownership conventions.
- The useful comparison is explicit pointer and value tradeoffs versus richer language-level transfer rules.

## Exercise Focus

- exercises/01.go: resource-like buffer with clone and transfer operations.
- exercises/02.go: insertion flow that contrasts shared vs copied slices.

### Exercise Specs

1. exercises/01.go
- Input: buffer size and values.
- Output: logs showing clone and transfer behavior.
- Edge cases: zero-size buffer; repeated transfers.

2. exercises/02.go
- Input: text values to store.
- Output: size and content checks after copy vs shared assignment.
- Edge cases: empty strings; repeated insertions.

## Checkpoint

- [ ] I can explain shallow copy vs deep copy in slices.
- [ ] I can model safe transfer-style ownership changes.
- [ ] I can avoid unintentional shared-backing-array mutations.
- [ ] I completed exercises/01.go.
- [ ] I completed exercises/02.go.
