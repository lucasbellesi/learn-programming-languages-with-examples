# Inheritance and Polymorphism (Go)

This module models behavior variation with interfaces and dynamic dispatch.

## Quick Run

~~~bash
go run example/main.go
~~~

## Topics Covered

- Interfaces as behavior contracts.
- Struct types implementing shared methods.
- Runtime polymorphism through interface values.
- Aggregating mixed implementations in one slice.

## Common Pitfalls

- Expecting inheritance syntax instead of composition/interfaces.
- Forgetting one required method and not satisfying the interface.
- Leaking concrete-type assumptions into generic iteration code.

## Exercise Focus

- exercises/01.go: extend shape model with `Triangle`.
- exercises/02.go: aggregate shapes in `[]Shape`.

### Exercise Specs

1. exercises/01.go
- Input: triangle base and height.
- Output: computed area through interface method.
- Edge cases: zero dimensions; decimal dimensions.

2. exercises/02.go
- Input: predefined shape objects.
- Output: total area through polymorphic iteration.
- Edge cases: empty shape list; mixed shape types.

## Checkpoint

- [ ] I can define interface-based polymorphic contracts.
- [ ] I can implement shared behavior across multiple structs.
- [ ] I can use polymorphic slices safely.
- [ ] I completed exercises/01.go.
- [ ] I completed exercises/02.go.
