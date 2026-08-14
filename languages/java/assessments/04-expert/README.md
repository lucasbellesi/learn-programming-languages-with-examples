# Assessment 04: Expert

## Goal

Prove you can combine immutable data ownership, concurrent work distribution, synchronized aggregation, and deterministic resource cleanup in Java.

## Task

Write a program that:

1. Keeps assessment values in an immutable owned snapshot.
2. Splits work across multiple executor tasks.
3. Computes a local total, minimum, and maximum for each worker.
4. Uses a synchronized aggregation boundary for shared summary state.
5. Closes the executor predictably.
6. Prints worker partial sums in deterministic worker order and the final summary.

## Learning Metadata

- Difficulty: Advanced.
- Estimated Time: 45-60 minutes.
- Prerequisites: All `04-expert` modules, especially `memory-management-and-raii`, `smart-pointers-in-depth`, and `concurrency-basics`.
- Learning Focus: Demonstrate explicit lifetime management, safe task coordination, local-result design, and shared aggregation under expert-level constraints.

## Learning Outcomes

- `EXP-MEM-02`
- `EXP-CON-01`
- `EXP-PER-01`
- `EXP-MOD-01`

## Quick Run

Run the reference solution from the repository root:

```bash
python scripts/automation.py check-checkpoint --language java --kind assessment --level 04-expert --solution
```

## Expected Output

```text
Worker 0 partial sum: 48
Worker 1 partial sum: 97
Worker 2 partial sum: 60

Final summary:
Total: 205
Minimum: 2
Maximum: 45
Executor terminated: true
```

## Cross-Language Notes

- Compared with C++, Java owns object lifetimes through references but still requires explicit executor cleanup.
- Relative to C#, `ExecutorService` and `Future` provide the task boundary while synchronized methods protect aggregation.
- Printing only after ordered future collection keeps observable output stable even when worker completion order changes.

## Check Your Work

Implement the task in `starter/`, then run from the repository root:

```bash
python scripts/automation.py check-checkpoint --language java --kind assessment --level 04-expert
```

Use `--solution` only after completing a full attempt. Each failed case reports targeted feedback without exposing the implementation.

## What To Check

- every input value belongs to exactly one worker range
- local results combine into the correct total, minimum, and maximum
- shared aggregation remains correct regardless of task completion order
- the input snapshot cannot be mutated externally
- the executor is terminated before the final report completes
