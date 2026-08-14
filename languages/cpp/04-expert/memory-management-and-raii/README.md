# Memory Management and RAII

This module introduces ownership and deterministic cleanup in C++.

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
python scripts/automation.py run-module --module-path languages/cpp/04-expert/memory-management-and-raii
~~~

## More Examples

- `example/main.cpp` is the primary runnable sample for this module.
- Try one variation: copy it to `example/variation.cpp`, change one rule, and compare outputs.

## Topics Covered

- Stack vs heap lifetime.
- RAII and destructor-driven cleanup.
- `std::unique_ptr` ownership.
- Move semantics for exclusive ownership transfer.

## Common Pitfalls

- Raw `new`/`delete` in modern educational code.
- Attempting to copy `unique_ptr`.
- Mixing ownership and non-ownership pointers incorrectly.

## Cross-Language Notes

- This is the canonical RAII version: cleanup is tied to scope exit through destructors.
- Compare this with C#, Python, Go, and TypeScript, where resource cleanup is explicit even when memory is managed.
- The transferable idea is lifetime discipline, not the exact destructor syntax.

## Exercise Focus

- `exercises/01.cpp`: dynamic array with `std::unique_ptr<int[]>`.
- `exercises/02.cpp`: RAII guard with automatic scope cleanup.

### Exercise Specs

1. `exercises/01.cpp`
- Input: integer `n`, then `n` integers.
- Output: sum and reversed sequence.
- Edge cases: `n <= 0` message; negative values in sequence.

2. `exercises/02.cpp`
- Input: none (scope demonstration).
- Output: enter/exit logs proving automatic cleanup.
- Edge cases: nested scopes; final counter should return to zero.

## Check Your Work

Run from the repository root after implementing a starter:

```bash
python scripts/automation.py check-exercise --language cpp --level 04-expert --module memory-management-and-raii --exercise 01
```

Change `--exercise 01` to `--exercise 02` for the second task. Consult `exercises/solutions/` only after making a complete attempt.

## Checkpoint

- [ ] I can explain why RAII prevents leaks.
- [ ] I can use `unique_ptr` for owned dynamic memory.
- [ ] I can design classes with cleanup in destructors.
- [ ] I completed both exercises.

