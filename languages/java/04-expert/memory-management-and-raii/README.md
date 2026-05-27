# Memory Management and RAII (Java)

This module adapts RAII to Java through `AutoCloseable` and `try-with-resources`.

## Learning Metadata

- Difficulty: Advanced.
- Estimated Time: 45-60 minutes.
- Prerequisites: `01-foundations/scope-and-lifetime-basics`, `03-advanced/constructors-and-invariants`, `03-advanced/copy-and-move-semantics`.
- Cross-Language Lens: Contrast deterministic cleanup in C++ with `IDisposable`, `defer`, context-manager style cleanup, and Java `try-with-resources`.

## Quick Run

~~~bash
javac -d build/java languages/java/04-expert/memory-management-and-raii/example/Main.java
java -cp build/java Main
~~~

## Topics Covered

- `AutoCloseable` resources.
- `try-with-resources` cleanup order.
- Idempotent `close` methods.
- Guarding methods after a resource has been released.
- Separating garbage-collected memory from external resource cleanup.

## Common Pitfalls

- Assuming garbage collection closes resources at the right time.
- Forgetting `try-with-resources` around files, streams, or custom resources.
- Reusing an object after it has already been closed.
- Making `close` unsafe to call more than once.

## Cross-Language Notes

- Java maps RAII-style cleanup to lexical `try-with-resources` scopes rather than destructors.
- Compared with C++, Java object lifetime and cleanup timing are deliberately separate.
- Compared with Go and Python, Java's cleanup contract is explicit through `AutoCloseable`.
- The learner goal is to make release points obvious and reliable.

## Exercise Focus

- exercises/Exercise01.java: owned integer buffer with deterministic cleanup.
- exercises/Exercise02.java: scope guard that proves nested cleanup order.

### Exercise Specs

1. exercises/Exercise01.java
- Input: integer `n`, then `n` integers.
- Output: sum and reversed sequence.
- Edge cases: `n <= 0`; invalid integer input.

2. exercises/Exercise02.java
- Input: none.
- Output: enter/close logs proving automatic cleanup.
- Edge cases: nested scopes; final active counter must return to zero.

## Checkpoint

- [ ] I can explain why `try-with-resources` gives deterministic cleanup.
- [ ] I can write a small `AutoCloseable` type.
- [ ] I can prevent work on a closed resource.
- [ ] I completed exercises/Exercise01.java.
- [ ] I completed exercises/Exercise02.java.
