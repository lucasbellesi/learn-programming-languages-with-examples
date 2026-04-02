# Inheritance and Polymorphism (C#)

This module models behavior variation with abstract base classes and overrides.

## Learning Metadata

- Difficulty: Intermediate.
- Estimated Time: 35-50 minutes.
- Prerequisites: `03-advanced/structs-and-classes`, `03-advanced/constructors-and-invariants`.
- Cross-Language Lens: Compare virtual dispatch, interfaces, and duck-typed behavior to see how polymorphism changes by language.

## Quick Run

~~~bash
dotnet run --project example/inheritance-and-polymorphism-example.csproj
~~~

## Topics Covered

- Abstract base classes and derived implementations.
- Runtime polymorphism through base references.
- Overriding behavior with `override`.
- Iterating mixed concrete types through one common contract.

## Common Pitfalls

- Forgetting to mark base APIs as abstract or virtual.
- Calling derived-only members through base references.
- Duplicating behavior instead of relying on polymorphic dispatch.

## Cross-Language Notes

- C# stays close to the canonical object-oriented version, with inheritance and virtual dispatch feeling more uniform than in C++.
- Compared with Go and TypeScript, class hierarchies remain a more natural first-class teaching tool here.
- The useful comparison is how a managed runtime simplifies polymorphic object use without removing design tradeoffs.

## Exercise Focus

- exercises/01.cs: extend shape hierarchy with `Triangle`.
- exercises/02.cs: aggregate shapes in `List<Shape>`.

### Exercise Specs

1. exercises/01.cs
- Input: triangle base and height.
- Output: computed area through overridden method.
- Edge cases: zero dimensions; decimal dimensions.

2. exercises/02.cs
- Input: predefined shape objects.
- Output: total area through polymorphic iteration.
- Edge cases: empty shape list; mixed shape types.

## Checkpoint

- [ ] I can define abstract base classes with polymorphic methods.
- [ ] I can override behavior in derived classes.
- [ ] I can use polymorphic collections safely.
- [ ] I completed exercises/01.cs.
- [ ] I completed exercises/02.cs.
