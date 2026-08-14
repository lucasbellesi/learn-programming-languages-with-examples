# Maps and Frequency Counting

This module uses `Map` to count repeated values and summarize categorical data.

## Learning Metadata

- Difficulty: Intermediate.
- Estimated Time: 30-45 minutes.
- Prerequisites: `02-core/algorithms-basics` and `01-foundations/strings`.
- Cross-Language Lens: Compare `Map` usage with `std::map`, `Dictionary`, Go maps, and Python dictionaries for the same counting task.

## Learning Outcomes

- `COR-MAP-01`: Use key-value collections to aggregate and retrieve data.
- `COR-MAP-02`: Define normalization and missing-key behavior explicitly.

## Quick Run

Run from the repository root:

~~~bash
python scripts/automation.py run-module --module-path languages/typescript/02-core/maps-and-frequency-counting
~~~

## Topics Covered

- Counting repeated tokens with `Map`.
- Updating counts without missing the first occurrence case.
- Sorting `(key, value)` pairs by frequency.
- Turning raw text into summary tables.

## Common Pitfalls

- Forgetting to initialize the first count.
- Sorting map entries lexicographically when frequency order is required.
- Treating empty tokens as meaningful categories.

## Exercise Focus

- exercises/01.ts: build a word-frequency table.
- exercises/02.ts: print the most frequent word and its count.

### Exercise Specs

1. exercises/01.ts
- Input: one line of space-separated words.
- Output: one frequency line per distinct word.
- Edge cases: empty input; repeated casing; single repeated word.

2. exercises/02.ts
- Input: one line of space-separated words.
- Output: the most frequent word and its count.
- Edge cases: ties should keep the first word that reaches the best count; empty input should print an error.

## Check Your Work

Run from the repository root after implementing a starter:

```bash
python scripts/automation.py check-exercise --language typescript --level 02-core --module maps-and-frequency-counting --exercise 01
```

Change `--exercise 01` to `--exercise 02` for the second task. Consult `exercises/solutions/` only after making a complete attempt.

## Checkpoint

- [ ] I can count repeated values with `Map`.
- [ ] I can convert map entries into a sorted summary.
- [ ] I can explain how the first-occurrence case differs from later updates.
- [ ] I completed exercises/01.ts.
- [ ] I completed exercises/02.ts.
