# 03 Advanced Capstone: Course Enrollment Manager

## Goal

Model courses and enrollments with classes and guarded state updates.

## Learning Metadata

- Difficulty: Intermediate.
- Estimated Time: 60-90 minutes.
- Prerequisites: All `03-advanced` modules, especially `structs-and-classes`, `constructors-and-invariants`, and `inheritance-and-polymorphism`.
- Learning Focus: Integrate custom types, guarded state changes, and reusable behavior in a program with more than one object in play.

## Quick Run

```bash
dotnet run --project advanced-project.csproj
```

## Requirements

- Define a `Course` class with title and capacity.
- Provide methods for enroll, drop, and print status.
- Prevent enrollment beyond capacity.
- Demonstrate multiple course objects.

## Sample Output

```text
Course: CSharpBasics | 2/2 enrolled
Course: Algorithms | 1/3 enrolled
```

## Cross-Language Notes

- Compared with the C++ capstone, this version preserves the object-oriented learner goal with less manual ownership overhead.
- Relative to Go and TypeScript, class-based design remains the most direct path here.
- The main comparison is expressive object modeling under a managed runtime.

## What To Check

- object or struct state changes respect capacity and invariant rules
- repeated operations keep the final model state consistent
- printed status lines reflect the actual final state of the system

## Extension Ideas

- Add student IDs.
- Add waitlist behavior.
