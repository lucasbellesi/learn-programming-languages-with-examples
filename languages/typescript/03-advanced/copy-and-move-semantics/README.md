# Copy and Move Semantics

This module adapts the C++ ownership topic to TypeScript by focusing on reference behavior, shallow copies, and explicit cloning.

## Learning Metadata

- Difficulty: Advanced.
- Estimated Time: 30-45 minutes.
- Prerequisites: `03-advanced/structs-and-classes` and `02-core/algorithms-basics`.
- Cross-Language Lens: Compare C++ copy and move rules with TypeScript reference sharing, spread copies, and deep-clone helpers.

## Quick Run

~~~bash
npm run build:typescript
node build/typescript/03-advanced/copy-and-move-semantics/example/main.js
~~~

## Topics Covered

- Reference aliasing.
- Shallow copy with spread syntax.
- Deep copy with explicit helper functions.
- Deciding when shared state is safe.

## Common Pitfalls

- Assuming spread syntax deep-copies nested objects.
- Mutating an alias and expecting the original to stay unchanged.
- Cloning blindly without understanding the data shape.

## Cross-Language Notes

- TypeScript adapts this topic through reference identity, shallow copies, and explicit clone helpers instead of real move operations.
- Compared with Python, static types help describe object shape, but assignment still shares runtime identity by default.
- The key comparison is how aliasing behaves in a typed JavaScript runtime versus a native ownership model.

## Exercise Focus

- exercises/01.ts: show shallow copy behavior on a nested object.
- exercises/02.ts: write a deep-clone helper for a small inventory model.

### Exercise Specs

1. exercises/01.ts
- Input: one product name and one quantity.
- Output: original and copied records after a nested update.
- Edge cases: negative quantity should print an error.

2. exercises/02.ts
- Input: item name, quantity, and reserved quantity.
- Output: original and cloned inventory states after a clone-only update.
- Edge cases: invalid counts; negative values.

## Checkpoint

- [ ] I can explain why object variables share references by default.
- [ ] I can tell the difference between shallow and deep copies.
- [ ] I can write an explicit clone helper when nested data requires it.
- [ ] I completed exercises/01.ts.
- [ ] I completed exercises/02.ts.
