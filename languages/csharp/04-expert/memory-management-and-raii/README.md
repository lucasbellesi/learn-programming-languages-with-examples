# Managed Memory and Deterministic Disposal (C#)

This module introduces deterministic cleanup patterns in managed C# code.

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
python scripts/automation.py run-module --module-path languages/csharp/04-expert/memory-management-and-raii
~~~

## Topics Covered

- `IDisposable` as the C# equivalent of deterministic scope cleanup.
- `using` and `using var` for automatic release at scope boundaries.
- Separating object lifetime from garbage collection timing.
- Releasing owned buffers or handles without relying on finalizers.

## Common Pitfalls

- Assuming the garbage collector closes files or releases resources immediately.
- Forgetting to guard methods against access after disposal.
- Using finalizers as the primary cleanup mechanism.
- Treating managed memory and unmanaged resources as the same lifetime problem.

## Cross-Language Notes

- Compare C++ destructor-driven cleanup with `IDisposable` and `using`: the intent is similar, but ordinary objects are not scope-cleaned automatically.
- This track keeps cleanup explicit so learners can see where the ownership boundary really lives.
- The key lesson is to separate managed memory from unmanaged resource lifetime.

## Exercise Focus

- exercises/01.cs: owned integer buffer with deterministic cleanup.
- exercises/02.cs: scope guard that proves nested cleanup order.

### Exercise Specs

1. exercises/01.cs
- Input: integer `n`, then `n` integers.
- Output: sum and reversed sequence.
- Edge cases: `n <= 0`; invalid integer input.

2. exercises/02.cs
- Input: positive nesting depth.
- Output: enter/exit logs proving automatic cleanup.
- Edge cases: nested scopes; final active counter returns to zero.

## Check Your Work

Run from the repository root after implementing a starter:

```bash
python scripts/automation.py check-exercise --language csharp --level 04-expert --module memory-management-and-raii --exercise 01
```

Change `--exercise 01` to `--exercise 02` for the second task. Consult `exercises/solutions/` only after making a complete attempt.

## Checkpoint

- [ ] I can explain why `IDisposable` is about deterministic cleanup, not general memory reclamation.
- [ ] I can use `using` or `using var` to scope owned resources.
- [ ] I can prevent work on an already disposed object.
- [ ] I completed exercises/01.cs.
- [ ] I completed exercises/02.cs.

