# Go 03 Advanced

This level starts advanced object modeling and type design.

## Learning Metadata

- Difficulty: Intermediate.
- Estimated Time: 4-6 hours across modules, project, and assessment.
- Prerequisites: Completion of `01-foundations` and `02-core`, including at least one checkpoint per level.
- Study Strategy: Compare abstraction patterns across languages as you go, trace object state changes by hand, then use the project and assessment to confirm the model sticks.

## Module Order

1. [structs-and-classes](./structs-and-classes/README.md)
2. [constructors-and-invariants](./constructors-and-invariants/README.md)
3. [copy-and-move-semantics](./copy-and-move-semantics/README.md)
4. [inheritance-and-polymorphism](./inheritance-and-polymorphism/README.md)
5. [templates-basics](./templates-basics/README.md)

Track progress in [../CHECKLIST.md](../CHECKLIST.md).

## Level Outcomes

- Model domain entities with structs, methods, and clear invariants.
- Explain how values, pointers, and copies affect program state.
- Apply interfaces for behavior variation across related types.
- Use generic functions and types for small reusable abstractions.

## Done When

- [ ] You completed every module in this level.
- [ ] You solved all exercises (`01.go` and `02.go`) for each module.
- [ ] You can explain where constructors, interfaces, and pointer semantics matter.
- [ ] You completed project `languages/go/projects/03-advanced`.

## Study Tip

Use `templates-basics` last to generalize previous patterns with Go type parameters and constraints.
