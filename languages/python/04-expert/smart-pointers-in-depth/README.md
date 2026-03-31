# Smart Pointers in Depth (Python)

This module adapts smart pointer ideas to Python references, ownership slots, and `weakref`.

## Learning Metadata

- Difficulty: Expert.
- Estimated Time: 40-55 minutes.
- Prerequisites: `04-expert/memory-management-and-raii`, `03-advanced/copy-and-move-semantics`.
- Cross-Language Lens: Compare explicit ownership in C++ with managed references, pointers, and weak observers in the other tracks.
## Quick Run

~~~bash
python example/main.py
~~~

## Topics Covered

- Moving an owned reference by reassigning it and clearing the previous owner.
- Using `None` as an explicit empty ownership slot.
- Observing objects without keeping them alive via `weakref.ref`.
- Distinguishing strong references from weak observers.

## Common Pitfalls

- Assuming a weak reference behaves like a normal strong reference.
- Forgetting to clear the old owner after a transfer.
- Dereferencing optional references without checking for `None`.
- Keeping accidental strong references in caches or observers.

## Exercise Focus

- exercises/01.py: move an owned note between holders.
- exercises/02.py: observe cache entries through `weakref.ref`.

### Exercise Specs

1. exercises/01.py
- Input: none.
- Output: ownership transfer logs before and after moving.
- Edge cases: moving from an empty holder; destination already occupied.

2. exercises/02.py
- Input: none.
- Output: alive/expired cache lookup logs.
- Edge cases: expired weak reference; cache miss.

## Checkpoint

- [ ] I can explain strong vs weak references in Python.
- [ ] I can model ownership transfer with reassignment and `None`.
- [ ] I can choose when a weak observer is appropriate.
- [ ] I completed exercises/01.py.
- [ ] I completed exercises/02.py.
