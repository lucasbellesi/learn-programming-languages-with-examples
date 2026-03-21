# C++ Track

## Scope and Status

This is the primary and most complete track in the repository.

- Covers setup, foundations, core, advanced, and expert levels.
- Includes level capstone projects and assessments.
- Targets C++17 with `g++`.

## Prerequisites

- `g++` with C++17 support
- Terminal (PowerShell or Bash)
- VS Code recommended

## Quick Start

1. Read [00-setup](./00-setup/README.md).
2. Open [01-foundations](./01-foundations/README.md).
3. Run one module example:

~~~bash
g++ -std=c++17 -Wall -Wextra -pedantic 01-foundations/types-and-io/example/main.cpp -o types_and_io_example
./types_and_io_example
~~~

## Level and Module Map

- [00-setup](./00-setup/README.md)
- [01-foundations](./01-foundations/README.md)
- [02-core](./02-core/README.md)
- [03-advanced](./03-advanced/README.md)
- [04-expert](./04-expert/README.md)
- [projects](./projects/README.md)
- [assessments](./assessments/README.md)

## Progress Tracking

- [CHECKLIST.md](./CHECKLIST.md)
- [01-foundations/PROGRESS.md](./01-foundations/PROGRESS.md)
- [02-core/PROGRESS.md](./02-core/PROGRESS.md)
- [03-advanced/PROGRESS.md](./03-advanced/PROGRESS.md)
- [04-expert/PROGRESS.md](./04-expert/PROGRESS.md)

## Cross-Language Parity Strategy

Use C++ as the reference implementation track:

- Solve the same module in C++, then in Python, Go, or C#.
- Compare syntax, type systems, and standard library patterns.
- Keep concept folder names aligned across languages.

## Documentation Standards

- [MODULE_README_STYLE.md](./MODULE_README_STYLE.md)
- [SOLUTION_RUBRIC.md](./SOLUTION_RUBRIC.md)