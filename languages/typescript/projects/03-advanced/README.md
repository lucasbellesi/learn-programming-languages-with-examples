# 03 Advanced Capstone: Course Enrollment Manager

## Goal

Model courses and enrollments with classes and guarded state updates in TypeScript.

## Learning Metadata

- Difficulty: Advanced.
- Estimated Time: 60-90 minutes.
- Prerequisites: All `03-advanced` modules, especially `structs-and-classes`, `constructors-and-invariants`, and `inheritance-and-polymorphism`.
- Learning Focus: Integrate object modeling, guarded state changes, and reusable behavior in a program with more than one object in play.

## Learning Outcomes

- `ADV-MOD-01`
- `ADV-INV-02`
- `ADV-POL-01`
- `ADV-GEN-01`

## Quick Run

Run the reference solution from the repository root:

```bash
python scripts/automation.py check-checkpoint --language typescript --kind project --level 03-advanced --solution
```

## Requirements

- Define a `Course` class with title and capacity.
- Provide methods for enroll, drop, and print status.
- Prevent enrollment beyond capacity.
- Demonstrate multiple course objects.

## Sample Output

```text
Course: TypeScriptBasics | 2/2 enrolled
Course: Algorithms | 1/3 enrolled
```

## Cross-Language Notes

- Compared with the C++ capstone, this version maps the same advanced modeling goal onto classes plus a structural type system.
- Relative to C# and Python, it sits between strict object modeling and scripting-level flexibility.
- The important comparison is which abstraction boundaries are checked at compile time and which remain runtime conventions.

## What To Check

- object state changes respect capacity and invariant rules
- repeated operations keep the final model state consistent
- printed status lines reflect the actual final state of the system

## Check Your Work

Implement the task in `starter/`, then run from the repository root:

```bash
python scripts/automation.py check-checkpoint --language typescript --kind project --level 03-advanced
```

Use `--solution` only after completing a full attempt. Each failed case reports targeted feedback without exposing the implementation.

## Extension Ideas

- Add student IDs.
- Add waitlist behavior.
