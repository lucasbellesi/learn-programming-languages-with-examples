# Control Flow (Python)

This module practices branching, looping, and sentinel-driven iteration.

## Quick Run

~~~bash
python example/main.py
~~~

## Topics Covered

- Conditional branches for FizzBuzz-style rules.
- For loops with clear termination conditions.
- While/for sentinel loops using stop value -1.
- Handling empty input sequences safely.

## Common Pitfalls

- Not handling non-positive upper bounds before entering loops.
- Forgetting to stop on sentinel values in streaming input.
- Dividing by zero when no values were collected.

## Exercise Focus

- exercises/01.py: run FizzBuzz rules from 1 to N using condition priority.
- exercises/02.py: read integers until -1 and print average when values exist.

### Exercise Specs

1. exercises/01.py
- Input: positive integer N.
- Output: sequence with Fizz, Buzz, or FizzBuzz substitutions.
- Edge cases: N <= 0; multiples of both 3 and 5.

2. exercises/02.py
- Input: integer stream terminated by -1.
- Output: average of entered values or a no-data message.
- Edge cases: first value already -1; negative values other than sentinel.

## Checkpoint

- [ ] I can explain the core ideas of this module.
- [ ] I can run and modify example/main.py.
- [ ] I completed exercises/01.py.
- [ ] I completed exercises/02.py.
- [ ] I validated at least one edge case for each exercise.