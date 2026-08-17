# Smart Pointers in Depth (C++)

This module expands ownership modeling with `unique_ptr`, `shared_ptr`, and `weak_ptr`.

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
python scripts/automation.py run-module --module-path languages/cpp/04-expert/smart-pointers-in-depth
~~~

## More Examples

- `example/main.cpp` is the primary runnable sample for this module.
- Try one variation: copy it to `example/variation.cpp`, change one rule, and compare outputs.

## Topics Covered

- Exclusive ownership with `std::unique_ptr`.
- Shared ownership with `std::shared_ptr`.
- Non-owning observation with `std::weak_ptr`.
- Avoiding ownership cycles.

## Common Pitfalls

- Overusing `shared_ptr` where `unique_ptr` is sufficient.
- Forgetting to break cycles.
- Using raw pointers for owned lifetime-sensitive resources.

## Cross-Language Notes

- This is the canonical smart-pointer track: ownership, borrowing, and shared lifetime are explicit language tools here.
- Other tracks adapt the idea with references, nil checks, weak references, or clone helpers instead of true smart pointers.
- Use this module as the baseline when comparing what "ownership" means elsewhere.

## Exercise Focus

- `exercises/01.cpp`: refactor raw-owner object to `unique_ptr`.
- `exercises/02.cpp`: break parent/child cycle with `weak_ptr`.

### Exercise Specs

1. `exercises/01.cpp`
- Input: none.
- Output: object construction/destruction messages.
- Edge cases: transfer ownership with move; null pointer checks.

2. `exercises/02.cpp`
- Input: none.
- Output: cycle-safe parent/child relationship logs.
- Edge cases: expired weak references; parent reset behavior.

## Check Your Work

Run from the repository root after implementing a starter:

```bash
python scripts/automation.py check-exercise --language cpp --level 04-expert --module smart-pointers-in-depth --exercise 01
```

Change `--exercise 01` to `--exercise 02` for the second task. Consult `exercises/solutions/` only after making a complete attempt.

## Checkpoint

- [ ] I can choose between `unique_ptr` and `shared_ptr`.
- [ ] I can use `weak_ptr` for non-owning links.
- [ ] I can prevent ownership cycles.
- [ ] I completed both exercises.

