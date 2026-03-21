# Maps and Frequency Counting (C#)

This module introduces dictionary-based counting patterns for grouped data.

## Quick Run

~~~bash
dotnet run --project example/maps-and-frequency-counting-example.csproj
~~~

## Topics Covered

- Counting occurrences with dictionary lookups.
- Building frequency tables from text and numeric input.
- Iterating key/value pairs in sorted-key order.
- Using frequency data to answer higher-level questions.

## Common Pitfalls

- Assuming missing keys exist before initialization.
- Iterating unsorted dictionary keys when deterministic output is needed.
- Forgetting to normalize or filter input before counting.

## Exercise Focus

- exercises/01.cs: count digit frequencies.
- exercises/02.cs: first non-repeating character.

### Exercise Specs

1. exercises/01.cs
- Input: integer count `n`, then `n` integers (`0-9`).
- Output: frequency per digit.
- Edge cases: missing digits should show count `0`; all values same digit.

2. exercises/02.cs
- Input: one lowercase string.
- Output: first non-repeating character or message if none.
- Edge cases: all repeated characters; one-character string.

## Checkpoint

- [ ] I can use dictionaries for counting tasks.
- [ ] I can build frequency tables from sequences.
- [ ] I can use frequency data to answer higher-level questions.
- [ ] I completed exercises/01.cs.
- [ ] I completed exercises/02.cs.
