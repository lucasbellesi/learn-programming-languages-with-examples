# Concept Template (Language-Agnostic)

Use this template when creating a new concept module in any track.
All section headings below are required by repository validation scripts.

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

## Checkpoint

- [ ] I understand the core ideas of this module.
- [ ] I can run and explain the example.
- [ ] I completed exercise 01.
- [ ] I completed exercise 02.
