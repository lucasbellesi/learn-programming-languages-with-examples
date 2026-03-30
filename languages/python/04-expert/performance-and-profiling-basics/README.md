# Performance and Profiling Basics (Python)

This module introduces simple timing and allocation-aware optimization patterns in Python.

## Quick Run

~~~bash
python example/main.py
~~~

## Topics Covered

- Measuring elapsed time with `time.perf_counter`.
- Comparing two implementations on the same workload.
- Reducing temporary allocations with `str.join`.
- Pre-sizing mutable containers when the final size is known.

## Common Pitfalls

- Timing workloads that are too small to compare fairly.
- Measuring setup work along with the code you meant to test.
- Drawing conclusions from one noisy run.
- Optimizing before understanding the dominant cost.

## Exercise Focus

- exercises/01.py: compare string concatenation with `str.join`.
- exercises/02.py: compare list growth with and without pre-sized storage.

### Exercise Specs

1. exercises/01.py
- Input: line count.
- Output: elapsed seconds for both string-building approaches.
- Edge cases: zero lines; very small workloads produce noisy timings.

2. exercises/02.py
- Input: element count.
- Output: elapsed seconds for list fill with and without pre-sized storage.
- Edge cases: zero count; small sizes with little visible difference.

## Checkpoint

- [ ] I can measure code with `time.perf_counter`.
- [ ] I can compare two implementations on the same input.
- [ ] I can explain why fewer allocations can help.
- [ ] I completed exercises/01.py.
- [ ] I completed exercises/02.py.
