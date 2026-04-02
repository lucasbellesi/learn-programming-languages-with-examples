# Functions (Python)

This module practices extracting reusable logic and calling helper functions.

## Learning Metadata

- Difficulty: Beginner.
- Estimated Time: 20-35 minutes.
- Prerequisites: `01-foundations/control-flow`, `01-foundations/operators-and-expressions`.
- Cross-Language Lens: Compare helper-function design, argument passing defaults, and overloading support across the four tracks.

## Quick Run

~~~bash
python example/main.py
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

- Python functions are flexible and lightweight, but they rely less on compile-time structure than the statically typed tracks.
- Compared with C++ or C#, overloads are usually expressed by convention or branching instead of distinct signatures.
- The important comparison is readability through convention versus readability through type structure.

## Exercise Focus

- exercises/01.py: implement maxOfThree and print the maximum of three integers.
- exercises/02.py: implement countVowels and report vowel count for input text.

### Exercise Specs

1. exercises/01.py
- Input: exactly three integer values.
- Output: single maximum value.
- Edge cases: duplicate maxima; all three values equal.

2. exercises/02.py
- Input: one text line.
- Output: number of vowels in the text.
- Edge cases: empty string; uppercase vowels.

## Checkpoint

- [ ] I can explain the core ideas of this module.
- [ ] I can run and modify example/main.py.
- [ ] I completed exercises/01.py.
- [ ] I completed exercises/02.py.
- [ ] I validated at least one edge case for each exercise.
