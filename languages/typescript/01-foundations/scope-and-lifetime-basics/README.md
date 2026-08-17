# Scope and Lifetime Basics

This module explains block scope and closure-based lifetime in beginner TypeScript programs.

## Learning Metadata

- Difficulty: Beginner.
- Estimated Time: 20-35 minutes.
- Prerequisites: 01-foundations/functions and 01-foundations/control-flow.
- Cross-Language Lens: Compare block scope everywhere, then contrast TypeScript closures and GC-managed lifetime with C++ stack lifetime.

## Learning Outcomes

- `FND-SCP-01`: Predict name visibility across nested scopes.
- `FND-SCP-02`: Explain when values and resources cease to be usable.

## Quick Run

Run from the repository root:

~~~bash
python scripts/automation.py run-module --module-path languages/typescript/01-foundations/scope-and-lifetime-basics
~~~

## Topics Covered

- let and const block scope.
- Shadowing and why it can confuse readers.
- Closures that keep values alive after a function returns.
- Using scope to limit where names can be used.

## Common Pitfalls

- Reusing the same variable name in too many nested scopes.
- Assuming a closure copies the value instead of keeping access to it.
- Using var-style thinking in a let and const codebase.

## Cross-Language Notes

- In TypeScript, read this module through the native focus ?Scope and Lifetime Basics?; the shared folder name remains stable for side-by-side navigation.
- Use structural types, Node APIs, and explicit reference conventions to demonstrate how to predict name visibility across nested scopes.
- Compare observable behavior with the other tracks when learning to explain when values and resources cease to be usable; equivalent evidence matters more than identical syntax.

## Exercise Focus

- exercises/01.ts: build a closure-based counter that prints the next value on each call.
- exercises/02.ts: show how a nested block can safely shadow a variable name.

### Exercise Specs

1. exercises/01.ts
- Input: one integer start value and one integer number of calls.
- Output: the counter values in order.
- Edge cases: zero calls should print nothing; negative start values should still work.

2. exercises/02.ts
- Input: one word and one replacement word.
- Output: outer and inner values to show the scopes stay separate.
- Edge cases: empty words should print an error; identical words should still demonstrate two scopes.

## Check Your Work

Run from the repository root after implementing a starter:

```bash
python scripts/automation.py check-exercise --language typescript --level 01-foundations --module scope-and-lifetime-basics --exercise 01
```

Change `--exercise 01` to `--exercise 02` for the second task. Consult `exercises/solutions/` only after making a complete attempt.

## Checkpoint

- [ ] I can explain the main TypeScript idea in this module.
- [ ] I can run the example and describe the output.
- [ ] I completed exercises/01.ts.
- [ ] I completed exercises/02.ts.
