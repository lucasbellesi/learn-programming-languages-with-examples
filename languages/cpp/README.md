# C++ Learning Track (C++17)

This track teaches core programming concepts in C++ using:

- A concept README for theory and pitfalls
- A runnable `example/main.cpp`
- Two practice exercises

## Roadmap

1. [00-setup](./00-setup/README.md)
2. 01-foundations
3. [types-and-io](./01-foundations/types-and-io/README.md)
4. [control-flow](./01-foundations/control-flow/README.md)
5. [functions](./01-foundations/functions/README.md)

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

## Build Command

```bash
g++ -std=c++17 -Wall -Wextra -pedantic file.cpp -o output
```

All provided files are compatible with this command on Windows (MSYS2 MinGW) and Linux.
