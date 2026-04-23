# Go 04 Expert

This level extends the Go track into resource cleanup, pointers, concurrency, performance, and larger-structure design.

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

- Use `defer` and explicit close patterns for predictable cleanup.
- Reason about pointers, aliases, and ownership-style transfer examples.
- Build concurrent examples with goroutines, channels, and protected shared data.
- Measure simple hot paths and organize larger programs across packages and files.

## Done When

- [ ] You completed every module in this level.
- [ ] You solved all exercises (`01.go` and `02.go`) for each module.
- [ ] You can explain cleanup, concurrency, and performance tradeoffs.
- [ ] You completed project `languages/go/projects/04-expert`.

## Study Tip

Use this level to compare Go's `defer`, pointers, goroutines, and package-oriented design with the more object-heavy expert tracks in C++ and C#.
