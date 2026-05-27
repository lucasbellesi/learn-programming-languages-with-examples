# Copy and Move Semantics (Java)

This module adapts copy and move semantics to Java through references, aliasing, defensive copies, and immutable views.

## Learning Metadata

- Difficulty: Intermediate.
- Estimated Time: 35-50 minutes.
- Prerequisites: `03-advanced/structs-and-classes`, `03-advanced/constructors-and-invariants`, `03-advanced/templates-basics`.
- Cross-Language Lens: Compare C++ ownership transfer with Java's reference assignment, copying helpers, and immutable collection boundaries.

## Quick Run

~~~bash
javac -d build/java languages/java/03-advanced/copy-and-move-semantics/example/Main.java
java -cp build/java Main
~~~

## Topics Covered

- Reference assignment and aliasing.
- Shallow copies vs defensive copies.
- Immutable snapshots with `List.copyOf`.
- Transfer-style updates that make ownership boundaries explicit.

## Common Pitfalls

- Assuming `=` duplicates an object.
- Returning internal mutable collections directly.
- Copying an object but still sharing nested mutable state.
- Confusing Java references with C++ move semantics.

## Cross-Language Notes

- Java has references and garbage collection, not C++ move constructors.
- Compared with Python and TypeScript, Java can use constructors and collection APIs to make copy boundaries explicit.
- Compared with Go, Java reference sharing is common for objects, while records and immutable lists help make state safer.
- The core comparison is accidental sharing versus deliberate copying.

## Exercise Focus

- exercises/Exercise01.java: clone a buffer and transfer values into a new buffer.
- exercises/Exercise02.java: protect a task list with defensive copying.

### Exercise Specs

1. exercises/Exercise01.java
- Input: buffer size.
- Output: sizes after clone and transfer operations.
- Edge cases: zero size; negative size.

2. exercises/Exercise02.java
- Input: task names.
- Output: internal task count after an external list changes.
- Edge cases: empty task list; repeated task names.

## Checkpoint

- [ ] I can explain why assigning an object variable copies a reference.
- [ ] I can create a defensive copy of a mutable collection.
- [ ] I can return immutable snapshots instead of internal state.
- [ ] I completed exercises/Exercise01.java.
- [ ] I completed exercises/Exercise02.java.
