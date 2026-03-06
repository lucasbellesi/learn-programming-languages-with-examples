# Learn Programming Languages With Examples

## Project Overview

This repository teaches programming through small, runnable examples and focused exercises.

- Primary implemented track: **C++ (C++17)**
- Expansion-ready for more languages (Python, Go, C#)
- Designed for a **VS Code-first** workflow on Windows and Linux

## Start Here (5 Minutes)

1. Open [C++ setup](languages/cpp/00-setup/README.md)
2. Open the [C++ roadmap](languages/cpp/README.md)
3. Run one example (for example, `types-and-io/example/main.cpp`)
4. Solve one exercise and mark progress in [C++ checklist](languages/cpp/CHECKLIST.md)

## Learning Philosophy

The project follows a practical, step-by-step approach:

- Learn one concept at a time.
- Run a minimal example.
- Solve short exercises immediately.
- Build level capstones and assessments to combine concepts.
- Track progress with checklists and review notes.

## Repository Structure

```text
learn-programming-languages-with-examples/
  .vscode/                  # VS Code tasks and recommendations
  scripts/                  # Build/run/link-check helpers (PowerShell + Bash)
  templates/                # Concept module template
  languages/
    cpp/                    # Main implemented learning track
    python/                 # Foundations started
    go/                     # Planned
    csharp/                 # Planned
  STUDY_PLAN.md             # 4-week C++ study path
```

## Learning Levels (C++)

C++ content lives in `languages/cpp` and is organized into measurable levels:

1. `01-foundations`
2. `02-core`
3. `03-advanced`
4. `04-expert`

Each concept module follows this structure:

```text
module-name/
  README.md
  example/main.cpp
  exercises/01.cpp
  exercises/02.cpp
```

## How To Navigate The Repository

1. Start with setup: [languages/cpp/00-setup/README.md](languages/cpp/00-setup/README.md)
2. Open the C++ roadmap: [languages/cpp/README.md](languages/cpp/README.md)
3. For each module:
   - read `README.md`
   - run `example/main.cpp`
   - solve `exercises/01.cpp` and `exercises/02.cpp`
   - expected pace: about 30-60 minutes per module, plus exercise time
4. Track completion:
   - [languages/cpp/CHECKLIST.md](languages/cpp/CHECKLIST.md)
   - `languages/cpp/<level>/PROGRESS.md` (for example: `languages/cpp/01-foundations/PROGRESS.md`)
5. Complete level practice:
   - capstones in `languages/cpp/projects/`
   - assessments in `languages/cpp/assessments/`
6. Use:
   - [STUDY_PLAN.md](STUDY_PLAN.md) for pacing
   - [languages/cpp/SOLUTION_RUBRIC.md](languages/cpp/SOLUTION_RUBRIC.md) for self-review quality

## How To Run Examples (C++17)

### Prerequisites

- `g++` installed and available in terminal
- VS Code installed (recommended)
- Terminal access (PowerShell, Bash, or WSL shell)

Required compile command:

```bash
g++ -std=c++17 -Wall -Wextra -pedantic path/to/file.cpp -o output_name
```

Example:

```bash
g++ -std=c++17 -Wall -Wextra -pedantic languages/cpp/01-foundations/types-and-io/example/main.cpp -o types_and_io_example
./types_and_io_example
```

On Windows (MSYS2/MinGW), run `types_and_io_example.exe`.

### Windows + WSL example

```bash
cd /path/to/learn-programming-languages-with-examples
g++ -std=c++17 -Wall -Wextra -pedantic languages/cpp/01-foundations/types-and-io/example/main.cpp -o types_and_io_example
./types_and_io_example
```

### Build helpers

Compile all C++ files:

```powershell
./scripts/build-all.ps1
```

```bash
bash ./scripts/build-all.sh
```

Run one module example quickly:

```powershell
./scripts/run-module.ps1 languages/cpp/01-foundations/strings
```

```bash
bash ./scripts/run-module.sh languages/cpp/01-foundations/strings
```

Run full repository checks (links + C++ build):

```powershell
./scripts/verify-repo.ps1
```

```bash
bash ./scripts/verify-repo.sh
```

### Common First Errors

- `g++: command not found`: install `g++` (MSYS2/MinGW on Windows or `g++` in WSL/Linux)
- `No such file or directory`: run commands from the repository root folder
- Program does not run on Windows: try `./program_name.exe` instead of `./program_name`

## Development Environment

Recommended environment:

- **Editor**: VS Code
- **C++ standard**: C++17
- **Compiler flags**: `-Wall -Wextra -pedantic`
- **Windows**: Windows 11 + MSYS2/MinGW `g++` (or WSL Ubuntu with `g++`)
- **Linux**: `g++` (GNU C++ compiler)

VS Code tasks are preconfigured in `.vscode/tasks.json` to build/run the active C++ file.

## How To Contribute

Contributions are welcome.

1. Read `CONTRIBUTING.md`
2. Follow `CODE_OF_CONDUCT.md`
3. Keep examples beginner-friendly and runnable
4. Preserve level structure and module pattern
5. Ensure C++ code compiles with:
   - `g++ -std=c++17 -Wall -Wextra -pedantic`

## Future Languages / Roadmap

- C++ is the active, most complete track.
- Python foundations are started under `languages/python/01-foundations`.
- Go and C# directories are present as planned tracks.
- Goal: keep concept structure consistent across languages for easier comparison.

## License

This project is licensed under the MIT License. See [LICENSE](./LICENSE).
