# Smart Pointers in Depth

This module expands ownership modeling with `unique_ptr`, `shared_ptr`, and `weak_ptr`.

## Learning Metadata

- Difficulty: Expert.
- Estimated Time: 40-55 minutes.
- Prerequisites: `04-expert/memory-management-and-raii`, `03-advanced/copy-and-move-semantics`.
- Cross-Language Lens: Compare explicit ownership in C++ with managed references, pointers, and weak observers in the other tracks.
## Quick Run

```bash
g++ -std=c++17 -Wall -Wextra -pedantic example/main.cpp -o smart_pointers_example
./smart_pointers_example
```

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

## Checkpoint

- [ ] I can choose between `unique_ptr` and `shared_ptr`.
- [ ] I can use `weak_ptr` for non-owning links.
- [ ] I can prevent ownership cycles.
- [ ] I completed both exercises.
