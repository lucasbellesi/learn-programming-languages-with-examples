# Java 04 Expert

This fully implemented level covers deterministic cleanup, managed-reference ownership, concurrent task coordination, JVM measurement discipline, and multi-file program structure.

## Learning Metadata

- Difficulty: Advanced.
- Estimated Time: 5-7 hours across modules, project, and assessment.
- Prerequisites: Completion of `01-foundations`, `02-core`, and `03-advanced`.
- Study Strategy: Progress from lifetime and ownership into concurrency, measurement, and source boundaries; compare the Java runtime and build model with each sibling track.

## Module Order

1. [memory-management-and-raii](./memory-management-and-raii/README.md)
2. [smart-pointers-in-depth](./smart-pointers-in-depth/README.md)
3. [concurrency-basics](./concurrency-basics/README.md)
4. [performance-and-profiling-basics](./performance-and-profiling-basics/README.md)
5. [modularization-and-build-structure](./modularization-and-build-structure/README.md)

## Level Outcomes

- Explain why Java garbage collection does not replace deterministic resource cleanup.
- Use `try-with-resources` with `AutoCloseable`.
- Make `close` operations idempotent.
- Guard resource methods after close.
- Model reference ownership transfer by clearing the old owner.
- Use defensive snapshots and weak references deliberately.
- Coordinate worker tasks with executors, futures, and blocking queues.
- Measure repeated JVM work without claiming one noisy timing is definitive.
- Split orchestration, domain logic, and formatting across Java source files.
- Compare Java cleanup with C++, C#, Go, Python, and TypeScript.

## Done When

- [ ] I ran `memory-management-and-raii/example/Main.java`.
- [ ] I completed both `memory-management-and-raii` exercises.
- [ ] I ran `smart-pointers-in-depth/example/Main.java`.
- [ ] I completed both `smart-pointers-in-depth` exercises.
- [ ] I ran `concurrency-basics/example/Main.java`.
- [ ] I completed both `concurrency-basics` exercises.
- [ ] I ran `performance-and-profiling-basics/example/Main.java`.
- [ ] I completed both `performance-and-profiling-basics` exercises.
- [ ] I compiled the multi-file `modularization-and-build-structure` example.
- [ ] I completed both `modularization-and-build-structure` exercises.
- [ ] I can explain why file handles, sockets, and buffers should be closed predictably.
- [ ] I can implement a small `AutoCloseable` resource.
- [ ] I can explain when Java references are owning, shared, or weak by convention.
- [ ] I can explain why executors must be shut down and why timing results vary.
- [ ] I completed `languages/java/projects/04-expert`.
- [ ] I completed `languages/java/assessments/04-expert`.

## Study Tip

Java's runtime removes some low-level work but not design responsibility. Keep resource release, task ownership, measurement boundaries, and source dependencies explicit even when the JVM manages memory and threads for you.
