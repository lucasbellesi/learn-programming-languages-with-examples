# Ownership, Weak References, and Disposal (C#)

This module adapts smart pointer ideas to managed references, ownership transfer, and weak observation in C#.

## Learning Metadata

- Difficulty: Advanced.
- Estimated Time: 45-60 minutes.
- Prerequisites: `04-expert/memory-management-and-raii`.
- Cross-Language Lens: Compare explicit ownership tools in C++ with managed references, pointer conventions, and weak-reference patterns elsewhere.

## Learning Outcomes

- `EXP-OWN-01`: Model exclusive, shared, and non-owning relationships idiomatically.
- `EXP-OWN-02`: Prevent leaks, cycles, and stale observations in ownership graphs.

## Quick Run

Run from the repository root:

~~~bash
python scripts/automation.py run-module --module-path languages/csharp/04-expert/smart-pointers-in-depth
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

## Cross-Language Notes

- C# does not expose C++-style smart pointers, so the comparison moves to references, `IDisposable`, and `WeakReference`.
- Compared with C++, ownership is often social or API-level rather than encoded in the type alone.
- This module teaches how to make aliasing and lifetime choices visible even in a managed runtime.

## Exercise Focus

- exercises/01.cs: move an owned document reference between holders.
- exercises/02.cs: observe cache entries through `WeakReference<T>`.

### Exercise Specs

1. exercises/01.cs
- Input: source and destination document names, or `empty`, one per line.
- Output: ownership transfer logs before and after moving.
- Edge cases: moving from an empty holder; destination already occupied.

2. exercises/02.cs
- Input: `alive`, `expired`, or `missing` cache scenario.
- Output: alive/expired cache lookup logs.
- Edge cases: expired or detached reference; missing reference.

## Check Your Work

Run from the repository root after implementing a starter:

```bash
python scripts/automation.py check-exercise --language csharp --level 04-expert --module smart-pointers-in-depth --exercise 01
```

Change `--exercise 01` to `--exercise 02` for the second task. Consult `exercises/solutions/` only after making a complete attempt.

## Checkpoint

- [ ] I can explain strong vs weak references in C#.
- [ ] I can model an ownership transfer by clearing the previous owner.
- [ ] I can choose when a weak observer is appropriate.
- [ ] I completed exercises/01.cs.
- [ ] I completed exercises/02.cs.

