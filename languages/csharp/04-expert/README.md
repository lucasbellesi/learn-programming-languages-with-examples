# C# 04 Expert

This level is now fully implemented in C#.

## Learning Metadata

- Difficulty: Advanced.
- Estimated Time: 4-6 hours across modules, project, and assessment.
- Prerequisites: Completion of `03-advanced` plus its project or assessment checkpoint.
- Study Strategy: Finish the modules in order, then the capstone, then the assessment, and explicitly compare runtime, ownership, and scaling tradeoffs across languages.

## Module Order

1. [memory-management-and-raii](./memory-management-and-raii/README.md)
2. [smart-pointers-in-depth](./smart-pointers-in-depth/README.md)
3. [concurrency-basics](./concurrency-basics/README.md)
4. [performance-and-profiling-basics](./performance-and-profiling-basics/README.md)
5. [modularization-and-build-structure](./modularization-and-build-structure/README.md)

Track progress in [../CHECKLIST.md](../CHECKLIST.md).

## Level Outcomes

- Use `IDisposable` and lifetime-aware patterns for predictable cleanup.
- Reason about shared references, weak references, and ownership transfer examples.
- Build thread-safe examples with synchronized shared data.
- Measure simple hot paths and organize larger programs across projects and files.

## Done When

- [ ] You completed every module in this level.
- [ ] You solved all exercises (`01.cs` and `02.cs`) for each module.
- [ ] You can explain cleanup, thread-safety, and performance tradeoffs.
- [ ] You completed project `languages/csharp/projects/04-expert`.

## Study Tip

Use this level to move from deterministic cleanup into ownership modeling, concurrent coordination, performance measurement, and modular project structure.
