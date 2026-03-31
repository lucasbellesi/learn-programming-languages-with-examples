# Smart Pointers in Depth (C#)

This module adapts smart pointer ideas to managed references, ownership transfer, and weak observation in C#.

## Learning Metadata

- Difficulty: Advanced.
- Estimated Time: 45-60 minutes.
- Prerequisites: `04-expert/memory-management-and-raii`.
- Cross-Language Lens: Compare explicit ownership tools in C++ with managed references, pointer conventions, and weak-reference patterns elsewhere.

## Quick Run

~~~bash
dotnet run --project example/smart-pointers-in-depth-example.csproj
~~~

## Topics Covered

- Treating nullable references as explicit ownership slots.
- Moving an owned reference by transferring it and clearing the original holder.
- Using `WeakReference<T>` for non-owning observation.
- Distinguishing strong lifetime responsibility from temporary access.

## Common Pitfalls

- Assuming the garbage collector makes ownership design irrelevant.
- Keeping accidental strong references in caches or observers.
- Using `WeakReference<T>` where a normal strong dependency is simpler.
- Forgetting to clear the old owner after a transfer.

## Exercise Focus

- exercises/01.cs: move an owned document reference between holders.
- exercises/02.cs: observe cache entries through `WeakReference<T>`.

### Exercise Specs

1. exercises/01.cs
- Input: none.
- Output: ownership transfer logs before and after moving.
- Edge cases: moving from an empty owner; destination already holding another object.

2. exercises/02.cs
- Input: none.
- Output: alive/expired cache lookup logs.
- Edge cases: expired weak reference; cache miss.

## Checkpoint

- [ ] I can explain strong vs weak references in C#.
- [ ] I can model an ownership transfer by clearing the previous owner.
- [ ] I can choose when a weak observer is appropriate.
- [ ] I completed exercises/01.cs.
- [ ] I completed exercises/02.cs.
