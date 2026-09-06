# Types and Input/Output (Go)

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

Run from the repository root:

~~~bash
python scripts/automation.py run-module --module-path languages/go/01-foundations/types-and-io
~~~

### Observe, Predict, Modify

Enter `Ada`, `20`, and `3.5`, pressing Enter after each value. Use a single word for the name because `Scanln` separates fields at whitespace.

Look for these result lines (interactive prompts and the summary heading are omitted):

~~~text
Name: Ada
Age: 20
GPA: 3.50
Adult: true
~~~

Change the age to `17` and predict the boolean. This introductory example assumes valid numeric input and does not handle the errors returned by `Scanln`; error checking comes in input-validation.

Restore the original values before moving on to the exercises.

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

## Check Your Work

Run from the repository root after implementing a starter:

```bash
python scripts/automation.py check-exercise --language go --level 01-foundations --module types-and-io --exercise 01
```

Change `--exercise 01` to `--exercise 02` for the second task. Consult `exercises/solutions/` only after making a complete attempt.

### Visible Practice Cases

These cases come from the exercise checker. Implement the general behavior; do not
hardcode these answers. Each input line below is a separate line of standard input.
The unmodified starters are incomplete, so a failed check before implementation is expected.

**Exercise 01**

Normal input:

~~~text
3
10
20
30
~~~

Expected result labels and values (prompts omitted; decimal formatting may add zeros):

~~~text
Sum: 60
Average: 20
Minimum: 10
Maximum: 30
~~~

Also check these boundary cases. The checker compares their full output, including
prompts and spaces. In this table, `\n` means a newline; input typed by the user is
not part of the program output.

| Case | Input lines (`\n` separates lines) | Exact program output |
| --- | --- | --- |
| edge: N <= 0 | `0\n10\n20\n30` | `How many numbers? Please enter a positive count.\n` |
| edge: repeated values where minimum equals maximum | `3\n5\n5\n5` | `How many numbers? Value 1: Value 2: Value 3: Sum: 15.0000\nAverage: 5.0000\nMinimum: 5.0000\nMaximum: 5.0000\n` |

**Exercise 02**

Normal input:

~~~text
notebook 2.50 4
~~~

Expected result labels and values (prompts omitted; decimal formatting may add zeros):

~~~text
Product: notebook
Total price: 10
~~~

Also check these boundary cases. The checker compares their full output, including
prompts and spaces. In this table, `\n` means a newline; input typed by the user is
not part of the program output.

| Case | Input lines (`\n` separates lines) | Exact program output |
| --- | --- | --- |
| edge: wrong token count | `notebook 2.50` | `Enter product price quantity: Invalid format. Use: product price quantity\n` |
| edge: quantity = 0 | `notebook 2.50 0` | `Enter product price quantity: Product: notebook\nTotal price: 0.00\n` |
| edge: extra product field | `notebook 2.50 4 extra` | `Enter product price quantity: Invalid format. Use: product price quantity\n` |

## Checkpoint

- [ ] I can explain the core ideas of this module.
- [ ] I can run and modify example/main.go.
- [ ] I completed exercises/01.go.
- [ ] I completed exercises/02.go.
- [ ] I validated at least one edge case for each exercise.
