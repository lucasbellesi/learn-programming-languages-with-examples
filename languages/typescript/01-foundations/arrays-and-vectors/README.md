# Arrays and Typed Sequences (TypeScript)

This module uses typed arrays to store, transform, and summarize groups of values.

## Learning Metadata

- Difficulty: Beginner.
- Estimated Time: 20-35 minutes.
- Prerequisites: 01-foundations/control-flow and 01-foundations/functions.
- Cross-Language Lens: Compare vector, List<T>, slices, Python lists, and TypeScript arrays as different tradeoffs for dynamic sequence work.

## Learning Outcomes

- `FND-SEQ-01`: Store and traverse ordered collections safely.
- `FND-SEQ-02`: Handle empty collections and index boundaries explicitly.

## Quick Run

Run from the repository root:

~~~bash
python scripts/automation.py run-module --module-path languages/typescript/01-foundations/arrays-and-vectors
~~~

## Topics Covered

- Typed arrays such as number[] and string[].
- Looping with for...of and array methods.
- Filtering and mapping without losing readability.
- Computing summary values from a list.

## Common Pitfalls

- Chaining too many array methods for a beginner example.
- Forgetting that arrays are mutable by default.
- Skipping empty-list checks before accessing index 0.

## Cross-Language Notes

- In TypeScript, read this module through the native focus ?Arrays and Typed Sequences?; the shared folder name remains stable for side-by-side navigation.
- Use structural types, Node APIs, and explicit reference conventions to demonstrate how to store and traverse ordered collections safely.
- Compare observable behavior with the other tracks when learning to handle empty collections and index boundaries explicitly; equivalent evidence matters more than identical syntax.

## Exercise Focus

- exercises/01.ts: read integers and print them in reverse order.
- exercises/02.ts: remove duplicates while preserving the first appearance order.

### Exercise Specs

1. exercises/01.ts
- Input: an integer N followed by N integers.
- Output: the integers from last to first.
- Edge cases: N <= 0 should print an error; repeated values should stay repeated in reverse.

2. exercises/02.ts
- Input: one line of space-separated words.
- Output: the unique words in first-seen order.
- Edge cases: empty input should print an error; already unique input should stay unchanged.

## Check Your Work

Run from the repository root after implementing a starter:

```bash
python scripts/automation.py check-exercise --language typescript --level 01-foundations --module arrays-and-vectors --exercise 01
```

Change `--exercise 01` to `--exercise 02` for the second task. Consult `exercises/solutions/` only after making a complete attempt.

## Checkpoint

- [ ] I can explain the main TypeScript idea in this module.
- [ ] I can run the example and describe the output.
- [ ] I completed exercises/01.ts.
- [ ] I completed exercises/02.ts.
