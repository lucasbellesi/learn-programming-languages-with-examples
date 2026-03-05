# Control Flow

Control flow decides which code runs and how many times it runs.

## Quick Run

```bash
g++ -std=c++17 -Wall -Wextra -pedantic example/main.cpp -o control_flow_example
./control_flow_example
```

## Topics Covered

### `if / else`

Use conditional logic to choose between branches.

```cpp
if (value > 0) {
    // positive
} else if (value < 0) {
    // negative
} else {
    // zero
}
```

### `switch`

Use `switch` for multi-way branching on integral values (such as menu options).

```cpp
switch (option) {
    case 1:
        // action
        break;
    default:
        // fallback
        break;
}
```

### Loops (`for`, `while`)

- `for`: ideal when the number of iterations is known.
- `while`: ideal when repeating until a condition changes.

### `break` and `continue`

- `break`: exits the nearest loop immediately.
- `continue`: skips the rest of the current iteration and moves to the next one.

## Common Pitfalls

- Forgetting braces when an `if` block has multiple statements.
- Accidentally creating infinite loops by not updating loop variables.
- Using `switch` without `break`, causing unintentional fallthrough.

## Exercise Focus

- `exercises/01.cpp`: implement classic FizzBuzz logic with conditions.
- `exercises/02.cpp`: process values until a sentinel and compute average safely.

## Checkpoint

- [ ] I can branch using `if / else`.
- [ ] I can use `switch` for menu-like decisions.
- [ ] I can write `for` and `while` loops.
- [ ] I understand when to use `break` and `continue`.
- [ ] I completed `exercises/01.cpp` and `exercises/02.cpp`.
