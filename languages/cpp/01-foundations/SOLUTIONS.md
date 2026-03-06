# Foundations Solutions Guide

This file provides solution strategy, common mistakes, and self-check points.
It is intentionally not a full answer dump.

## How To Use

1. Try each exercise first without this guide.
2. Use the strategy bullets only if you are blocked.
3. After finishing, compare your output with the module `Exercise Specs`.

## Global Verification Checklist

- [ ] Program compiles with `-std=c++17 -Wall -Wextra -pedantic`.
- [ ] Output format matches the spec exactly.
- [ ] Edge cases from the module README are handled.
- [ ] Variables and control flow are easy to read.

## types-and-io

### `exercises/01.cpp` (sum, average, min, max)
- Strategy: read `n`, validate `n > 0`, loop `n` times, keep running sum, and update min/max in the same loop.
- Common mistakes: dividing by zero when `n <= 0`; not initializing min/max from first value.
- Self-check: test with positive, negative, and decimal values.

### `exercises/02.cpp` (product price quantity)
- Strategy: read product name and numeric values; compute `price * quantity`; print total clearly.
- Common mistakes: mixing `getline` and `cin` without clearing input; truncating decimal values.
- Self-check: verify total with decimal price and integer quantity.

## control-flow

### `exercises/01.cpp` (FizzBuzz)
- Strategy: loop from `1` to `n`; check `i % 15` first, then `i % 3`, then `i % 5`.
- Common mistakes: wrong condition order (`%3` before `%15`).
- Self-check: verify `15`, `30`, and non-multiples.

### `exercises/02.cpp` (sentinel average)
- Strategy: keep reading values until `-1`; track sum and count for non-sentinel numbers.
- Common mistakes: counting `-1` in the average; not handling "no valid values".
- Self-check: test immediate `-1` and mixed positive/negative inputs.

## functions

### `exercises/01.cpp` (max of three)
- Strategy: create function returning max among three integers with simple comparisons.
- Common mistakes: comparing only two values or forgetting equal-value cases.
- Self-check: test all permutations of largest value and ties.

### `exercises/02.cpp` (count vowels)
- Strategy: create function taking `const string&`; iterate chars and count vowels case-insensitively.
- Common mistakes: only counting lowercase vowels.
- Self-check: test empty string, uppercase input, and mixed text.

## arrays-and-vectors

### `exercises/01.cpp` (reverse output)
- Strategy: read vector of `n` values; print from `n - 1` to `0`.
- Common mistakes: out-of-range indexing when `n == 0`.
- Self-check: test with `n = 1`, repeated values, and `n <= 0`.

### `exercises/02.cpp` (frequency count)
- Strategy: read values into vector, read target, loop once and increment counter when matched.
- Common mistakes: forgetting to initialize counter to `0`.
- Self-check: test target absent and target present in every element.

## strings

### `exercises/01.cpp` (palindrome check)
- Strategy: normalize input (ignore case/spaces if exercise requires), compare mirrored positions.
- Common mistakes: mismatched index bounds when checking from both ends.
- Self-check: test odd/even length strings and punctuation handling expectations.

### `exercises/02.cpp` (word counting or string parsing task)
- Strategy: define exact parsing rule first, then loop through characters/tokens accordingly.
- Common mistakes: not handling leading/trailing spaces.
- Self-check: test empty input and multiple spaces between words.

## operators-and-expressions

### `exercises/01.cpp` (seconds to h:m:s)
- Strategy: use integer division and modulo to extract hours, minutes, seconds.
- Common mistakes: wrong modulo order causing invalid minutes/seconds.
- Self-check: test `0`, `59`, `60`, `3600`, and larger values.

### `exercises/02.cpp` (discount and tax)
- Strategy: calculate discount first (if eligible), then tax according to spec order.
- Common mistakes: applying tax before discount when spec expects the opposite.
- Self-check: compare eligible vs non-eligible scenarios.

## scope-and-lifetime-basics

### `exercises/01.cpp` (shadowing fix)
- Strategy: identify duplicated variable names in nested scopes and remove accidental shadowing.
- Common mistakes: updating one variable while printing another with same name.
- Self-check: add prints before/after scope blocks to verify expected value.

### `exercises/02.cpp` (reduce variable lifetime)
- Strategy: declare variables as close as possible to first use inside the smallest valid block.
- Common mistakes: keeping mutable state alive across unrelated logic.
- Self-check: ensure behavior unchanged and code easier to reason about.

## formatted-output-and-iomanip

### `exercises/01.cpp` (invoice table)
- Strategy: use `setw`, `left`/`right`, and `fixed << setprecision(...)` for aligned columns.
- Common mistakes: alignment resets not applied consistently between columns.
- Self-check: test with short and long product names.

### `exercises/02.cpp` (statistics report precision)
- Strategy: read precision setting, apply with `setprecision`, print all metrics using same format.
- Common mistakes: mixing default formatting with fixed formatting.
- Self-check: compare outputs for precision `0`, `2`, and `4`.
