# Strong/Weak References and Ownership (Python)

This module adapts smart pointer ideas to Python references, ownership slots, and `weakref`.

## Learning Metadata

- Difficulty: Advanced.
- Estimated Time: 45-60 minutes.
- Prerequisites: `04-expert/memory-management-and-raii`.
- Cross-Language Lens: Compare explicit ownership tools in C++ with managed references, pointer conventions, and weak-reference patterns elsewhere.

## Learning Outcomes

- `EXP-OWN-01`: Model exclusive, shared, and non-owning relationships idiomatically.
- `EXP-OWN-02`: Prevent leaks, cycles, and stale observations in ownership graphs.

## Quick Run

Run from the repository root:

~~~bash
python scripts/automation.py run-module --module-path languages/python/04-expert/smart-pointers-in-depth
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

## Cross-Language Notes

- Python treats references as the default, so this module compares C++ smart pointers with aliasing, cloning, and `weakref`.
- Compared with C++, ownership is far less encoded in syntax and much more about disciplined object relationships.
- The main teaching goal is to notice when sharing is intentional and when it is accidental.

## Exercise Focus

- exercises/01.py: move an owned note between holders.
- exercises/02.py: observe cache entries through `weakref.ref`.

### Exercise Specs

1. exercises/01.py
- Input: source and destination note titles, or `empty`, one per line.
- Output: ownership transfer logs before and after moving.
- Edge cases: moving from an empty holder; destination already occupied.

2. exercises/02.py
- Input: `alive`, `expired`, or `missing` cache scenario.
- Output: alive/expired cache lookup logs.
- Edge cases: expired or detached reference; missing reference.

## Check Your Work

Run from the repository root after implementing a starter:

```bash
python scripts/automation.py check-exercise --language python --level 04-expert --module smart-pointers-in-depth --exercise 01
```

Change `--exercise 01` to `--exercise 02` for the second task. Consult `exercises/solutions/` only after making a complete attempt.

## Checkpoint

- [ ] I can explain strong vs weak references in Python.
- [ ] I can model ownership transfer with reassignment and `None`.
- [ ] I can choose when a weak observer is appropriate.
- [ ] I completed exercises/01.py.
- [ ] I completed exercises/02.py.

