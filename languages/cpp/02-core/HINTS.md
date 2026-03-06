# 02 Core Hints

Use these hints to debug your approach before reading or writing full solutions.

## input-validation

### Exercise 01 hints

- Use a `while (true)` loop.
- On extraction failure: `cin.clear()` + `cin.ignore(...)`.
- Validate range `[1, 100]` after successful extraction.

### Exercise 02 hints

- Validate count first, then each score.
- Keep score range checks in the inner loop.

## algorithms-basics

### Exercise 01 hints

- Initialize `index = -1`.
- Break loop when first match is found.

### Exercise 02 hints

- Initialize `min`/`max` from first element.
- Update `evenCount` with `value % 2 == 0`.

## file-io-basics

### Exercise 01 hints

- Read full lines with `std::getline`.
- Prefix each line with incremental number.

### Exercise 02 hints

- Loop until EOF.
- Handle malformed rows by clearing stream and discarding bad line.

## sorting-and-searching

### Exercise 01 hints

- Selection sort: find smallest element in unsorted tail and swap.

### Exercise 02 hints

- Binary search condition: `left <= right`.
- Adjust bounds based on `midValue < target`.

## maps-and-frequency-counting

### Exercise 01 hints

- Initialize counts for digits `0..9`.
- Increment only if value is in valid range.

### Exercise 02 hints

- First pass: count each char.
- Second pass: find first char with count `1`.

## error-handling-and-defensive-programming

### Exercise 01 hints

- Find first and second comma positions.
- Validate that no field is empty.

### Exercise 02 hints

- Retry on invalid type and zero divisor.
- Continue loop until one valid division is completed.
