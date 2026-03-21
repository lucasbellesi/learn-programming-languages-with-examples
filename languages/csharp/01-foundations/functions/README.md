# Functions (C#)

This module practices extracting reusable logic and calling helper functions.

## Quick Run

~~~bash
dotnet run --project example/functions-example.csproj
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

## Exercise Focus

- exercises/01.cs: implement maxOfThree and print the maximum of three integers.
- exercises/02.cs: implement countVowels and report vowel count for input text.

### Exercise Specs

1. exercises/01.cs
- Input: exactly three integer values.
- Output: single maximum value.
- Edge cases: duplicate maxima; all three values equal.

2. exercises/02.cs
- Input: one text line.
- Output: number of vowels in the text.
- Edge cases: empty string; uppercase vowels.

## Checkpoint

- [ ] I can explain the core ideas of this module.
- [ ] I can run and modify example/main.cs.
- [ ] I completed exercises/01.cs.
- [ ] I completed exercises/02.cs.
- [ ] I validated at least one edge case for each exercise.