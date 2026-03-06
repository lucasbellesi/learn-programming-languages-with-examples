# Arrays and Vectors

This module introduces fixed-size and dynamic collections in C++.

## Quick Run

```bash
g++ -std=c++17 -Wall -Wextra -pedantic example/main.cpp -o arrays_and_vectors_example
./arrays_and_vectors_example
```

## Topics Covered

- Fixed-size arrays (`T values[N]`).
- Dynamic arrays with `std::vector<T>`.
- Index-based and range-based iteration.
- Safe indexing and input count validation.

## Common Pitfalls

- Accessing out-of-range indexes.
- Mixing signed and unsigned indexes carelessly.
- Forgetting to validate `n` before reading values.

## Exercise Focus

- `exercises/01.cpp`: print user-provided integers in reverse order.
- `exercises/02.cpp`: count frequency of a target number in a vector.

### Exercise Specs

1. `exercises/01.cpp`
- Input: integer `n`, then `n` integers.
- Output: values in reverse order.
- Edge cases: `n <= 0` should print a friendly message; repeated values should remain repeated in output.

2. `exercises/02.cpp`
- Input: integer `n`, then `n` integers, then one target integer.
- Output: number of occurrences of target.
- Edge cases: target not found should print `0`; all values equal target should print `n`.

## Checkpoint

- [ ] I can choose between arrays and vectors.
- [ ] I can loop over vectors safely.
- [ ] I can solve frequency/counting tasks with vectors.
- [ ] I completed both exercises.
