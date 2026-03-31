# Maps and Frequency Counting (Python)

This module introduces dictionary-based counting patterns for grouped data.

## Learning Metadata

- Difficulty: Intermediate.
- Estimated Time: 30-45 minutes.
- Prerequisites: `01-foundations/arrays-and-vectors`, `01-foundations/strings`.
- Cross-Language Lens: Compare hash map ergonomics, missing-key behavior, and default-value patterns across the four languages.

## Quick Run

~~~bash
python example/main.py
~~~

## Topics Covered

- Counting occurrences with dictionary lookups.
- Building frequency tables from text and numeric input.
- Producing deterministic output by sorting keys before printing.
- Using frequency data to answer higher-level questions.

## Common Pitfalls

- Assuming missing keys already exist.
- Printing unsorted dictionary keys when deterministic output is expected.
- Forgetting to filter separators before counting symbols.

## Exercise Focus

- exercises/01.py: count digit frequencies.
- exercises/02.py: first non-repeating character.

### Exercise Specs

1. exercises/01.py
- Input: integer count `n`, then `n` integers (`0-9`).
- Output: frequency per digit.
- Edge cases: missing digits should show count `0`; all values same digit.

2. exercises/02.py
- Input: one lowercase string.
- Output: first non-repeating character or message if none.
- Edge cases: all repeated characters; one-character string.

## Checkpoint

- [ ] I can use dictionaries for counting tasks.
- [ ] I can build frequency tables from sequences.
- [ ] I can use frequency data to answer higher-level questions.
- [ ] I completed exercises/01.py.
- [ ] I completed exercises/02.py.
