# Java 04 Expert

This level starts the expert Java track with deterministic resource cleanup, clear boundaries between garbage-collected memory and external resources, and managed-reference ownership patterns.

## Learning Metadata

- Difficulty: Advanced.
- Estimated Time: 45-60 minutes per module.
- Prerequisites: Completion of `01-foundations`, `02-core`, and `03-advanced`.
- Study Strategy: Focus on resource lifetime first, then compare Java cleanup, ownership slots, defensive snapshots, and weak references with equivalent patterns in other tracks.

## Module Order

1. [memory-management-and-raii](./memory-management-and-raii/README.md)
2. [smart-pointers-in-depth](./smart-pointers-in-depth/README.md)

## Level Outcomes

- Explain why Java garbage collection does not replace deterministic resource cleanup.
- Use `try-with-resources` with `AutoCloseable`.
- Make `close` operations idempotent.
- Guard resource methods after close.
- Model reference ownership transfer by clearing the old owner.
- Use defensive snapshots and weak references deliberately.
- Compare Java cleanup with C++, C#, Go, Python, and TypeScript.

## Done When

- [ ] I ran `memory-management-and-raii/example/Main.java`.
- [ ] I completed both `memory-management-and-raii` exercises.
- [ ] I ran `smart-pointers-in-depth/example/Main.java`.
- [ ] I completed both `smart-pointers-in-depth` exercises.
- [ ] I can explain why file handles, sockets, and buffers should be closed predictably.
- [ ] I can implement a small `AutoCloseable` resource.
- [ ] I can explain when Java references are owning, shared, or weak by convention.

## Study Tip

Java's garbage collector manages memory, but it does not make external resources close at the exact time your program logic needs. Use `try-with-resources` when cleanup timing matters, and make ownership boundaries visible when several references can reach the same object.
