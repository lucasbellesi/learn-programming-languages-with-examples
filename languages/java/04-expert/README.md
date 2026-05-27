# Java 04 Expert

This level starts the expert Java track with deterministic resource cleanup and clear boundaries between garbage-collected memory and external resources.

## Learning Metadata

- Difficulty: Advanced.
- Estimated Time: 45-60 minutes for the current module.
- Prerequisites: Completion of `01-foundations`, `02-core`, and `03-advanced`.
- Study Strategy: Focus on resource lifetime first, then compare Java cleanup patterns with RAII, `defer`, context managers, and disposable objects in other tracks.

## Module Order

1. [memory-management-and-raii](./memory-management-and-raii/README.md)

## Level Outcomes

- Explain why Java garbage collection does not replace deterministic resource cleanup.
- Use `try-with-resources` with `AutoCloseable`.
- Make `close` operations idempotent.
- Guard resource methods after close.
- Compare Java cleanup with C++, C#, Go, Python, and TypeScript.

## Done When

- [ ] I ran `memory-management-and-raii/example/Main.java`.
- [ ] I completed both `memory-management-and-raii` exercises.
- [ ] I can explain why file handles, sockets, and buffers should be closed predictably.
- [ ] I can implement a small `AutoCloseable` resource.

## Study Tip

Java's garbage collector manages memory, but it does not make external resources close at the exact time your program logic needs. Use `try-with-resources` when cleanup timing matters.
