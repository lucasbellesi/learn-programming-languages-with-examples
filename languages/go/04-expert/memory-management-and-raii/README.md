# Memory Management and RAII (Go)

This module introduces deterministic cleanup in Go through `defer` and explicit `Close` methods.

## Learning Metadata

- Difficulty: Advanced.
- Estimated Time: 45-60 minutes.
- Prerequisites: `01-foundations/scope-and-lifetime-basics`, `03-advanced/structs-and-classes`.
- Cross-Language Lens: Contrast deterministic cleanup in C++ with `IDisposable`, `defer`, and context-manager style resource handling.

## Quick Run

~~~bash
go run example/main.go
~~~

## Topics Covered

- Releasing owned resources with `Close`.
- Scheduling cleanup with `defer`.
- Guarding methods after a resource is closed.
- Distinguishing garbage collection from deterministic cleanup.

## Common Pitfalls

- Assuming the garbage collector closes resources on time.
- Forgetting to `defer` cleanup right after successful acquisition.
- Reusing a resource after it has been closed.
- Returning early without releasing an owned handle.

## Exercise Focus

- exercises/01.go: owned integer buffer with deterministic cleanup.
- exercises/02.go: scope guard that proves nested cleanup order.

### Exercise Specs

1. exercises/01.go
- Input: integer `n`, then `n` integers.
- Output: sum and reversed sequence.
- Edge cases: `n <= 0`; invalid integer input.

2. exercises/02.go
- Input: none.
- Output: enter/exit logs proving automatic cleanup.
- Edge cases: nested scopes; final active counter must return to zero.

## Checkpoint

- [ ] I can explain how `defer` gives deterministic cleanup in Go.
- [ ] I can write a small type with `Close`.
- [ ] I can avoid using a resource after cleanup.
- [ ] I completed exercises/01.go.
- [ ] I completed exercises/02.go.
