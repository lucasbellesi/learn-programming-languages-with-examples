# Learn Programming Languages With Examples

## Project Overview

This repository teaches programming through small runnable examples and focused exercises.

- Four active language tracks: C++, C#, Go, and Python.
- Shared concept naming across tracks for easier comparison.
- VS Code-first workflow, with scripts for Windows PowerShell and Bash.

## Start Here

1. Choose your language guide:
   - [C++ Guide](languages/cpp/README.md)
   - [C# Guide](languages/csharp/README.md)
   - [Go Guide](languages/go/README.md)
   - [Python Guide](languages/python/README.md)
2. Open the `01-foundations` roadmap for your selected language.
3. Run one module example.
4. Solve `exercises/01` and `exercises/02` in that module.
5. Mark progress in the language checklist.

## Language Status

| Language | Current Levels | Module Coverage | Track Status |
| --- | --- | --- | --- |
| C++ | 00-setup, 01-foundations, 02-core, 03-advanced, 04-expert | Foundations, Core, Advanced, Expert, projects, assessments | Most complete and primary track |
| C# | 01-foundations | 8/8 foundations modules | Foundations implemented, expanding next levels |
| Go | 01-foundations | 8/8 foundations modules | Foundations implemented, expanding next levels |
| Python | 01-foundations | 8/8 foundations modules | Foundations implemented, expanding next levels |

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
~~~

## Documentation Contract

All `01-foundations/<module>/README.md` files follow one required structure:

1. `## Quick Run`
2. `## Topics Covered`
3. `## Common Pitfalls`
4. `## Exercise Focus`
5. `### Exercise Specs`
6. `## Checkpoint`

Reference: [Module README Style](languages/cpp/MODULE_README_STYLE.md)

## Validation and CI

Run checks locally:

~~~powershell
./scripts/check-links.ps1
./scripts/check-readme-structure.ps1
./scripts/build-all.ps1
./scripts/verify-repo.ps1
~~~

~~~bash
bash ./scripts/check-links.sh
bash ./scripts/check-readme-structure.sh
bash ./scripts/build-all.sh
bash ./scripts/verify-repo.sh
~~~

GitHub Actions validates links, README structure, and C++ build on Linux and Windows.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution workflow and documentation requirements.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE).