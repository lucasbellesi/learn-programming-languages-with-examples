# Managed Memory, Close, and defer (Go)

This module introduces deterministic cleanup in Go through `defer` and explicit `Close` methods.

## Learning Metadata

- Difficulty: Advanced.
- Estimated Time: 45-60 minutes.
- Prerequisites: `01-foundations/scope-and-lifetime-basics`, `03-advanced/structs-and-classes`.
- Cross-Language Lens: Contrast deterministic cleanup in C++ with `IDisposable`, `defer`, and context-manager style resource handling.

## Learning Outcomes

- `EXP-MEM-01`: Explain the language's resource and memory lifetime model.
- `EXP-MEM-02`: Guarantee deterministic cleanup for non-memory resources.

## Quick Run

Run from the repository root:

~~~bash
python scripts/automation.py run-module --module-path languages/go/04-expert/memory-management-and-raii
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

## Cross-Language Notes

- Go replaces RAII with explicit cleanup plus `defer`, so release timing is scheduled by code rather than object destruction.
- Compared with C++, the ownership idea stays useful even though the cleanup mechanism changes completely.
- This module is really about disciplined release paths, not about emulating destructors.

## Exercise Focus

- exercises/01.go: owned integer buffer with deterministic cleanup.
- exercises/02.go: scope guard that proves nested cleanup order.

### Exercise Specs

1. exercises/01.go
- Input: integer `n`, then `n` integers.
- Output: sum and reversed sequence.
- Edge cases: `n <= 0`; invalid integer input.

2. exercises/02.go
- Input: positive nesting depth.
- Output: enter/exit logs proving automatic cleanup.
- Edge cases: nested scopes; final active counter must return to zero.

## Check Your Work

Run from the repository root after implementing a starter:

```bash
python scripts/automation.py check-exercise --language go --level 04-expert --module memory-management-and-raii --exercise 01
```

Change `--exercise 01` to `--exercise 02` for the second task. Consult `exercises/solutions/` only after making a complete attempt.

## Checkpoint

- [ ] I can explain how `defer` gives deterministic cleanup in Go.
- [ ] I can write a small type with `Close`.
- [ ] I can avoid using a resource after cleanup.
- [ ] I completed exercises/01.go.
- [ ] I completed exercises/02.go.

