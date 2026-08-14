# Maps and Frequency Counting

This module introduces associative containers for counting/grouping data.

## Learning Metadata

- Difficulty: Intermediate.
- Estimated Time: 30-45 minutes.
- Prerequisites: `01-foundations/arrays-and-vectors`, `01-foundations/strings`.
- Cross-Language Lens: Compare hash map ergonomics, missing-key behavior, and default-value patterns across the six active languages.

## Learning Outcomes

- `COR-MAP-01`: Use key-value collections to aggregate and retrieve data.
- `COR-MAP-02`: Define normalization and missing-key behavior explicitly.

## Quick Run

Run from the repository root:

~~~bash
python scripts/automation.py run-module --module-path languages/cpp/02-core/maps-and-frequency-counting
~~~

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

## Check Your Work

Run from the repository root after implementing a starter:

```bash
python scripts/automation.py check-exercise --language cpp --level 02-core --module maps-and-frequency-counting --exercise 01
```

Change `--exercise 01` to `--exercise 02` for the second task. Consult `exercises/solutions/` only after making a complete attempt.

## Checkpoint

- [ ] I can use maps for counting tasks.
- [ ] I can build frequency tables from sequences.
- [ ] I can use frequency data to answer higher-level questions.
- [ ] I completed both exercises.
