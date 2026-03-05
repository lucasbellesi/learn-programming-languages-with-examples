# learn-programming-languages-with-examples

An educational repository for learning programming languages through focused concepts, runnable examples, and hands-on exercises.

The first fully implemented track is **C++ (C++17)**, designed for beginners while following solid coding practices.

## Project Goals

- Learn core programming concepts progressively.
- Compare how the same ideas appear across languages.
- Practice with small exercises after each concept.
- Keep everything easy to run in VS Code on Windows and Linux.

## Repository Structure

```text
learn-programming-languages-with-examples/
  templates/                # Reusable concept layout
  languages/
    cpp/                    # Fully implemented C++ track
    python/                 # Planned track
    go/                     # Planned track
    csharp/                 # Planned track
```

Main C++ content lives in `languages/cpp` and is split into numbered modules.

## How To Use This Repository

1. Start with `languages/cpp/00-setup/README.md`.
2. Follow modules in numeric order.
3. Read each concept README first.
4. Run the `example/main.cpp` file.
5. Solve exercises in the same folder.
6. Track progress in `languages/cpp/CHECKLIST.md`.

## Compile And Run (C++17)

All C++ code is standard C++17 and should compile cleanly with:

```bash
g++ -std=c++17 -Wall -Wextra -pedantic path/to/file.cpp -o path/to/output
```

### Linux example

```bash
g++ -std=c++17 -Wall -Wextra -pedantic languages/cpp/01-foundations/types-and-io/example/main.cpp -o types_and_io_example
./types_and_io_example
```

### Windows (MSYS2 MinGW) example

```bash
g++ -std=c++17 -Wall -Wextra -pedantic languages/cpp/01-foundations/types-and-io/example/main.cpp -o types_and_io_example
./types_and_io_example.exe
```

VS Code users can also run the included build task in `.vscode/tasks.json` to compile the currently open C++ file.

## Contribution Summary

Contributions are welcome. Please:

- Read `CONTRIBUTING.md` for workflow and coding expectations.
- Follow the `CODE_OF_CONDUCT.md`.
- Keep changes educational, clear, and cross-platform.
- Ensure C++ examples compile with `-Wall -Wextra -pedantic`.

## License

This repository is licensed under the MIT License. See `LICENSE`.
