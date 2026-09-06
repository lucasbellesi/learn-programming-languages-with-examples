# Types and Input/Output

This module covers basic data types and console input/output in C++.

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
python scripts/automation.py run-module --module-path languages/cpp/01-foundations/types-and-io
~~~

## More Examples

- `example/input-validation-loop.cpp`:

```bash
g++ -std=c++17 -Wall -Wextra -pedantic example/input-validation-loop.cpp -o types_and_io_validation_loop
./types_and_io_validation_loop
```

### Observe, Predict, Modify

Enter `Ada Lovelace`, `20`, `3.5`, and `y`, pressing Enter after each value.

Look for these result lines (interactive prompts and the summary heading are omitted):

~~~text
Name: Ada Lovelace
Age: 20
GPA: 3.5
Enrolled: true
~~~

Change `y` to `n` and predict the enrollment label. `getline` preserves spaces in the name; `cin >>` extracts numeric values. This introductory example assumes valid input; stream failure handling comes in input-validation.

Restore the original values before moving on to the exercises.

## Topics Covered

- `int`, `double`, `char`, `bool`, `std::string`.
- Formatted extraction with `std::cin`.
- Output formatting with `std::cout`.
- Full-line input using `std::getline`.

## Common Pitfalls

- Mixing `cin >>` and `getline` without clearing newline.
- Assuming numeric input always succeeds.
- Forgetting to check ranges for user input.

## Cross-Language Notes

- C++ is the canonical baseline here: types are explicit and stream state matters immediately when input goes wrong.
- Compared with Python and TypeScript, this track forces you to think earlier about conversion failures and mixed text and numeric reads.
- The recurring comparison is compile-time type safety versus runtime parsing flexibility.

## Exercise Focus

- `exercises/01.cpp`: read `N` numbers and compute sum, average, min, max.
- `exercises/02.cpp`: parse `product price quantity` and compute total price.

### Exercise Specs

1. `exercises/01.cpp`
- Input: integer `N` followed by `N` numeric values.
- Output: sum, average, minimum, maximum.
- Edge cases: `N <= 0` should exit with message; all equal values should produce equal min/max.

2. `exercises/02.cpp`
- Input: single line: `product price quantity`.
- Output: parsed fields and total price.
- Edge cases: quantity `0` should give total `0`; decimal price should keep precision.

## Check Your Work

Run from the repository root after implementing a starter:

```bash
python scripts/automation.py check-exercise --language cpp --level 01-foundations --module types-and-io --exercise 01
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
| edge: N <= 0 should exit with message | `0\n10\n20\n30` | `How many numbers will you enter? Please enter a positive count.\n` |
| edge: all equal values should produce equal min/max | `3\n5\n5\n5` | `How many numbers will you enter? Number 1: Number 2: Number 3: \nResults:\nSum: 15\nAverage: 5\nMinimum: 5\nMaximum: 5\n` |

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
| edge: quantity 0 should give total 0 | `notebook 2.50 0` | `Enter product price quantity (example: notebook 2.50 4): Product: notebook\nUnit price: 2.5\nQuantity: 0\nTotal price: 0\n` |
| edge: decimal price should keep precision | `notebook 2.345 4` | `Enter product price quantity (example: notebook 2.50 4): Product: notebook\nUnit price: 2.345\nQuantity: 4\nTotal price: 9.38\n` |

## Checkpoint

- [ ] I can read and print typed values.
- [ ] I can safely use `getline` after formatted extraction.
- [ ] I can compute simple statistics from input.
- [ ] I completed both exercises.
