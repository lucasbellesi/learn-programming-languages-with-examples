# Control Flow

Control flow decides which code runs and how many times it runs.

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

## Checkpoint

- [ ] I can branch using `if / else`.
- [ ] I can use `switch` for menu-like decisions.
- [ ] I can write `for` and `while` loops.
- [ ] I understand when to use `break` and `continue`.
- [ ] I completed `exercises/01.cpp` and `exercises/02.cpp`.
