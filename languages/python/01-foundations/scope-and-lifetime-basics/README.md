# Scope and Lifetime Basics (Python)

This module practices variable lifetime in blocks and safe accumulation patterns.

## Learning Metadata

- Difficulty: Beginner.
- Estimated Time: 20-35 minutes.
- Prerequisites: `01-foundations/functions`, `01-foundations/control-flow`.
- Cross-Language Lens: Compare block scope everywhere, then contrast deterministic destruction in C++ with garbage-collected lifetime in the other tracks.

## Learning Outcomes

- `FND-SCP-01`: Predict name visibility across nested scopes.
- `FND-SCP-02`: Explain when values and resources cease to be usable.

## Quick Run

~~~bash
python example/main.py
~~~

## Topics Covered

- Variables declared in branches and loops.
- Accumulator patterns scoped to full function lifetime.
- Conditional assignment before use.
- Guard clauses for invalid ranges.

## Common Pitfalls

- Using values before they are assigned in all branches.
- Declaring accumulators inside loops by mistake.
- Skipping range validation for score or count inputs.

## Exercise Focus

- exercises/01.py: map numeric score ranges to a letter grade using branch-local logic.
- exercises/02.py: accumulate N integers and compute sum and average from shared state.

### Exercise Specs

1. exercises/01.py
- Input: integer score expected in the range 0..100.
- Output: single letter grade from A to F.
- Edge cases: scores below 0 or above 100; exact boundary values 60/70/80/90.

2. exercises/02.py
- Input: positive count and then count integer values.
- Output: sum and average values.
- Edge cases: count <= 0; negative numbers within the sequence.

## Check Your Work

Run from the repository root after implementing a starter:

```bash
python scripts/automation.py check-exercise --language python --level 01-foundations --module scope-and-lifetime-basics --exercise 01
```

Change `--exercise 01` to `--exercise 02` for the second task. Consult `exercises/solutions/` only after making a complete attempt.

## Checkpoint

- [ ] I can explain the core ideas of this module.
- [ ] I can run and modify example/main.py.
- [ ] I completed exercises/01.py.
- [ ] I completed exercises/02.py.
- [ ] I validated at least one edge case for each exercise.
