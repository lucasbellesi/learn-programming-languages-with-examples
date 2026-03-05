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
3. [types-and-io](./01-foundations/types-and-io/README.md)
4. [control-flow](./01-foundations/control-flow/README.md)
5. [functions](./01-foundations/functions/README.md)
6. [arrays-and-vectors](./01-foundations/arrays-and-vectors/README.md)

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

## Build Command

```bash
g++ -std=c++17 -Wall -Wextra -pedantic file.cpp -o output
```

All provided files are compatible with this command on Windows (MSYS2 MinGW) and Linux.
