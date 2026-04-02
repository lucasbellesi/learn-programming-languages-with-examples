# Types and Input/Output (Go)

This module practices typed input, safe parsing, and basic numeric summaries.

## Learning Metadata

- Difficulty: Beginner.
- Estimated Time: 20-35 minutes.
- Prerequisites: None; this is the entry module for the track.
- Cross-Language Lens: Compare strongly typed console input in C++ and C# with explicit parsing in Go and Python's more dynamic input model.

## Quick Run

~~~bash
go run example/main.go
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

- Go makes input and conversion explicit, usually with scanned strings plus parse helpers and returned errors.
- Compared with C# and Python, there is less hidden convenience and more emphasis on simple control flow after parsing.
- The useful comparison is direct error-return handling versus exceptions or looser dynamic conversion.

## Exercise Focus

- exercises/01.go: read N numeric values and print sum, average, minimum, and maximum.
- exercises/02.go: parse product price quantity and print the computed total price.

### Exercise Specs

1. exercises/01.go
- Input: integer N followed by N numeric values.
- Output: summary lines for sum, average, minimum, and maximum.
- Edge cases: N <= 0; repeated values where minimum equals maximum.

2. exercises/02.go
- Input: single-line record: product price quantity.
- Output: parsed product name and computed total price.
- Edge cases: wrong token count; quantity = 0.

## Checkpoint

- [ ] I can explain the core ideas of this module.
- [ ] I can run and modify example/main.go.
- [ ] I completed exercises/01.go.
- [ ] I completed exercises/02.go.
- [ ] I validated at least one edge case for each exercise.
