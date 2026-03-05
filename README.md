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
  .vscode/                  # VS Code tasks and recommendations
  templates/                # Reusable concept layout for new modules
  languages/
    cpp/                    # Active C++ track (implemented)
    python/                 # Planned track
    go/                     # Planned track
    csharp/                 # Planned track
```

Main C++ content lives in `languages/cpp` and is split into numbered modules.

Current C++ foundations modules:

- `types-and-io`
- `control-flow`
- `functions`
- `arrays-and-vectors`

## Guided Learning Path

1. Complete setup: `languages/cpp/00-setup/README.md`
2. Open C++ roadmap: `languages/cpp/README.md`
3. Study one concept at a time:
   - read `README.md`
   - run `example/main.cpp`
   - solve `exercises/01.cpp` and `exercises/02.cpp`
4. Mark progress in `languages/cpp/CHECKLIST.md`
5. Repeat until all modules are complete

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

## VS Code Workflow (Zero Friction)

1. Open any `*.cpp` file.
2. Press `Ctrl+Shift+B` to build it with C++17 and strict warnings.
3. Run the task `Run active C++ file` from the command palette (`Tasks: Run Task`).
4. Use `Build and run active C++ file` for one-step iteration while studying exercises.

## Contribution Summary

Contributions are welcome. Please:

- Read `CONTRIBUTING.md` for workflow and coding expectations.
- Follow the `CODE_OF_CONDUCT.md`.
- Keep changes educational, clear, and cross-platform.
- Ensure C++ examples compile with `-Wall -Wextra -pedantic`.

## License

This repository is licensed under the MIT License. See `LICENSE`.
