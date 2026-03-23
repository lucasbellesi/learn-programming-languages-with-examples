# Assessment 02: Core

## Goal

Practice validation, counting, file output, and defensive logic.

## Task

Write a program that reads integer values until `-1`, then:

1. Ignores any value outside range `0..100`.
2. Prints count of valid values.
3. Prints min, max, and average for valid values.
4. Prints a frequency table by tens:
- `0-9`, `10-19`, ..., `90-100`
5. Saves the same report to `core_assessment_report.txt`.

## Quick Run

```bash
dotnet run --project assessment-02-core.csproj
```

## Sample Input

```text
12 17 31 77 91 105 64 -3 88 -1
```

## Expected Behavior

- `105` and `-3` are ignored.
- Only values in `0..100` are used for statistics and frequency table.
- If no valid values are entered, print a friendly message and still create the report file.
