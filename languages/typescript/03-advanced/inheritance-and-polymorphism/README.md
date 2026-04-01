# Inheritance and Polymorphism

This module introduces shared interfaces and subtype behavior in TypeScript.

## Learning Metadata

- Difficulty: Advanced.
- Estimated Time: 30-45 minutes.
- Prerequisites: `03-advanced/structs-and-classes` and `03-advanced/constructors-and-invariants`.
- Cross-Language Lens: Compare abstract classes, interfaces, and runtime dispatch across C++, C#, Go, Python, and TypeScript.

## Quick Run

~~~bash
npm run build:typescript
node build/typescript/03-advanced/inheritance-and-polymorphism/example/main.js
~~~

## Topics Covered

- Abstract base classes.
- Overridden methods.
- Arrays of base-type references.
- Runtime dispatch through a shared API.

## Common Pitfalls

- Using inheritance when composition would be simpler.
- Forgetting that polymorphism only helps when callers use the shared interface.
- Storing subtype-specific assumptions in base-type code.

## Exercise Focus

- exercises/01.ts: implement a polymorphic item hierarchy.
- exercises/02.ts: store mixed renderers behind a shared interface.

### Exercise Specs

1. exercises/01.ts
- Input: one product type and one numeric parameter.
- Output: a subtype-specific description line.
- Edge cases: unknown type; invalid numeric parameter.

2. exercises/02.ts
- Input: one label.
- Output: the same label rendered through two interface implementations.
- Edge cases: empty label should print an error.

## Checkpoint

- [ ] I can define a shared abstract API for multiple subtypes.
- [ ] I can call subtype behavior through a base-type collection.
- [ ] I can tell when an interface is enough without extra inheritance depth.
- [ ] I completed exercises/01.ts.
- [ ] I completed exercises/02.ts.
