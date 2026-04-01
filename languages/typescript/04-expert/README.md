# TypeScript 04 Expert

This level adapts expert topics to TypeScript's runtime model: explicit cleanup, reference identity, async concurrency, performance measurement, and modular structure.

## Learning Metadata

- Difficulty: Advanced.
- Estimated Time: 4-6 hours across modules, project, and assessment.
- Prerequisites: Completion of `03-advanced` plus its project or assessment checkpoint.
- Study Strategy: Work through the modules in order, then the capstone, then the assessment, and compare which expert ideas map directly from C++ and which need a TypeScript-specific interpretation.

## Module Order

1. [memory-management-and-raii](./memory-management-and-raii/README.md)
2. [smart-pointers-in-depth](./smart-pointers-in-depth/README.md)
3. [concurrency-basics](./concurrency-basics/README.md)
4. [performance-and-profiling-basics](./performance-and-profiling-basics/README.md)
5. [modularization-and-build-structure](./modularization-and-build-structure/README.md)

Track progress in [../CHECKLIST.md](../CHECKLIST.md).

## Study Tip

Treat this level as a translation exercise: TypeScript does not have RAII or move semantics in the C++ sense, so focus on explicit cleanup, reference behavior, and event-loop concurrency instead of forcing one-to-one vocabulary matches.
