# Input Validation (Go)

This module teaches defensive input handling for interactive programs.

## Learning Metadata

- Difficulty: Intermediate.
- Estimated Time: 30-45 minutes.
- Prerequisites: `01-foundations/control-flow`, `01-foundations/types-and-io`.
- Cross-Language Lens: Compare loop-driven validation in all four languages and notice where parsing APIs are strict versus forgiving.

## Quick Run

~~~bash
go run example/main.go
~~~

## Topics Covered

- Parsing and validating integers and floating-point numbers from user input.
- Enforcing numeric ranges with reusable helper functions.
- Recovering from invalid input without terminating the program.
- Keeping interactive flow stable with retry loops.

## Common Pitfalls

- Assuming `Atoi` and `ParseFloat` always succeed.
- Accepting values outside allowed ranges after type conversion.
- Repeating validation code instead of centralizing it in helpers.

## Exercise Focus

- exercises/01.go: read an integer in range 1 to 100 and print its square.
- exercises/02.go: read a valid score count and valid scores, then print average.

### Exercise Specs

1. exercises/01.go
- Input: repeated attempts until a valid integer in range 1..100 is entered.
- Output: square of the accepted value.
- Edge cases: non-numeric text; values below 1 or above 100.

2. exercises/02.go
- Input: score count in range 1..50, followed by scores in range 0..100.
- Output: average score.
- Edge cases: invalid score entered mid-sequence; boundary values 0 and 100.

## Checkpoint

- [ ] I can validate parsed values before using them.
- [ ] I can enforce both type and range constraints in one loop.
- [ ] I can reuse helper functions for multiple prompts.
- [ ] I completed exercises/01.go.
- [ ] I completed exercises/02.go.
