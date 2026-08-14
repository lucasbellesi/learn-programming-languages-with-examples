# Functions (Go)

This module practices extracting reusable logic and calling helper functions.

## Learning Metadata

- Difficulty: Beginner.
- Estimated Time: 20-35 minutes.
- Prerequisites: `01-foundations/control-flow`, `01-foundations/operators-and-expressions`.
- Cross-Language Lens: Compare helper-function design, argument passing defaults, and overloading support across the six active tracks.

## Learning Outcomes

- `FND-FUN-01`: Decompose a problem into focused functions with explicit contracts.
- `FND-FUN-02`: Use parameters and return values without hidden state changes.

## Quick Run

Run from the repository root:

~~~bash
python scripts/automation.py run-module --module-path languages/go/01-foundations/functions
~~~

## Topics Covered

- Function signatures with typed parameters and return values.
- Separating pure computation from input/output.
- Simple string-processing helpers.
- Testing function behavior with direct inputs.

## Common Pitfalls

- Embedding all logic in main instead of reusable helpers.
- Not validating expected input shape before function calls.
- Ignoring case normalization when counting vowels.

## Cross-Language Notes

- Go keeps functions simple on purpose: no traditional overloading, direct parameter lists, and clear return-value conventions.
- Compared with C++ and C#, the language chooses less syntax in exchange for fewer abstraction tricks.
- The key comparison is simplicity and readability versus richer signature-level expressiveness.

## Exercise Focus

- exercises/01.go: implement maxOfThree and print the maximum of three integers.
- exercises/02.go: implement countVowels and report vowel count for input text.

### Exercise Specs

1. exercises/01.go
- Input: exactly three integer values.
- Output: single maximum value.
- Edge cases: duplicate maxima; all three values equal.

2. exercises/02.go
- Input: one text line.
- Output: number of vowels in the text.
- Edge cases: empty string; uppercase vowels.

## Check Your Work

Run from the repository root after implementing a starter:

```bash
python scripts/automation.py check-exercise --language go --level 01-foundations --module functions --exercise 01
```

Change `--exercise 01` to `--exercise 02` for the second task. Consult `exercises/solutions/` only after making a complete attempt.

## Checkpoint

- [ ] I can explain the core ideas of this module.
- [ ] I can run and modify example/main.go.
- [ ] I completed exercises/01.go.
- [ ] I completed exercises/02.go.
- [ ] I validated at least one edge case for each exercise.
