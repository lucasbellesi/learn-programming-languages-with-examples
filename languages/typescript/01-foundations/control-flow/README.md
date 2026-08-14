# Control Flow

This module practices branching and loops to keep TypeScript programs predictable.

## Learning Metadata

- Difficulty: Beginner.
- Estimated Time: 20-35 minutes.
- Prerequisites: 01-foundations/types-and-io and 01-foundations/operators-and-expressions.
- Cross-Language Lens: Compare braces-and-loops in C++, C#, Go, and TypeScript with Python indentation while keeping the control decisions the same.

## Learning Outcomes

- `FND-CFL-01`: Select branches that cover normal and boundary conditions.
- `FND-CFL-02`: Write terminating loops and reason about their invariants.

## Quick Run

Run from the repository root:

~~~bash
python scripts/automation.py run-module --module-path languages/typescript/01-foundations/control-flow
~~~

## Topics Covered

- if / else if / else decision trees.
- switch for simple menu handling.
- for and while loops for repeated work.
- Guard clauses that stop invalid cases early.

## Common Pitfalls

- Using switch when a small helper array or map would be clearer.
- Forgetting to update loop state.
- Nesting conditionals so deeply that the rule becomes hard to read.

## Exercise Focus

- exercises/01.ts: map a numeric menu choice to a command label.
- exercises/02.ts: print a countdown and classify the last number reached.

### Exercise Specs

1. exercises/01.ts
- Input: one integer menu choice.
- Output: the command label for that choice.
- Edge cases: unknown menu options should print Unknown option; negative numbers should still be handled.

2. exercises/02.ts
- Input: one non-negative integer.
- Output: a countdown and a final classification line.
- Edge cases: 0 should still print one line; negative input should print an error.

## Check Your Work

Run from the repository root after implementing a starter:

```bash
python scripts/automation.py check-exercise --language typescript --level 01-foundations --module control-flow --exercise 01
```

Change `--exercise 01` to `--exercise 02` for the second task. Consult `exercises/solutions/` only after making a complete attempt.

## Checkpoint

- [ ] I can explain the main TypeScript idea in this module.
- [ ] I can run the example and describe the output.
- [ ] I completed exercises/01.ts.
- [ ] I completed exercises/02.ts.
