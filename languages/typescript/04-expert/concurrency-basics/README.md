# Concurrency Basics

This module introduces TypeScript concurrency through async tasks, `Promise.all`, and work coordination on the event loop.

## Learning Metadata

- Difficulty: Advanced.
- Estimated Time: 45-60 minutes.
- Prerequisites: `02-core/algorithms-basics` and `03-advanced/templates-basics`.
- Cross-Language Lens: Compare thread-based concurrency in C++ or Go with TypeScript's event-loop concurrency, where tasks overlap without shared-memory threads by default.

## Quick Run

~~~bash
npm run build:typescript
node build/typescript/04-expert/concurrency-basics/example/main.js
~~~

## Topics Covered

- Launching independent async tasks.
- Preserving result order with `Promise.all`.
- Limiting concurrency with a worker-pool helper.
- Separating task coordination from task logic.

## Common Pitfalls

- Confusing concurrency with parallel CPU work.
- Awaiting inside a loop when independent work could overlap.
- Mutating shared arrays in confusing ways instead of returning results.
- Ignoring task failures inside a larger concurrent batch.

## Exercise Focus

- exercises/01.ts: fetch several async results and preserve display order.
- exercises/02.ts: process jobs with a maximum of two active workers.

### Exercise Specs

1. exercises/01.ts
- Input: none.
- Output: completed task results in the original request order.
- Edge cases: mixed delays; one task finishing earlier than the first request.

2. exercises/02.ts
- Input: none.
- Output: worker start/finish logs plus a final ordered summary.
- Edge cases: fewer jobs than workers; an empty job list.

## Checkpoint

- [ ] I can explain how `Promise.all` overlaps async work.
- [ ] I can preserve deterministic output even when completion order varies.
- [ ] I can limit concurrency without rewriting the task itself.
- [ ] I completed exercises/01.ts.
- [ ] I completed exercises/02.ts.
