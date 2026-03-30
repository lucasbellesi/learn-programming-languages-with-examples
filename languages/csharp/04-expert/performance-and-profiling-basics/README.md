# Performance and Profiling Basics (C#)

This module introduces simple measurement and optimization patterns in C#.

## Quick Run

~~~bash
dotnet run --project example/performance-and-profiling-basics-example.csproj
~~~

## Topics Covered

- Measuring elapsed time with `Stopwatch`.
- Comparing two implementations on the same workload.
- Reducing allocations with `StringBuilder` or pre-sized collections.
- Avoiding conclusions from noisy one-off timings.

## Common Pitfalls

- Timing workloads that are too small to compare meaningfully.
- Mixing data generation time with the code under test.
- Treating a single faster run as a final truth.
- Optimizing without understanding algorithmic cost first.

## Exercise Focus

- exercises/01.cs: compare string concatenation with `StringBuilder`.
- exercises/02.cs: compare `List<T>` growth with and without initial capacity.

### Exercise Specs

1. exercises/01.cs
- Input: line count.
- Output: elapsed ticks for both string-building approaches.
- Edge cases: zero lines; very small workloads produce noisy timings.

2. exercises/02.cs
- Input: element count.
- Output: elapsed ticks for list fill with and without preset capacity.
- Edge cases: zero count; small sizes with little visible difference.

## Checkpoint

- [ ] I can measure work with `Stopwatch`.
- [ ] I can compare two implementations on the same input fairly.
- [ ] I can explain why pre-sizing or reducing allocations can help.
- [ ] I completed exercises/01.cs.
- [ ] I completed exercises/02.cs.
