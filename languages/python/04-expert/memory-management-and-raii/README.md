# Memory Management and RAII (Python)

This module introduces deterministic cleanup in Python through context managers.

## Learning Metadata

- Difficulty: Advanced.
- Estimated Time: 45-60 minutes.
- Prerequisites: `01-foundations/scope-and-lifetime-basics`, `03-advanced/structs-and-classes`.
- Cross-Language Lens: Contrast deterministic cleanup in C++ with `IDisposable`, `defer`, and context-manager style resource handling.

## Learning Outcomes

- `EXP-MEM-01`: Explain the language's resource and memory lifetime model.
- `EXP-MEM-02`: Guarantee deterministic cleanup for non-memory resources.

## Quick Run

~~~bash
python example/main.py
~~~

## Topics Covered

- Automatic cleanup with `with`.
- Implementing `__enter__` and `__exit__`.
- Guarding methods after a resource has been released.
- Distinguishing garbage collection from deterministic scope cleanup.

## Common Pitfalls

- Assuming cleanup will happen at a predictable time without a context manager.
- Forgetting to release resources on early returns.
- Reusing an object after it has already been closed.
- Using `__del__` as the primary cleanup strategy.

## Cross-Language Notes

- Python maps this idea to context managers, `try/finally`, and explicit `close` methods rather than destructor-based RAII.
- Compared with C++, object lifetime and resource cleanup are related but not identical concerns.
- The learner goal is to make release points obvious and reliable.

## Exercise Focus

- exercises/01.py: owned integer buffer with deterministic cleanup.
- exercises/02.py: scope guard that proves nested cleanup order.

### Exercise Specs

1. exercises/01.py
- Input: integer `n`, then `n` integers.
- Output: sum and reversed sequence.
- Edge cases: `n <= 0`; invalid integer input.

2. exercises/02.py
- Input: none.
- Output: enter/exit logs proving automatic cleanup.
- Edge cases: nested scopes; final active counter must return to zero.

## Check Your Work

Run from the repository root after implementing a starter:

```bash
python scripts/automation.py check-exercise --language python --level 04-expert --module memory-management-and-raii --exercise 01
```

Change `--exercise 01` to `--exercise 02` for the second task. Consult `exercises/solutions/` only after making a complete attempt.

## Checkpoint

- [ ] I can explain why `with` gives deterministic cleanup.
- [ ] I can write a small context manager.
- [ ] I can prevent work on a closed resource.
- [ ] I completed exercises/01.py.
- [ ] I completed exercises/02.py.

