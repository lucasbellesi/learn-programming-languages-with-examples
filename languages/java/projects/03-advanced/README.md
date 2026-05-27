# 03 Advanced Capstone: Course Enrollment Manager

## Goal

Model courses and enrollments with Java classes, invariants, defensive copies, polymorphic reporting, and generic helpers.

## Learning Metadata

- Difficulty: Intermediate.
- Estimated Time: 60-90 minutes.
- Prerequisites: All `03-advanced` modules, especially `constructors-and-invariants`, `copy-and-move-semantics`, `inheritance-and-polymorphism`, and `templates-basics`.
- Learning Focus: Integrate custom types, guarded state changes, copy boundaries, and reusable reporting in one small object-oriented program.

## Quick Run

```bash
javac -d build/java languages/java/projects/03-advanced/Main.java
java -cp build/java Main
```

## Requirements

- Define a `Student` record with validated fields.
- Define a `Course` class with title, capacity, enroll, drop, and status behavior.
- Prevent enrollment beyond capacity and duplicate student IDs.
- Return immutable snapshots instead of internal mutable lists.
- Print multiple reportable objects through one generic helper.

## Concepts Practiced

- Records and classes.
- Constructor-enforced invariants.
- Defensive copies with `List.copyOf`.
- Interfaces and polymorphic reporting.
- Generic methods and generic containers.

## Sample Output

```text
Course Enrollment Report
Course: JavaAdvanced | 2/2 enrolled
Course: Algorithms | 1/3 enrolled
Overflow accepted: false
Catalog courses after external clear: 2
JavaAdvanced roster snapshot: 2
```

## Cross-Language Notes

- Compared with C++, Java uses references and defensive copies instead of explicit move constructors.
- Relative to Python, Java makes the model boundaries more verbose but more compile-time checked.
- Compared with TypeScript, Java uses nominal interfaces and JVM collection APIs for snapshots.

## What To Check

- course capacity and duplicate student rules are enforced
- external list changes do not mutate the catalog
- report output reflects the final object state
- generic reporting works for more than one concrete object

## Extension Ideas

- Add waitlist behavior.
- Read enrollment commands from a file.
- Add grade summaries per course.
