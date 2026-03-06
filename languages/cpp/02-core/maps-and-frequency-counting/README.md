# Maps and Frequency Counting

This module introduces associative containers for counting/grouping data.

## Quick Run

```bash
g++ -std=c++17 -Wall -Wextra -pedantic example/main.cpp -o maps_frequency_example
./maps_frequency_example
```

## More Examples

- `example/top-k-frequency.cpp`:

```bash
g++ -std=c++17 -Wall -Wextra -pedantic example/top-k-frequency.cpp -o maps_top_k_frequency
./maps_top_k_frequency
```

## Topics Covered

- `std::map<Key, Value>` basics.
- Frequency counting patterns.
- Iterating sorted key/value pairs.
- Simple text token counting.

## Common Pitfalls

- Forgetting that `map[key]` creates missing keys.
- Using wrong key type for comparison needs.
- Not normalizing input before counting.

## Exercise Focus

- `exercises/01.cpp`: count digit frequencies.
- `exercises/02.cpp`: first non-repeating character.

### Exercise Specs

1. `exercises/01.cpp`
- Input: integer count `n`, then `n` integers (`0-9`).
- Output: frequency per digit.
- Edge cases: missing digits should show count `0`; all values same digit.

2. `exercises/02.cpp`
- Input: one lowercase string.
- Output: first non-repeating character or message if none.
- Edge cases: all repeated characters; one-character string.

## Checkpoint

- [ ] I can use maps for counting tasks.
- [ ] I can build frequency tables from sequences.
- [ ] I can use frequency data to answer higher-level questions.
- [ ] I completed both exercises.
