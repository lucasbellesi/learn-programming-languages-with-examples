# Scope and Lifetime Basics

This module explains block scope and closure-based lifetime in beginner TypeScript programs.

## Learning Metadata

- Difficulty: Beginner.
- Estimated Time: 20-35 minutes.
- Prerequisites: 01-foundations/functions and 01-foundations/control-flow.
- Cross-Language Lens: Compare block scope everywhere, then contrast TypeScript closures and GC-managed lifetime with C++ stack lifetime.

## Quick Run

~~~bash
npm run build:typescript
node build/typescript/01-foundations/scope-and-lifetime-basics/example/main.js
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

## Checkpoint

- [ ] I can explain the main TypeScript idea in this module.
- [ ] I can run the example and describe the output.
- [ ] I completed exercises/01.ts.
- [ ] I completed exercises/02.ts.
