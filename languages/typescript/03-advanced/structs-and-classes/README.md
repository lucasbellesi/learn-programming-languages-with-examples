# Structs and Classes

This module introduces richer object modeling in TypeScript with interfaces and classes.

## Learning Metadata

- Difficulty: Advanced.
- Estimated Time: 30-45 minutes.
- Prerequisites: `02-core/algorithms-basics` and `01-foundations/arrays-and-vectors`.
- Cross-Language Lens: Compare C++ structs, C# classes, Go structs, Python classes, and TypeScript interfaces/classes as different tradeoffs for modeling state and behavior.

## Quick Run

~~~bash
npm run build:typescript
node build/typescript/03-advanced/structs-and-classes/example/main.js
~~~

## Topics Covered

- Interfaces for data shape.
- Classes for bundling data with methods.
- Readonly fields and derived methods.
- Arrays of custom objects.

## Common Pitfalls

- Using a class when a plain interface would be enough.
- Forgetting that object references stay shared by default.
- Mixing formatting logic directly into constructors.

## Exercise Focus

- exercises/01.ts: parse records into typed objects and print a summary.
- exercises/02.ts: model a simple class with a computed method.

### Exercise Specs

1. exercises/01.ts
- Input: one integer `n`, then `n` pairs of `name score`.
- Output: one typed summary line per record.
- Edge cases: `n <= 0`; missing tokens; invalid scores.

2. exercises/02.ts
- Input: label, quantity, and unit price.
- Output: class-based invoice summary with total.
- Edge cases: negative quantity or price should print an error.

## Checkpoint

- [ ] I can decide when an interface is enough and when a class helps.
- [ ] I can store custom objects in arrays and summarize them.
- [ ] I can move repeated behavior into methods instead of duplicating it.
- [ ] I completed exercises/01.ts.
- [ ] I completed exercises/02.ts.
