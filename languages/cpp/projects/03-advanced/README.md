# 03 Advanced Capstone: Course Enrollment Manager

## Goal

Model courses and enrollments with classes and vectors.

## Learning Metadata

- Difficulty: Intermediate.
- Estimated Time: 60-90 minutes.
- Prerequisites: All `03-advanced` modules, especially `structs-and-classes`, `constructors-and-invariants`, and `inheritance-and-polymorphism`.
- Learning Focus: Integrate custom types, guarded state changes, and reusable behavior in a program with more than one object in play.

## Quick Run

```bash
g++ -std=c++17 -Wall -Wextra -pedantic main.cpp -o advanced_capstone
./advanced_capstone
```

## Requirements

- Define a `Course` class with title and capacity.
- Provide methods for enroll, drop, and print status.
- Prevent enrollment beyond capacity.
- Demonstrate multiple course objects.

## Sample Output

```text
Course: CppBasics | 2/2 enrolled
Course: Algorithms | 1/3 enrolled
```

## What To Check

- object or struct state changes respect capacity and invariant rules
- repeated operations keep the final model state consistent
- printed status lines reflect the actual final state of the system

## Extension Ideas

- Add student IDs.
- Add waitlist behavior.
