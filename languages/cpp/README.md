# C++ Learning Track (C++17)

This track teaches core programming concepts in C++ using:

- A concept README for theory and pitfalls
- A runnable `example/main.cpp`
- Two practice exercises

## Who This Track Is For

This path is for beginners who are learning programming fundamentals and want practical, small C++ programs that compile on Windows and Linux.

## Roadmap

1. [00-setup](./00-setup/README.md)
2. [01-foundations overview](./01-foundations/README.md)
3. [02-core overview](./02-core/README.md)
4. [03-advanced overview](./03-advanced/README.md)
5. [04-expert overview](./04-expert/README.md)

Current concept modules inside `01-foundations`:

- [types-and-io](./01-foundations/types-and-io/README.md)
- [control-flow](./01-foundations/control-flow/README.md)
- [functions](./01-foundations/functions/README.md)
- [arrays-and-vectors](./01-foundations/arrays-and-vectors/README.md)
- [strings](./01-foundations/strings/README.md)

Current concept modules inside `02-core`:

- [input-validation](./02-core/input-validation/README.md)
- [algorithms-basics](./02-core/algorithms-basics/README.md)

Current concept modules inside `03-advanced`:

- [structs-and-classes](./03-advanced/structs-and-classes/README.md)

Current concept modules inside `04-expert`:

- [memory-management-and-raii](./04-expert/memory-management-and-raii/README.md)

Use the checklist: [CHECKLIST.md](./CHECKLIST.md)

## Concept Folder Structure

Each concept follows the same structure:

```text
concept-name/
  README.md
  example/
    main.cpp
  exercises/
    01.cpp
    02.cpp
```

`README.md` explains the topic and what to practice.  
`example/main.cpp` demonstrates the concept.  
`exercises/` contains practical tasks to solve and run.

## Study Routine

For each concept:

1. Read the concept README in full.
2. Run the example and change small parts to observe behavior.
3. Solve exercise 01 without looking up the answer.
4. Solve exercise 02 and refactor your first attempt.
5. Compare your approach with the example style and naming.

After finishing all concepts in `01-foundations`, continue with `02-core` in this order:

1. `input-validation`
2. `algorithms-basics`

Then continue with `03-advanced`:

1. `structs-and-classes`

Then continue with `04-expert`:

1. `memory-management-and-raii`

## Build Command

```bash
g++ -std=c++17 -Wall -Wextra -pedantic file.cpp -o output
```

All provided files are compatible with this command on Windows (MSYS2 MinGW) and Linux.
