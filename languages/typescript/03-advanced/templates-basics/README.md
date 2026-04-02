# Templates Basics

This module adapts the generic-programming idea to TypeScript generics.

## Learning Metadata

- Difficulty: Advanced.
- Estimated Time: 30-45 minutes.
- Prerequisites: `03-advanced/structs-and-classes` and `03-advanced/inheritance-and-polymorphism`.
- Cross-Language Lens: Compare C++ templates, C# generics, Go type parameters, Python type hints, and TypeScript generics as related but not identical tools.

## Quick Run

~~~bash
npm run build:typescript
node build/typescript/03-advanced/templates-basics/example/main.js
~~~

## Topics Covered

- Generic functions.
- Generic containers.
- Reusable helpers that preserve type information.
- Light constraints when they clarify the API.

## Common Pitfalls

- Adding generics when a concrete helper would be clearer.
- Forgetting that generic code still needs readable names and behavior.
- Over-constraining a type parameter too early.

## Cross-Language Notes

- Compared with C++, this concept broadens from templates into each language's own reusable generic abstraction model.
- Relative to Go and C#, TypeScript generics stay expressive without runtime specialization, while Python treats the same idea more informally.
- The useful comparison is how each language generalizes logic without abandoning type clarity.

## Exercise Focus

- exercises/01.ts: write a generic first-element helper.
- exercises/02.ts: write a generic pair wrapper.

### Exercise Specs

1. exercises/01.ts
- Input: one line of tokens.
- Output: the first token.
- Edge cases: empty input should print an error.

2. exercises/02.ts
- Input: two values.
- Output: a generic pair rendered in order.
- Edge cases: missing second value should print an error.

## Checkpoint

- [ ] I can write a generic helper that preserves the input type.
- [ ] I can recognize when a generic wrapper reduces duplication.
- [ ] I can keep generic examples simpler than the underlying type theory.
- [ ] I completed exercises/01.ts.
- [ ] I completed exercises/02.ts.
