# Control Flow (C#)

This module practices branching, looping, and sentinel-driven iteration.

## Learning Metadata

- Difficulty: Beginner.
- Estimated Time: 20-35 minutes.
- Prerequisites: `01-foundations/types-and-io`, `01-foundations/operators-and-expressions`.
- Cross-Language Lens: Compare braces-and-loops in C++, C#, and Go with Python indentation while keeping the underlying branching logic identical.

## Learning Outcomes

- `FND-CFL-01`: Select branches that cover normal and boundary conditions.
- `FND-CFL-02`: Write terminating loops and reason about their invariants.

## Quick Run

Run from the repository root:

~~~bash
python scripts/automation.py run-module --module-path languages/csharp/01-foundations/control-flow
~~~

## Topics Covered

- Conditional branches for FizzBuzz-style rules.
- For loops with clear termination conditions.
- While/for sentinel loops using stop value -1.
- Handling empty input sequences safely.

## Common Pitfalls

- Not handling non-positive upper bounds before entering loops.
- Forgetting to stop on sentinel values in streaming input.
- Dividing by zero when no values were collected.

## Exercise Focus

- exercises/01.cs: run FizzBuzz rules from 1 to N using condition priority.
- exercises/02.cs: read integers until -1 and print average when values exist.

### Exercise Specs

1. exercises/01.cs
- Input: positive integer N.
- Output: sequence with Fizz, Buzz, or FizzBuzz substitutions.
- Edge cases: N <= 0; multiples of both 3 and 5.

2. exercises/02.cs
- Input: integer stream terminated by -1.
- Output: average of entered values or a no-data message.
- Edge cases: first value already -1; negative values other than sentinel.

## Check Your Work

Run from the repository root after implementing a starter:

```bash
python scripts/automation.py check-exercise --language csharp --level 01-foundations --module control-flow --exercise 01
```

Change `--exercise 01` to `--exercise 02` for the second task. Consult `exercises/solutions/` only after making a complete attempt.

## Checkpoint

- [ ] I can explain the core ideas of this module.
- [ ] I can run and modify example/main.cs.
- [ ] I completed exercises/01.cs.
- [ ] I completed exercises/02.cs.
- [ ] I validated at least one edge case for each exercise.
