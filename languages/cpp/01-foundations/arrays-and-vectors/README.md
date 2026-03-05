# Arrays and Vectors

This module introduces collections of values and how to process them safely.

## Why This Matters

Real programs rarely use only one variable. You often work with lists of data such as scores, prices, or names.

## Topics Covered

### Arrays

- Fixed size, decided at creation time.
- Good for small, known-size data.

```cpp
int scores[3] = {85, 90, 78};
```

### `std::vector`

- Dynamic size (can grow or shrink).
- Safer and more flexible than raw arrays for beginners.

```cpp
std::vector<int> scores;
scores.push_back(85);
scores.push_back(90);
```

### Iteration

- Index-based loops when you need positions.
- Range-based loops when you only need values.

### Common Pitfalls

- Accessing out-of-range indexes (for example, `values[values.size()]`).
- Mixing signed `int` and unsigned `size_t` carelessly.
- Forgetting to validate how many values were read from input.

## Checkpoint

- [ ] I understand fixed-size arrays vs dynamic vectors.
- [ ] I can add values to a vector using `push_back`.
- [ ] I can loop through values and compute results.
- [ ] I completed `exercises/01.cpp` and `exercises/02.cpp`.
