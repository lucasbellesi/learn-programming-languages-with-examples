# C++ Learning Track (C++17)

This track teaches C++ through small, runnable programs and focused exercises.

## Learning Levels

1. [00-setup](./00-setup/README.md)
2. [01-foundations](./01-foundations/README.md)
3. [02-core](./02-core/README.md)
4. [03-advanced](./03-advanced/README.md)
5. [04-expert](./04-expert/README.md)

Use progress tracking: [CHECKLIST.md](./CHECKLIST.md)
  
Module README format reference: [MODULE_README_STYLE.md](./MODULE_README_STYLE.md)

## Modules By Level

### 01-foundations

- [01-foundations/types-and-io](./01-foundations/types-and-io/README.md)
- [01-foundations/control-flow](./01-foundations/control-flow/README.md)
- [01-foundations/functions](./01-foundations/functions/README.md)
- [01-foundations/arrays-and-vectors](./01-foundations/arrays-and-vectors/README.md)
- [01-foundations/strings](./01-foundations/strings/README.md)
- [01-foundations/operators-and-expressions](./01-foundations/operators-and-expressions/README.md)
- [01-foundations/scope-and-lifetime-basics](./01-foundations/scope-and-lifetime-basics/README.md)
- [01-foundations/formatted-output-and-iomanip](./01-foundations/formatted-output-and-iomanip/README.md)

### 02-core

- [02-core/input-validation](./02-core/input-validation/README.md)
- [02-core/algorithms-basics](./02-core/algorithms-basics/README.md)
- [02-core/file-io-basics](./02-core/file-io-basics/README.md)
- [02-core/sorting-and-searching](./02-core/sorting-and-searching/README.md)
- [02-core/maps-and-frequency-counting](./02-core/maps-and-frequency-counting/README.md)
- [02-core/error-handling-and-defensive-programming](./02-core/error-handling-and-defensive-programming/README.md)

### 03-advanced

- [03-advanced/structs-and-classes](./03-advanced/structs-and-classes/README.md)
- [03-advanced/constructors-and-invariants](./03-advanced/constructors-and-invariants/README.md)
- [03-advanced/copy-and-move-semantics](./03-advanced/copy-and-move-semantics/README.md)
- [03-advanced/inheritance-and-polymorphism](./03-advanced/inheritance-and-polymorphism/README.md)
- [03-advanced/templates-basics](./03-advanced/templates-basics/README.md)

### 04-expert

- [04-expert/memory-management-and-raii](./04-expert/memory-management-and-raii/README.md)
- [04-expert/smart-pointers-in-depth](./04-expert/smart-pointers-in-depth/README.md)
- [04-expert/concurrency-basics](./04-expert/concurrency-basics/README.md)
- [04-expert/performance-and-profiling-basics](./04-expert/performance-and-profiling-basics/README.md)
- [04-expert/modularization-and-build-structure](./04-expert/modularization-and-build-structure/README.md)

## Concept Module Shape

Every concept module follows:

```text
module-name/
  README.md
  example/
    main.cpp
  exercises/
    01.cpp
    02.cpp
```

## Study Routine

1. Read module `README.md`.
2. Run `example/main.cpp`.
3. Solve `exercises/01.cpp`.
4. Solve `exercises/02.cpp`.
5. Mark progress in `CHECKLIST.md`.
6. Complete level capstone project in `projects/<level>/`.

## Capstone Projects

Use capstones to combine concepts in a realistic task flow:

- [projects/README.md](./projects/README.md)

## Level Assessments

Use assessments after each level to validate readiness before moving on:

- [assessments/README.md](./assessments/README.md)

## Hint Guides

- [01-foundations/HINTS.md](./01-foundations/HINTS.md)
- [02-core/HINTS.md](./02-core/HINTS.md)
- [01-foundations/SOLUTIONS.md](./01-foundations/SOLUTIONS.md)
- [02-core/SOLUTIONS.md](./02-core/SOLUTIONS.md)

## Build Command

```bash
g++ -std=c++17 -Wall -Wextra -pedantic file.cpp -o output
```

This track targets Windows (MSYS2/MinGW) and Linux (`g++`).
