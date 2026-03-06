# learn-programming-languages-with-examples

An educational repository for learning programming languages through focused concepts, runnable examples, and hands-on exercises.

The first fully implemented track is **C++ (C++17)**.  
Content is designed for VS Code-first workflows and cross-platform execution (Windows MSYS2/MinGW + Linux g++).

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
  scripts/                  # Build validation scripts (PowerShell + Bash)
  languages/
    cpp/                    # Active C++ track (implemented)
    python/                 # Python parity track (foundations started)
    go/                     # Planned track
    csharp/                 # Planned track
  STUDY_PLAN.md             # 4-week guided learning plan
```

Main C++ content lives in `languages/cpp` and is split into measurable levels:

- `01-foundations`
- `02-core`
- `03-advanced`
- `04-expert`

Python parity starter modules live in `languages/python/01-foundations`:

- [`types-and-io`](languages/python/01-foundations/types-and-io/README.md)
- [`control-flow`](languages/python/01-foundations/control-flow/README.md)
- [`functions`](languages/python/01-foundations/functions/README.md)

## Guided Learning Path

1. Complete setup: `languages/cpp/00-setup/README.md`
2. Open C++ roadmap: `languages/cpp/README.md`
3. Study one concept at a time:
   - read `README.md`
   - run `example/main.cpp`
   - solve `exercises/01.cpp` and `exercises/02.cpp`
   - use level `HINTS.md` only when blocked
   - follow the level order from foundations to expert
4. Mark progress in `languages/cpp/CHECKLIST.md`
5. Build capstones in `languages/cpp/projects/`
6. Complete level assessments in `languages/cpp/assessments/`
7. Follow weekly pacing in `STUDY_PLAN.md`
8. Use per-level `PROGRESS.md` + `languages/cpp/SOLUTION_RUBRIC.md` for self-review

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

## Build Validation Scripts

You can compile all C++ examples and exercises with:

PowerShell:

```powershell
./scripts/build-all.ps1
```

Bash:

```bash
bash ./scripts/build-all.sh
```

Run a single module example quickly:

PowerShell:

```powershell
./scripts/run-module.ps1 languages/cpp/01-foundations/strings
```

Bash:

```bash
bash ./scripts/run-module.sh languages/cpp/01-foundations/strings
```

`build-all` compiles each `*.cpp` file under `languages/cpp` with:

```bash
g++ -std=c++17 -Wall -Wextra -pedantic
```

CI also validates this on Linux and Windows in `.github/workflows/cpp-build.yml`.

You can validate markdown links with:

PowerShell:

```powershell
./scripts/check-links.ps1
```

Bash:

```bash
bash ./scripts/check-links.sh
```

## Contribution Summary

Contributions are welcome. Please:

- Read `CONTRIBUTING.md` for workflow and coding expectations.
- Follow the `CODE_OF_CONDUCT.md`.
- Keep changes educational, clear, and cross-platform.
- Ensure C++ examples compile with `-Wall -Wextra -pedantic`.

## License

This repository is licensed under the MIT License. See `LICENSE`.
