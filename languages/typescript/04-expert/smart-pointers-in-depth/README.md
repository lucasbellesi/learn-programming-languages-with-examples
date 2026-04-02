# Smart Pointers in Depth

This module adapts smart pointer ideas to TypeScript references, ownership transfer conventions, and explicit alias management.

## Learning Metadata

- Difficulty: Advanced.
- Estimated Time: 30-45 minutes.
- Prerequisites: `04-expert/memory-management-and-raii` and `03-advanced/copy-and-move-semantics`.
- Cross-Language Lens: Compare C++ smart pointers with TypeScript object references, transfer-by-convention, and cloning when aliases become risky.

## Quick Run

~~~bash
npm run build:typescript
node build/typescript/04-expert/smart-pointers-in-depth/example/main.js
~~~

## Topics Covered

- Representing an owned reference with `T | null`.
- Moving ownership by assigning a reference and clearing the previous owner.
- Detecting shared aliases explicitly.
- Choosing between transfer, clone, and shared access.

## Common Pitfalls

- Treating object references as automatic deep copies.
- Forgetting to clear the previous owner after a transfer.
- Updating nested state through an alias without realizing it is shared.
- Cloning blindly when a simpler ownership rule would work.

## Cross-Language Notes

- TypeScript adapts smart-pointer ideas through object references, nullable ownership slots, and explicit clone helpers.
- Compared with C++, assignment never means deep ownership transfer by itself, so aliasing deserves more attention.
- The comparison is most useful when deciding whether to share, move by convention, or clone.

## Exercise Focus

- exercises/01.ts: transfer an owned task between holders.
- exercises/02.ts: clone nested preferences before a local update.

### Exercise Specs

1. exercises/01.ts
- Input: none.
- Output: holder state before and after transfer.
- Edge cases: moving from an empty holder; destination already occupied.

2. exercises/02.ts
- Input: none.
- Output: original and cloned preference states after editing only the clone.
- Edge cases: nested arrays or objects that would break a shallow copy.

## Checkpoint

- [ ] I can model ownership with a nullable reference slot.
- [ ] I can explain why assignment shares object identity in TypeScript.
- [ ] I can decide when to transfer, share, or clone.
- [ ] I completed exercises/01.ts.
- [ ] I completed exercises/02.ts.

