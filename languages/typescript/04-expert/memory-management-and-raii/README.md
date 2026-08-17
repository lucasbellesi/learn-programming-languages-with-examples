# Managed Memory and Explicit Cleanup (TypeScript)

This module adapts RAII to TypeScript by focusing on explicit cleanup, `try/finally`, and disposable-style helpers.

## Learning Metadata

- Difficulty: Advanced.
- Estimated Time: 30-45 minutes.
- Prerequisites: `03-advanced/constructors-and-invariants` and `02-core/error-handling-and-defensive-programming`.
- Cross-Language Lens: Compare C++ destructor-driven cleanup with TypeScript's explicit `close` methods and `try/finally` scopes.

## Learning Outcomes

- `EXP-MEM-01`: Explain the language's resource and memory lifetime model.
- `EXP-MEM-02`: Guarantee deterministic cleanup for non-memory resources.

## Quick Run

Run from the repository root:

~~~bash
python scripts/automation.py run-module --module-path languages/typescript/04-expert/memory-management-and-raii
~~~

## Topics Covered

- Explicit cleanup through `close`.
- Wrapping resource usage in helper scopes.
- Guarding against use-after-close bugs.
- Separating resource lifetime from business logic.

## Common Pitfalls

- Assuming garbage collection will close files or sockets for you.
- Forgetting to close a resource on the error path.
- Reusing a closed resource because the object reference still exists.
- Mixing cleanup logic into unrelated application code.

## Cross-Language Notes

- TypeScript has garbage collection, but it does not automatically close files, sockets, or logical sessions for you.
- Compared with C++, this module shifts RAII into explicit `close` plus `try/finally` patterns.
- The important comparison is deterministic cleanup versus eventual memory reclamation.

## Exercise Focus

- exercises/01.ts: use `try/finally` to close a temporary resource safely.
- exercises/02.ts: enforce closed-state guardrails in a reusable session object.

### Exercise Specs

1. exercises/01.ts
- Input: none.
- Output: setup, work, and cleanup messages in the correct order.
- Edge cases: cleanup must still happen after a simulated failure.

2. exercises/02.ts
- Input: none.
- Output: session logs before closing, after closing, and a guarded error message.
- Edge cases: repeated close calls; operations attempted after close.

## Check Your Work

Run from the repository root after implementing a starter:

```bash
python scripts/automation.py check-exercise --language typescript --level 04-expert --module memory-management-and-raii --exercise 01
```

Change `--exercise 01` to `--exercise 02` for the second task. Consult `exercises/solutions/` only after making a complete attempt.

## Checkpoint

- [ ] I can explain why garbage collection does not replace explicit cleanup.
- [ ] I can use `try/finally` to guarantee cleanup.
- [ ] I can guard a resource from use-after-close mistakes.
- [ ] I completed exercises/01.ts.
- [ ] I completed exercises/02.ts.

