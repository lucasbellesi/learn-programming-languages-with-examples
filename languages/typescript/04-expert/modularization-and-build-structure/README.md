# Modularization and Build Structure

This module shows how to split a TypeScript console program into reusable files with explicit imports and exported types.

## Learning Metadata

- Difficulty: Advanced.
- Estimated Time: 30-45 minutes.
- Prerequisites: `03-advanced/structs-and-classes` and `04-expert/performance-and-profiling-basics`.
- Cross-Language Lens: Compare TypeScript imports and shared type exports with header/source splits in C++ and package layouts in Go.

## Quick Run

~~~bash
npm run build:typescript
node build/typescript/04-expert/modularization-and-build-structure/example/main.js
~~~

## Topics Covered

- Splitting logic across multiple `.ts` files.
- Exporting shared types and helper functions.
- Keeping orchestration in `main` and reusable logic in imported modules.
- Designing module boundaries around one responsibility each.

## Common Pitfalls

- Leaving all logic in `main.ts` and calling it modular.
- Creating circular imports accidentally.
- Hiding useful shared types inside one file instead of exporting them.
- Mixing formatting code with calculation code.

## Exercise Focus

- exercises/01.ts: extract validation and reporting helpers for a config summary.
- exercises/02.ts: separate parsing and statistics helpers for an event log.

### Exercise Specs

1. exercises/01.ts
- Input: none.
- Output: a validated configuration summary with reusable helper functions.
- Edge cases: missing service name; invalid retry count.

2. exercises/02.ts
- Input: none.
- Output: parsed event counts plus a short summary report.
- Edge cases: malformed lines; empty input arrays.

## Checkpoint

- [ ] I can split a program into modules with explicit imports and exports.
- [ ] I can place shared types in the module that owns the concept.
- [ ] I can keep `main` focused on orchestration instead of business logic.
- [ ] I completed exercises/01.ts.
- [ ] I completed exercises/02.ts.
