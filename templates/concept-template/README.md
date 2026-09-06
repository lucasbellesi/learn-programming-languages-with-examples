# Concept Template (Language-Agnostic)

Use this template when creating a new concept module in any track.
The core section headings follow the repository validation contract. The
walkthrough and visible practice subsections provide additional learner guidance.

Register both exercises in `scripts/learning_exercises.json`. Exercise 01 uses
`route_role: guided`; exercise 02 uses `route_role: both`. Both use
`starter_mode: guided`, keep the reference implementation under
`exercises/solutions/`, and provide three staged hints through the canonical README
specification rather than solved code.

When writing `example/main.*`, start with a short header comment that states the module focus and why it matters, then add intent-first comments before meaningful logic blocks so new developers can follow program flow quickly.

## Learning Metadata

- Difficulty:
- Estimated Time:
- Prerequisites:
- Cross-Language Lens:

## Learning Outcomes

- `<OUTCOME-ID-01>`: First measurable result shared by this module across tracks.
- `<OUTCOME-ID-02>`: Second measurable result, adapted idiomatically for the language.

## Quick Run

Run from the repository root:

~~~bash
python scripts/automation.py run-module --module-path languages/<language>/<level>/<module>
~~~

### Observe, Predict, Modify

State whether the example uses fixed data or waits for keyboard input. Provide a
concrete input and expected result, explain why that result follows, and suggest
one small change for the learner to predict before running again. Identify any
input validation deliberately left to a later module.

## Topics Covered

- Topic 1
- Topic 2
- Topic 3

## Common Pitfalls

- Pitfall 1
- Pitfall 2

## Cross-Language Notes

- Comparison point 1
- Comparison point 2
- Comparison point 3

## Exercise Focus

- exercises/01.<ext> or Exercise01.java: short task summary.
- exercises/02.<ext> or Exercise02.java: short task summary.

### Exercise Specs

1. exercises/01.<ext> or Exercise01.java
- Input:
- Output:
- Edge cases:

2. exercises/02.<ext> or Exercise02.java
- Input:
- Output:
- Edge cases:

## Check Your Work

Run from the repository root after implementing a starter:

~~~bash
python scripts/automation.py check-exercise --language <language> --level <level> --module <module> --exercise 01
~~~

Change `--exercise 01` to `--exercise 02` for the second task. Consult `exercises/solutions/` only after making a complete attempt.

Ask for the least revealing hint first:

~~~bash
python scripts/automation.py hint-exercise --language <language> --level <level> --module <module> --exercise 01 --stage 1
~~~

Stages are conceptual, structural, and idiomatic API guidance. They must never reveal
the reference solution.

### Visible Practice Cases

Show a normal input and expected output for each exercise, plus its named boundary
cases from `scripts/learning_exercises.json`. Distinguish output fragments from
exact output, including prompts, spaces, and decimal formatting when required.
Explain that an unmodified starter is expected to fail until implemented.

## Checkpoint

- [ ] I understand the core ideas of this module.
- [ ] I can run and explain the example.
- [ ] I completed exercise 01.
- [ ] I completed exercise 02.
