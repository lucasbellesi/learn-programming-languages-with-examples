# Smart Pointers in Depth (Go)

This module adapts smart pointer ideas to Go pointers, nil-safe ownership slots, and mutation boundaries.

## Learning Metadata

- Difficulty: Expert.
- Estimated Time: 40-55 minutes.
- Prerequisites: `04-expert/memory-management-and-raii`, `03-advanced/copy-and-move-semantics`.
- Cross-Language Lens: Compare explicit ownership in C++ with managed references, pointers, and weak observers in the other tracks.
## Quick Run

~~~bash
go run example/main.go
~~~

## Topics Covered

- Choosing between values and pointers.
- Moving an owned pointer by assigning it and clearing the previous owner.
- Guarding optional pointers with nil checks.
- Making shared mutation explicit through pointer access.

## Common Pitfalls

- Using pointers everywhere even when values are simpler.
- Forgetting to nil the old owner after a transfer.
- Dereferencing optional pointers without checking for nil.
- Hiding shared mutation behind too many aliases.

## Exercise Focus

- exercises/01.go: move an owned note between holders.
- exercises/02.go: navigate parent-child pointers safely.

### Exercise Specs

1. exercises/01.go
- Input: none.
- Output: ownership transfer logs before and after moving.
- Edge cases: moving from an empty holder; destination already occupied.

2. exercises/02.go
- Input: none.
- Output: parent/child navigation logs with nil-safe checks.
- Edge cases: detached child pointer; missing parent pointer.

## Checkpoint

- [ ] I can explain when a pointer is useful in Go.
- [ ] I can model a transfer by clearing the previous owner.
- [ ] I can write nil-safe code around optional references.
- [ ] I completed exercises/01.go.
- [ ] I completed exercises/02.go.
