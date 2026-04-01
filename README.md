# Learn Programming Languages With Examples

## Project Overview

This repository teaches programming through small runnable examples and focused exercises.

- Five active language tracks: C++, C#, Go, Python, and TypeScript.
- Shared concept naming across tracks for easier comparison.
- Each module follows the same shape: `README.md`, `example/main.*`, and two exercises.
- Each implemented level ends with a project and an assessment checkpoint.
- VS Code-first workflow, with scripts for Windows PowerShell and Bash.

## Repo Prerequisites

For the full local pipeline, install:

- Python 3
- a C++17-capable `g++`
- Go
- .NET 8 SDK
- Node LTS with `npm`

If you only want to learn one track, follow that track README first because language-specific prerequisites differ.

## Start Here

### Learning Path

1. Choose your language guide:
   - [C++ Guide](languages/cpp/README.md)
   - [C# Guide](languages/csharp/README.md)
   - [Go Guide](languages/go/README.md)
   - [Python Guide](languages/python/README.md)
   - [TypeScript Guide](languages/typescript/README.md)
2. Start at the first roadmap for that track:
   - C++: [00-setup](languages/cpp/00-setup/README.md), then `01-foundations`
   - C#, Go, Python, TypeScript: `01-foundations`
3. Run one module example.
4. Solve `exercises/01` and `exercises/02` in that module.
5. Mark progress in the language checklist.

### Contributor Path

1. Read [CONTRIBUTING.md](CONTRIBUTING.md).
2. Install the repo prerequisites listed above.
3. Run `./scripts/verify-repo.ps1` or `bash ./scripts/verify-repo.sh`.
4. Run `./scripts/lint.ps1` or `bash ./scripts/lint.sh` before opening a pull request.

## Language Status

| Language | Current Levels | Coverage | Track Status |
| --- | --- | --- | --- |
| C++ | 00-setup, 01-foundations, 02-core, 03-advanced, 04-expert | Foundations, Core, Advanced, Expert, projects, assessments | Most complete and primary track |
| C# | 01-foundations, 02-core, 03-advanced, 04-expert | 8/8 foundations modules, 6/6 core modules, 5/5 advanced modules, 5/5 expert modules, 4/4 projects, 4/4 assessments | Module and checkpoint parity complete through expert |
| Go | 01-foundations, 02-core, 03-advanced, 04-expert | 8/8 foundations modules, 6/6 core modules, 5/5 advanced modules, 5/5 expert modules, 4/4 projects, 4/4 assessments | Module and checkpoint parity complete through expert |
| Python | 01-foundations, 02-core, 03-advanced, 04-expert | 8/8 foundations modules, 6/6 core modules, 5/5 advanced modules, 5/5 expert modules, 4/4 projects, 4/4 assessments | Module and checkpoint parity complete through expert |
| TypeScript | 01-foundations, 02-core, 03-advanced | 8/8 foundations modules, 6/6 core modules, 5/5 advanced modules, 3/4 projects, 3/4 assessments | Foundations, core, and advanced complete; expert planned |

Parity planning reference: [LANGUAGE_PARITY_MATRIX.md](LANGUAGE_PARITY_MATRIX.md)

## Run One Example Per Language

### C++

~~~bash
g++ -std=c++17 -Wall -Wextra -pedantic languages/cpp/01-foundations/types-and-io/example/main.cpp -o types_and_io_cpp
./types_and_io_cpp
~~~

### C#

~~~bash
dotnet run --project languages/csharp/01-foundations/types-and-io/example/types-and-io-example.csproj
~~~

### Go

~~~bash
go run languages/go/01-foundations/types-and-io/example/main.go
~~~

### Python

~~~bash
python languages/python/01-foundations/types-and-io/example/main.py
~~~

### TypeScript

~~~bash
npm run build:typescript
node build/typescript/01-foundations/types-and-io/example/main.js
~~~

## Repository Structure

~~~text
learn-programming-languages-with-examples/
  .github/workflows/        # CI checks
  .vscode/                  # VS Code tasks and recommendations
  scripts/                  # Build, run, and documentation checks
  templates/                # Concept module templates
  languages/
    cpp/
    csharp/
    go/
    python/
    typescript/
~~~

## Documentation Contract

All concept module README files under `languages/<language>/<level>/<module>/README.md` follow one required structure:

1. `## Quick Run`
2. `## Topics Covered`
3. `## Common Pitfalls`
4. `## Exercise Focus`
5. `### Exercise Specs`
6. `## Checkpoint`

Reference: [Module README Style](languages/cpp/MODULE_README_STYLE.md)

A standardized `## Learning Metadata` block is required before `## Quick Run` for implemented modules and checkpoints. Implemented level READMEs should also include it before `## Module Order`. Use these fields:

- modules: difficulty, estimated time, prerequisites, cross-language comparison guidance
- checkpoints: difficulty, estimated time, prerequisites, learning focus
- level READMEs: difficulty, estimated time, prerequisites, study strategy

Checkpoint artifacts under `languages/<language>/projects/*` and `languages/<language>/assessments/*` should mirror the corresponding C++ checkpoint style:

- `README.md`
- runnable entrypoint (`main.cpp` in C++, `main.cs` + `.csproj` in C#, `main.go` in Go, `main.py` in Python, or `main.ts` in TypeScript)
- same learner goal, input/output shape, and acceptance expectations as the C++ version

## Example Commenting Standard

Example files (`example/main.*`) should use intent-first comments to help new developers read code quickly:

- Explain purpose, intent, and edge-case handling.
- Place comments before meaningful logic blocks (not every single line).
- Keep comments short, practical, and in English.

## Validation and CI

Run checks locally:

~~~powershell
./scripts/check-links.ps1
./scripts/check-readme-structure.ps1
./scripts/check-module-completeness.ps1
./scripts/check-checkpoint-completeness.ps1
./scripts/lint.ps1
./scripts/smoke-languages.ps1
./scripts/build-all.ps1
./scripts/verify-repo.ps1
~~~

~~~bash
bash ./scripts/check-links.sh
bash ./scripts/check-readme-structure.sh
bash ./scripts/check-module-completeness.sh
bash ./scripts/check-checkpoint-completeness.sh
bash ./scripts/lint.sh
bash ./scripts/smoke-languages.sh
bash ./scripts/build-all.sh
bash ./scripts/verify-repo.sh
~~~

GitHub Actions validates links, README structure, module completeness, checkpoint completeness, documentation sync, compiled-language builds, multi-language smoke checks, and Linux lint checks for C++, Python, Go, C#, and TypeScript.

The public PowerShell and Bash scripts remain the supported entrypoints, but they now delegate to a shared Python automation core under `scripts/automation.py` backed by `scripts/automation_manifest.json`.

The multi-language smoke scripts also compile standalone C# exercises by generating temporary validation projects during the check and compile TypeScript foundations programs before executing their smoke targets.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution workflow and documentation requirements.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE).
