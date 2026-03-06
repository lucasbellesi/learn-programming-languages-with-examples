# 01 Foundations Hints

Use these hints only after attempting each exercise.

## types-and-io

### Exercise 01 hints

- Track `sum` while reading values.
- Initialize `min` and `max` from the first input value, not from `0`.
- Compute `average` as `sum / n` after the loop.

### Exercise 02 hints

- Read three tokens: `product`, `price`, `quantity`.
- Multiply `price * quantity` for total.

## operators-and-expressions

### Exercise 01 hints

- `hours = totalSeconds / 3600`
- `minutes = (totalSeconds % 3600) / 60`
- `seconds = totalSeconds % 60`

### Exercise 02 hints

- Apply discount before tax.
- Tax percentage `x` is `x / 100.0`.

## control-flow

### Exercise 01 hints

- Check multiples of 15 before checking 3 or 5.

### Exercise 02 hints

- Stop when you read `-1`.
- Only divide by `count` if `count > 0`.

## functions

### Exercise 01 hints

- Compare values step by step and keep a `currentMax`.

### Exercise 02 hints

- Convert characters with `std::tolower`.
- Count `a, e, i, o, u`.

## arrays-and-vectors

### Exercise 01 hints

- Store values in `std::vector<int>`.
- Print from index `n - 1` down to `0`.

### Exercise 02 hints

- Loop through vector and increment `frequency` on match.

## strings

### Exercise 01 hints

- Count transitions from whitespace to non-whitespace as new words.

### Exercise 02 hints

- Use two indexes (`left`/`right`) and skip non-letter characters.
- Compare lowercase versions of letters.

## scope-and-lifetime-basics

### Exercise 01 hints

- Use a single `grade` variable and assign it in one branch chain.

### Exercise 02 hints

- Keep loop variable scoped inside `for`.
- Keep `sum` outside loop.

## formatted-output-and-iomanip

### Exercise 01 hints

- Use `std::setw` for each column.
- Keep `std::fixed << std::setprecision(2)` for money.

### Exercise 02 hints

- Set precision once before printing final results.
- Reuse min/max pattern from foundations statistics exercises.
