# Input Validation (C#)

This module teaches defensive input handling for interactive programs.

## Quick Run

~~~bash
dotnet run --project example/input-validation-example.csproj
~~~

## Topics Covered

- Validating integers and decimals using `TryParse`.
- Enforcing value ranges before consuming input.
- Reusing helper methods for consistent validation logic.
- Keeping console applications stable when users provide invalid data.

## Common Pitfalls

- Using `int.Parse` or `double.Parse` directly for user-entered text.
- Accepting out-of-range values after successful parsing.
- Duplicating similar validation loops instead of extracting helpers.

## Exercise Focus

- exercises/01.cs: read an integer in range 1 to 100 and print its square.
- exercises/02.cs: read a valid score count and valid scores, then print average.

### Exercise Specs

1. exercises/01.cs
- Input: repeated attempts until a valid integer in range 1..100 is entered.
- Output: square of the accepted value.
- Edge cases: non-numeric text; values below 1 or above 100.

2. exercises/02.cs
- Input: score count in range 1..50, followed by scores in range 0..100.
- Output: average score.
- Edge cases: invalid score entered mid-sequence; boundary values 0 and 100.

## Checkpoint

- [ ] I can validate input with `TryParse` and range checks.
- [ ] I can recover from invalid entries without terminating the program.
- [ ] I can structure reusable input helper methods.
- [ ] I completed exercises/01.cs.
- [ ] I completed exercises/02.cs.
