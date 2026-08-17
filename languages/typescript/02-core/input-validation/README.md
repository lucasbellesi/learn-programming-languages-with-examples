# Input Validation

This module teaches defensive validation patterns for TypeScript console programs.

## Learning Metadata

- Difficulty: Intermediate.
- Estimated Time: 30-45 minutes.
- Prerequisites: `01-foundations/types-and-io` and `01-foundations/control-flow`.
- Cross-Language Lens: Compare retry-loop validation in TypeScript with the same logic in C++, C#, Go, and Python, especially where parsing APIs fail differently.

## Learning Outcomes

- `COR-VAL-01`: Reject malformed and out-of-domain input without corrupting state.
- `COR-VAL-02`: Design retry and termination behavior that cannot loop accidentally.

## Quick Run

Run from the repository root:

~~~bash
python scripts/automation.py run-module --module-path languages/typescript/02-core/input-validation
~~~

## Topics Covered

- Centralizing validation in helper functions.
- Separating parse failures from range failures.
- Keeping programs stable after invalid attempts.
- Reusing validation rules across prompts or datasets.

## Common Pitfalls

- Accepting parsed values before checking range constraints.
- Returning vague errors that hide why validation failed.
- Repeating the same checks inline instead of extracting helpers.

## Cross-Language Notes

- In TypeScript, read this module through the native focus ?Input Validation?; the shared folder name remains stable for side-by-side navigation.
- Use structural types, Node APIs, and explicit reference conventions to demonstrate how to reject malformed and out-of-domain input without corrupting state.
- Compare observable behavior with the other tracks when learning to design retry and termination behavior that cannot loop accidentally; equivalent evidence matters more than identical syntax.

## Exercise Focus

- exercises/01.ts: validate one integer in range `1..100` and print its square.
- exercises/02.ts: validate a score count and matching scores, then print the average.

### Exercise Specs

1. exercises/01.ts
- Input: one integer attempt.
- Output: square of the accepted value.
- Edge cases: non-numeric text; values below `1` or above `100`.

2. exercises/02.ts
- Input: score count in range `1..50`, followed by that many scores in range `0..100`.
- Output: average score.
- Edge cases: missing scores; invalid score values; boundary values `0` and `100`.

## Check Your Work

Run from the repository root after implementing a starter:

```bash
python scripts/automation.py check-exercise --language typescript --level 02-core --module input-validation --exercise 01
```

Change `--exercise 01` to `--exercise 02` for the second task. Consult `exercises/solutions/` only after making a complete attempt.

## Checkpoint

- [ ] I can validate both parsing and range constraints before using a value.
- [ ] I can keep error messages specific enough to explain what failed.
- [ ] I can reuse one helper across multiple validation points.
- [ ] I completed exercises/01.ts.
- [ ] I completed exercises/02.ts.
