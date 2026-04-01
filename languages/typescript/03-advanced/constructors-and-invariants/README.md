# Constructors and Invariants

This module focuses on constructors that reject invalid state and keep objects trustworthy.

## Learning Metadata

- Difficulty: Advanced.
- Estimated Time: 30-45 minutes.
- Prerequisites: `03-advanced/structs-and-classes` and `02-core/input-validation`.
- Cross-Language Lens: Compare constructor validation across C++, C#, Go factory patterns, Python initializers, and TypeScript classes.

## Quick Run

~~~bash
npm run build:typescript
node build/typescript/03-advanced/constructors-and-invariants/example/main.js
~~~

## Topics Covered

- Constructor guards.
- Private mutable state with public methods.
- Preventing impossible states.
- Keeping mutation rules near the data they protect.

## Common Pitfalls

- Allowing invalid values into the constructor and hoping later methods fix them.
- Exposing fields that bypass invariant checks.
- Returning partially initialized objects.

## Exercise Focus

- exercises/01.ts: build a validated bank account.
- exercises/02.ts: build a temperature range that preserves `minimum <= maximum`.

### Exercise Specs

1. exercises/01.ts
- Input: owner and opening balance.
- Output: account summary or an error.
- Edge cases: empty owner; negative opening balance.

2. exercises/02.ts
- Input: minimum and maximum temperatures.
- Output: validated range or an error.
- Edge cases: minimum above maximum; invalid numbers.

## Checkpoint

- [ ] I can encode business rules directly in the constructor.
- [ ] I can keep object state valid after later method calls.
- [ ] I can explain why rejecting invalid construction simplifies later code.
- [ ] I completed exercises/01.ts.
- [ ] I completed exercises/02.ts.
