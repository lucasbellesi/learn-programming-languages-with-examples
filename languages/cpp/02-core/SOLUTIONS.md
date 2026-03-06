# Core Solutions Guide

This file gives solution direction without full code.
Use it to unblock yourself, then finish the full implementation.

## How To Use

1. Read the exercise spec in the module README.
2. Implement your own version first.
3. Use this guide to debug logic or edge cases.

## Global Verification Checklist

- [ ] Code compiles with `-std=c++17 -Wall -Wextra -pedantic`.
- [ ] Input validation is explicit and user-friendly.
- [ ] File operations check open/read/write failures.
- [ ] Edge cases from each module README are covered.

## input-validation

### `exercises/01.cpp`
- Strategy: wrap input reads in a retry loop; clear error flags and flush invalid input on failure.
- Common mistakes: infinite loops when stream fail state is not cleared.
- Self-check: test letters where numbers are expected.

### `exercises/02.cpp`
- Strategy: validate each field as soon as it is read; reject invalid entries early.
- Common mistakes: accepting partially valid records.
- Self-check: test empty input and mixed valid/invalid lines.

## algorithms-basics

### `exercises/01.cpp`
- Strategy: break task into small helper logic (read, process, print).
- Common mistakes: combining too many responsibilities inside one loop.
- Self-check: run with tiny, medium, and edge-size input sets.

### `exercises/02.cpp`
- Strategy: define algorithm steps on paper first, then translate directly into loops/conditions.
- Common mistakes: off-by-one loop boundaries.
- Self-check: test first element, last element, and not-found cases.

## file-io-basics

### `exercises/01.cpp` (copy with line numbers)
- Strategy: open input and output files, then stream line-by-line with incrementing counter.
- Common mistakes: not checking file open success before reading/writing.
- Self-check: test empty file and multi-line file.

### `exercises/02.cpp` (name-score average)
- Strategy: parse `name score` rows safely, accumulate totals, and compute average at end.
- Common mistakes: trusting malformed lines without validation.
- Self-check: test malformed rows and file with one valid row.

## sorting-and-searching

### `exercises/01.cpp` (selection sort)
- Strategy: for each index, find minimum in remaining range and swap once.
- Common mistakes: swapping inside inner loop instead of after minimum is found.
- Self-check: test already sorted, reverse sorted, and duplicated values.

### `exercises/02.cpp` (binary search)
- Strategy: keep `left` and `right`, compute middle safely, shrink range based on comparison.
- Common mistakes: wrong loop condition causing missed final candidate.
- Self-check: test found at first/middle/last and not-found.

## maps-and-frequency-counting

### `exercises/01.cpp` (digit frequency)
- Strategy: iterate values, extract digits, increment counts in a map/array.
- Common mistakes: not handling `0` correctly as a digit.
- Self-check: test repeated digits and numbers containing zero.

### `exercises/02.cpp` (first non-repeating char)
- Strategy: first pass to count, second pass to find first char with count `1`.
- Common mistakes: trying to solve in one pass with unstable order.
- Self-check: test all-repeating string and single-character string.

## error-handling-and-defensive-programming

### `exercises/01.cpp` (CSV-like validation)
- Strategy: split or parse fields, validate field count/type/range before processing.
- Common mistakes: accepting rows with missing fields.
- Self-check: test malformed separators and extra delimiters.

### `exercises/02.cpp` (safe division utility)
- Strategy: validate numeric input and guard division by zero before computing result.
- Common mistakes: performing division before checks.
- Self-check: test zero divisor, non-numeric input, and valid decimals.
