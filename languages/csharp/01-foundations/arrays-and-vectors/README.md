# Arrays and Vectors (C#)

This module practices storing sequences, iterating them, and computing frequencies.

## Learning Metadata

- Difficulty: Beginner.
- Estimated Time: 20-35 minutes.
- Prerequisites: `01-foundations/control-flow`, `01-foundations/functions`.
- Cross-Language Lens: Compare `vector`, `List<T>`, slices, and Python lists as different tradeoffs for dynamic sequence handling.

## Quick Run

~~~bash
dotnet run --project example/arrays-and-vectors-example.csproj
~~~

## Topics Covered

- Building dynamic collections from user input.
- Forward and reverse iteration patterns.
- Counting occurrences of a target value.
- Handling empty or invalid-size collections.

## Common Pitfalls

- Trusting collection size input when count is zero or negative.
- Off-by-one errors while reading N elements.
- Not handling empty input in frequency tasks.

## Exercise Focus

- exercises/01.cs: read N integers, store them, and print them in reverse order.
- exercises/02.cs: read a collection and count frequency for a target integer.

### Exercise Specs

1. exercises/01.cs
- Input: positive integer count and then count integers.
- Output: values printed in reverse insertion order.
- Edge cases: count <= 0; repeated values in the collection.

2. exercises/02.cs
- Input: integer list plus a target integer.
- Output: frequency count for target value.
- Edge cases: empty list input; target not present.

## Checkpoint

- [ ] I can explain the core ideas of this module.
- [ ] I can run and modify example/main.cs.
- [ ] I completed exercises/01.cs.
- [ ] I completed exercises/02.cs.
- [ ] I validated at least one edge case for each exercise.
