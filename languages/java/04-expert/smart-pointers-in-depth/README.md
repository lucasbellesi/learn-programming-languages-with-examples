# Smart Pointers in Depth (Java)

This module adapts smart pointer ideas to Java through strong references, explicit ownership slots, defensive copies, `Optional`, and `WeakReference`.

## Learning Metadata

- Difficulty: Advanced.
- Estimated Time: 45-60 minutes.
- Prerequisites: `04-expert/memory-management-and-raii`.
- Cross-Language Lens: Compare explicit ownership tools in C++ with managed references, pointer conventions, and weak-reference patterns elsewhere.

## Quick Run

~~~bash
javac -d build/java languages/java/04-expert/smart-pointers-in-depth/example/Main.java
java -cp build/java Main
~~~

## Topics Covered

- Strong references as normal object ownership in Java.
- Moving a reference between explicit owner slots.
- Clearing old owners so ownership transfer is visible.
- Returning defensive snapshots instead of mutable internals.
- Using `Optional` for empty ownership slots.
- Using `WeakReference` for non-owning observation.

## Common Pitfalls

- Assuming garbage collection makes ownership design irrelevant.
- Keeping accidental strong references in caches or observers.
- Returning mutable internal collections instead of defensive snapshots.
- Using `WeakReference` where a normal strong dependency is simpler.
- Treating `Optional` as storage instead of an API boundary signal.

## Cross-Language Notes

- Java does not expose C++-style smart pointers, so the comparison moves to references, ownership protocols, defensive copying, and `WeakReference`.
- Compared with C++, ownership is usually expressed through object boundaries and method contracts rather than pointer types.
- Compared with C# and Python, Java makes empty slots explicit with `Optional` and named reference types.
- The learner goal is to make aliasing, ownership transfer, and weak observation visible in a managed runtime.

## Exercise Focus

- exercises/Exercise01.java: move an owned document reference between holders.
- exercises/Exercise02.java: observe cache entries through `WeakReference`.

### Exercise Specs

1. exercises/Exercise01.java
- Input: none.
- Output: ownership transfer logs before and after moving.
- Edge cases: moving from an empty owner; destination already holding another object.

2. exercises/Exercise02.java
- Input: none.
- Output: alive/expired cache lookup logs.
- Edge cases: expired weak reference; cache miss.

## Checkpoint

- [ ] I can explain strong vs weak references in Java.
- [ ] I can model an ownership transfer by clearing the previous owner.
- [ ] I can return defensive snapshots instead of shared mutable internals.
- [ ] I can choose when a weak observer is appropriate.
- [ ] I completed exercises/Exercise01.java.
- [ ] I completed exercises/Exercise02.java.
