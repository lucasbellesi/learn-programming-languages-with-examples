# Performance and Profiling Basics (Go)

This module introduces simple timing and allocation-aware optimization patterns in Go.

## Quick Run

~~~bash
go run example/main.go
~~~

## Topics Covered

- Measuring elapsed time with `time.Since`.
- Comparing two implementations on the same workload.
- Reducing allocations with `strings.Builder`.
- Pre-sizing slices when the final size is known.

## Common Pitfalls

- Timing workloads that are too small to compare fairly.
- Mixing setup cost into the section you meant to measure.
- Assuming one faster run is enough evidence.
- Optimizing before checking algorithmic complexity first.

## Exercise Focus

- exercises/01.go: compare string concatenation with `strings.Builder`.
- exercises/02.go: compare slice growth with and without reserved capacity.

### Exercise Specs

1. exercises/01.go
- Input: line count.
- Output: elapsed nanoseconds for both string-building approaches.
- Edge cases: zero lines; very small workloads produce noisy timings.

2. exercises/02.go
- Input: element count.
- Output: elapsed nanoseconds for slice fill with and without reserved capacity.
- Edge cases: zero count; small sizes with little visible difference.

## Checkpoint

- [ ] I can measure code sections with `time.Since`.
- [ ] I can compare two implementations on the same input.
- [ ] I can explain why builders or slice capacity can reduce allocations.
- [ ] I completed exercises/01.go.
- [ ] I completed exercises/02.go.
