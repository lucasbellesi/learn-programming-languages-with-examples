# Structs and Classes

This module introduces object modeling with `struct` and `class` in C++.

## Why It Matters

As programs grow, related data and behavior should be grouped together.  
`struct` and `class` help you model real entities clearly.

## Quick Run

```bash
g++ -std=c++17 -Wall -Wextra -pedantic example/main.cpp -o structs_and_classes_example
./structs_and_classes_example
```

On Windows (MSYS2 shell), run:

```bash
./structs_and_classes_example.exe
```

## Topics Covered

### `struct` vs `class`

- `struct` members are `public` by default.
- `class` members are `private` by default.
- Both can have fields, methods, and constructors.

### Constructors

Constructors initialize objects when they are created.

```cpp
class Account {
public:
    Account(const std::string& ownerName, double initialBalance);
};
```

### Encapsulation

Keep object state private and expose safe methods (`deposit`, `withdraw`, getters).

## Common Pitfalls

- Exposing all fields publicly in classes that should protect state.
- Forgetting `const` on methods that do not modify object state.
- Not validating values in constructors or mutating methods.

## Exercise Focus

- `exercises/01.cpp`: model a rectangle with a `struct` and member methods.
- `exercises/02.cpp`: create a small class with private state and controlled updates.

## Checkpoint

- [ ] I can explain default access in `struct` and `class`.
- [ ] I can write and use constructors.
- [ ] I can protect state with private fields and public methods.
- [ ] I completed both exercises.
