# Memory Management and RAII (Python)

This module introduces deterministic cleanup in Python through context managers.

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

## Checkpoint

- [ ] I can explain why `with` gives deterministic cleanup.
- [ ] I can write a small context manager.
- [ ] I can prevent work on a closed resource.
- [ ] I completed exercises/01.py.
- [ ] I completed exercises/02.py.
