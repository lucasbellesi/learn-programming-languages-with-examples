# Types and Input/Output (Python)

This module practices typed input, safe parsing, and basic numeric summaries.

## Learning Metadata

- Difficulty: Beginner.
- Estimated Time: 20-35 minutes.
- Prerequisites: None; this is the entry module for the track.
- Cross-Language Lens: Compare strongly typed console input in C++ and C# with explicit parsing in Go and Python's more dynamic input model.

## Learning Outcomes

- `FND-TIO-01`: Choose suitable primitive values and variables for a small problem.
- `FND-TIO-02`: Read, validate, transform, and present console data.

## Quick Run

~~~bash
python example/main.py
~~~

## Topics Covered

- Reading typed values from standard input.
- Computing sum, average, minimum, and maximum.
- Parsing structured one-line input into typed fields.
- Printing results with clear labels and numeric formatting.

## Common Pitfalls

- Assuming input parsing always succeeds without validation.
- Accepting non-positive counts when statistics require at least one value.
- Mixing integer and floating-point arithmetic incorrectly.

## Cross-Language Notes

- Python starts with strings too, but dynamic values make early experiments feel lighter than in the statically typed tracks.
- Compared with C++ or Go, most mistakes show up at runtime rather than during compilation.
- The key comparison is fast experimentation versus the stronger guardrails of explicit typed input pipelines.

## Exercise Focus

- exercises/01.py: read N numeric values and print sum, average, minimum, and maximum.
- exercises/02.py: parse product price quantity and print the computed total price.

### Exercise Specs

1. exercises/01.py
- Input: integer N followed by N numeric values.
- Output: summary lines for sum, average, minimum, and maximum.
- Edge cases: N <= 0; repeated values where minimum equals maximum.

2. exercises/02.py
- Input: single-line record: product price quantity.
- Output: parsed product name and computed total price.
- Edge cases: wrong token count; quantity = 0.

## Practice Workflow

1. Edit the starter in `exercises/01.py` or `exercises/02.py`.
2. Check your work from the repository root:

~~~bash
python scripts/automation.py check-exercise --language python --level 01-foundations --module types-and-io --exercise 01
~~~

3. Change `--exercise` to `02` for the second task. Reference implementations are under `exercises/solutions/`; use `--solution` only after attempting the exercise.

## Check Your Work

Run from the repository root after implementing a starter:

```bash
python scripts/automation.py check-exercise --language python --level 01-foundations --module types-and-io --exercise 01
```

Change `--exercise 01` to `--exercise 02` for the second task. Consult `exercises/solutions/` only after making a complete attempt.

## Checkpoint

- [ ] I can explain the core ideas of this module.
- [ ] I can run and modify example/main.py.
- [ ] I completed exercises/01.py.
- [ ] I completed exercises/02.py.
- [ ] I validated at least one edge case for each exercise.
