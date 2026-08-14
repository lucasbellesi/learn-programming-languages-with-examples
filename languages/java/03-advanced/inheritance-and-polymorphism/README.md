# Inheritance and Polymorphism (Java)

This module models behavior variation with interfaces and overriding implementations.

## Learning Metadata

- Difficulty: Intermediate.
- Estimated Time: 35-50 minutes.
- Prerequisites: `03-advanced/structs-and-classes`, `03-advanced/constructors-and-invariants`.
- Cross-Language Lens: Compare virtual dispatch, interfaces, and duck-typed behavior to see how polymorphism changes by language.

## Learning Outcomes

- `ADV-POL-01`: Program against a shared behavioral abstraction.
- `ADV-POL-02`: Use dynamic dispatch without unsafe type assumptions.

## Quick Run

Run from the repository root:

~~~bash
python scripts/automation.py run-module --module-path languages/java/03-advanced/inheritance-and-polymorphism
~~~

## Topics Covered

- Interfaces and required methods.
- Runtime polymorphism through shared interface references.
- Overriding concrete behavior in implementing classes.
- Aggregating mixed implementations in one list.

## Common Pitfalls

- Forgetting to implement required interface methods.
- Accessing implementation-only state from generic iteration code.
- Replacing polymorphism with `instanceof` checks.

## Cross-Language Notes

- Java interfaces define named contracts that classes explicitly implement.
- Compared with Go, Java uses nominal interface implementation; compared with Python, more mistakes are caught before execution.
- The key lesson is that polymorphism is a design idea first, not just a language feature.

## Exercise Focus

- exercises/Exercise01.java: extend shape model with `Triangle`.
- exercises/Exercise02.java: aggregate shapes in `List<Shape>`.

### Exercise Specs

1. exercises/Exercise01.java
- Input: triangle base and height.
- Output: computed area through overridden method.
- Edge cases: zero dimensions; decimal dimensions.

2. exercises/Exercise02.java
- Input: predefined shape objects.
- Output: total area through polymorphic iteration.
- Edge cases: empty shape list; mixed shape types.

## Check Your Work

Run from the repository root after implementing a starter:

```bash
python scripts/automation.py check-exercise --language java --level 03-advanced --module inheritance-and-polymorphism --exercise 01
```

Change `--exercise 01` to `--exercise 02` for the second task. Consult `exercises/solutions/` only after making a complete attempt.

## Checkpoint

- [ ] I can define interfaces with polymorphic methods.
- [ ] I can override behavior in implementing classes.
- [ ] I can use polymorphic collections safely.
- [ ] I completed exercises/Exercise01.java.
- [ ] I completed exercises/Exercise02.java.
