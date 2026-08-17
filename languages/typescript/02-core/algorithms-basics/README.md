# Algorithms Basics

This module introduces core algorithm patterns over arrays in plain TypeScript.

## Learning Metadata

- Difficulty: Intermediate.
- Estimated Time: 30-45 minutes.
- Prerequisites: `01-foundations/arrays-and-vectors` and `01-foundations/functions`.
- Cross-Language Lens: Compare explicit loops with library helpers and notice when beginner-friendly code is clearer than a dense chain of methods.

## Learning Outcomes

- `COR-ALG-01`: Implement linear scans and accumulations with clear invariants.
- `COR-ALG-02`: Analyze behavior for empty, duplicate, and missing values.

## Quick Run

Run from the repository root:

~~~bash
python scripts/automation.py run-module --module-path languages/typescript/02-core/algorithms-basics
~~~

## Topics Covered

- Linear search for the first matching item.
- One-pass minimum and maximum updates.
- Counting matches while scanning once.
- Combining several statistics in a single traversal.

## Common Pitfalls

- Assuming arrays are non-empty before min/max logic.
- Using multiple passes when one traversal is enough.
- Hiding simple logic inside clever but unreadable helpers.

## Cross-Language Notes

- In TypeScript, read this module through the native focus ?Algorithms Basics?; the shared folder name remains stable for side-by-side navigation.
- Use structural types, Node APIs, and explicit reference conventions to demonstrate how to implement linear scans and accumulations with clear invariants.
- Compare observable behavior with the other tracks when learning to analyze behavior for empty, duplicate, and missing values; equivalent evidence matters more than identical syntax.

## Exercise Focus

- exercises/01.ts: find the first index of a target value.
- exercises/02.ts: compute minimum, maximum, and even count in one pass.

### Exercise Specs

1. exercises/01.ts
- Input: integer `n`, then `n` values, then a target.
- Output: first index of target or `-1`.
- Edge cases: `n <= 0`; target not present.

2. exercises/02.ts
- Input: integer `n`, then `n` values.
- Output: minimum, maximum, and even count.
- Edge cases: all odd numbers; all equal values; `n <= 0`.

## Check Your Work

Run from the repository root after implementing a starter:

```bash
python scripts/automation.py check-exercise --language typescript --level 02-core --module algorithms-basics --exercise 01
```

Change `--exercise 01` to `--exercise 02` for the second task. Consult `exercises/solutions/` only after making a complete attempt.

## Checkpoint

- [ ] I can implement linear search without relying on hidden helpers.
- [ ] I can compute multiple statistics in a single traversal.
- [ ] I can protect min/max logic against empty input.
- [ ] I completed exercises/01.ts.
- [ ] I completed exercises/02.ts.
