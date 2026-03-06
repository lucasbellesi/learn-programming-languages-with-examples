# Memory Management and RAII

This module introduces safe ownership patterns in modern C++.

## Why It Matters

Many C++ bugs come from incorrect memory or resource handling.  
RAII and smart pointers reduce those bugs by tying cleanup to object lifetime.

## Quick Run

```bash
g++ -std=c++17 -Wall -Wextra -pedantic example/main.cpp -o memory_raii_example
./memory_raii_example
```

On Windows (MSYS2 shell), run:

```bash
./memory_raii_example.exe
```

## Topics Covered

### Stack vs Heap

- Stack objects are destroyed automatically at scope end.
- Heap objects need ownership and cleanup strategy.

### RAII (Resource Acquisition Is Initialization)

Acquire resources in constructors and release them in destructors.

### Smart Pointers

- `std::unique_ptr<T>`: single owner.
- `std::shared_ptr<T>`: shared ownership (use carefully).
- Prefer `unique_ptr` unless shared ownership is required.

## Common Pitfalls

- Using raw `new`/`delete` directly in beginner/intermediate code.
- Copying `unique_ptr` (it must be moved).
- Creating ownership cycles with `shared_ptr`.

## Exercise Focus

- `exercises/01.cpp`: use `std::unique_ptr<int[]>` for dynamic arrays safely.
- `exercises/02.cpp`: model RAII with a scope-based guard class.

## Checkpoint

- [ ] I can explain ownership with `unique_ptr`.
- [ ] I understand how destructors enforce cleanup.
- [ ] I can model scope-based resource management.
- [ ] I completed both exercises.
