# Performance and Profiling Basics (Java)

This module introduces measurement discipline and allocation-aware comparisons on the JVM.

## Learning Metadata

- Difficulty: Advanced.
- Estimated Time: 45-60 minutes.
- Prerequisites: `02-core/algorithms-basics`, `02-core/maps-and-frequency-counting`, `03-advanced/structs-and-classes`.
- Cross-Language Lens: Compare JVM warm-up and allocation costs with native timing, managed runtimes, interpreters, and JavaScript engines.

## Learning Outcomes

- `EXP-PER-01`: Measure before optimizing and interpret timing data cautiously.
- `EXP-PER-02`: Relate algorithmic and allocation choices to observed cost.

## Quick Run

~~~bash
javac -d build/java languages/java/04-expert/performance-and-profiling-basics/example/Main.java
java -cp build/java Main
~~~

## Topics Covered

- Measuring elapsed work with `System.nanoTime`.
- Warming up code before comparing JVM execution.
- Averaging repeated runs instead of trusting one sample.
- Comparing algorithm and data-structure choices on the same workload.
- Keeping observable results so measured work is not discarded conceptually.

## Common Pitfalls

- Treating a microbenchmark as production profiling evidence.
- Timing setup work together with the operation under comparison.
- Declaring a winner from one noisy run.
- Ignoring JIT compilation, garbage collection, and allocation effects.
- Optimizing before checking algorithmic complexity.

## Cross-Language Notes

- Java timings include JVM warm-up and JIT effects that do not map directly to ahead-of-time compiled C++.
- Compared with Python or TypeScript, JVM code may change performance characteristics as hot methods are compiled.
- `System.nanoTime` is suitable for elapsed-time comparisons, while Java Flight Recorder and profilers are better for real diagnosis.
- The learner goal is to form a hypothesis, measure fairly, and avoid promising that one run proves an optimization.

## Exercise Focus

- exercises/Exercise01.java: compare repeated string concatenation with `StringBuilder`.
- exercises/Exercise02.java: compare `ArrayList` growth with and without initial capacity.

### Exercise Specs

1. exercises/Exercise01.java
- Input: number of text fragments.
- Output: average nanoseconds and equal-output confirmation.
- Edge cases: zero fragments; small workloads with noisy timings.

2. exercises/Exercise02.java
- Input: number of integer elements.
- Output: average nanoseconds and equal-checksum confirmation.
- Edge cases: zero elements; small workloads with little visible difference.

## Check Your Work

Run from the repository root after implementing a starter:

```bash
python scripts/automation.py check-exercise --language java --level 04-expert --module performance-and-profiling-basics --exercise 01
```

Change `--exercise 01` to `--exercise 02` for the second task. Consult `exercises/solutions/` only after making a complete attempt.

## Checkpoint

- [ ] I can measure elapsed work with `System.nanoTime`.
- [ ] I can warm up and repeat a comparison.
- [ ] I can separate setup from the operation under test.
- [ ] I can explain why microbenchmarks are not full profilers.
- [ ] I completed exercises/Exercise01.java.
- [ ] I completed exercises/Exercise02.java.
