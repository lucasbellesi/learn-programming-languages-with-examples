# Assessment 03: Advanced

## Goal

Prove you can combine Java records, classes, invariants, defensive copies, interfaces, and generics in one bounded assessment.

## Task

Write a program that:

1. Reads a course capacity.
2. Reads a number of enrollment attempts.
3. Reads each attempt as `StudentId Name`.
4. Rejects duplicate student IDs and enrollments beyond capacity.
5. Keeps the enrollment batch safe from later external-list changes.
6. Prints accepted/rejected counts and a final course report.

## Learning Metadata

- Difficulty: Intermediate.
- Estimated Time: 45-60 minutes.
- Prerequisites: All `03-advanced` modules, especially `constructors-and-invariants`, `copy-and-move-semantics`, `inheritance-and-polymorphism`, and `templates-basics`.
- Learning Focus: Demonstrate object modeling, guarded state updates, defensive copying, and reusable reporting under a small input contract.

## Quick Run

```bash
javac -d build/java languages/java/assessments/03-advanced/Main.java
java -cp build/java Main
```

## Sample Input

```text
2
4
S-101 Ana
S-202 Bob
S-202 Duplicate
S-303 Carla
```

## Sample Output

```text
Advanced Assessment Report
Course: JavaAdvanced | 2/2 enrolled
Accepted: 2
Rejected: 2
External attempts after clear: 0
Batch requests after external clear: 4
Roster snapshot: 2
```

## Cross-Language Notes

- Compared with C++, Java uses defensive copies and immutable snapshots instead of ownership transfer syntax.
- Relative to Python, Java makes invalid states more visible through constructors and explicit types.
- Compared with TypeScript, Java relies on nominal interfaces and JVM collection APIs for the reporting and snapshot boundaries.

## What To Check

- duplicate student IDs are rejected
- capacity overflow is rejected
- batch data survives external-list mutation
- final report values come from the modeled objects, not hardcoded text
