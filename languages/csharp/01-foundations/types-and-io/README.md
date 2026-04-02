# Types and Input/Output (C#)

This module practices typed input, safe parsing, and basic numeric summaries.

## Learning Metadata

- Difficulty: Beginner.
- Estimated Time: 20-35 minutes.
- Prerequisites: None; this is the entry module for the track.
- Cross-Language Lens: Compare strongly typed console input in C++ and C# with explicit parsing in Go and Python's more dynamic input model.

## Quick Run

~~~bash
dotnet run --project example/types-and-io-example.csproj
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

- C# keeps the same string-first console model as Python and TypeScript, but parsing still lands in a statically typed program.
- Compared with C++, stream handling feels higher-level, but failed conversions still need explicit decisions.
- The key comparison is how much safety comes from the runtime library versus the language itself.

## Exercise Focus

- exercises/01.cs: read N numeric values and print sum, average, minimum, and maximum.
- exercises/02.cs: parse product price quantity and print the computed total price.

### Exercise Specs

1. exercises/01.cs
- Input: integer N followed by N numeric values.
- Output: summary lines for sum, average, minimum, and maximum.
- Edge cases: N <= 0; repeated values where minimum equals maximum.

2. exercises/02.cs
- Input: single-line record: product price quantity.
- Output: parsed product name and computed total price.
- Edge cases: wrong token count; quantity = 0.

## Checkpoint

- [ ] I can explain the core ideas of this module.
- [ ] I can run and modify example/main.cs.
- [ ] I completed exercises/01.cs.
- [ ] I completed exercises/02.cs.
- [ ] I validated at least one edge case for each exercise.
