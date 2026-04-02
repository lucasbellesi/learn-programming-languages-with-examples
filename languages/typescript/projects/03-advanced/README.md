# 03 Advanced Capstone: Course Enrollment Manager

## Goal

Model courses and enrollments with classes and guarded state updates in TypeScript.

## Learning Metadata

- Difficulty: Advanced.
- Estimated Time: 60-90 minutes.
- Prerequisites: All `03-advanced` modules, especially `structs-and-classes`, `constructors-and-invariants`, and `inheritance-and-polymorphism`.
- Learning Focus: Integrate object modeling, guarded state changes, and reusable behavior in a program with more than one object in play.

## Quick Run

~~~bash
npm run build:typescript
node build/typescript/projects/03-advanced/main.js
~~~

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

## Extension Ideas

- Add student IDs.
- Add waitlist behavior.
