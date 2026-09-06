# Learn Programming Languages With Examples

## Project Overview

This repository teaches programming through small runnable examples and focused exercises.

- Six active language tracks: C++, C#, Go, Java, Python, and TypeScript.
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
- Java 21 JDK

If you only want to learn one track, follow that track README first because language-specific prerequisites differ.

## Start Here

### Your First Session

Install only the prerequisites for your chosen track. You do not need all six
toolchains to study one language. Open the track guide below, then its first
`types-and-io` module: each entry module includes a sample run, a small change to
predict, and visible exercise cases with expected output.

New to terminals or automated checks? Follow the [first-session walkthrough](STUDY_PLAN.md#first-session-walkthrough).
The examples are complete programs; the exercise files intentionally need your work.
An initial failed exercise check is expected.

### Learning Path

1. Choose your language guide:
   - [C++ Guide](languages/cpp/README.md)
   - [C# Guide](languages/csharp/README.md)
   - [Go Guide](languages/go/README.md)
   - [Java Guide](languages/java/README.md)
   - [Python Guide](languages/python/README.md)
   - [TypeScript Guide](languages/typescript/README.md)
2. Start at the first roadmap for that track:
   - C++: [00-setup](languages/cpp/00-setup/README.md), then `01-foundations`
   - Java: `01-foundations`, then `02-core`, `03-advanced`, and `04-expert`
   - C#, Go, Python, TypeScript: `01-foundations`, then `02-core`, `03-advanced`, and `04-expert`
3. Run one module example.
4. Choose the guided or comparative route described in [STUDY_PLAN.md](STUDY_PLAN.md).
5. Solve the selected starter files and check every named normal and edge case.
6. Mark progress using [LEARNING_LOG_TEMPLATE.md](LEARNING_LOG_TEMPLATE.md).

### Practical Course Workflow

Run every command from the repository root. First confirm the selected toolchain, then run a module and check a starter:

~~~bash
python scripts/automation.py doctor --language python
python scripts/automation.py run-module --module-path languages/python/01-foundations/types-and-io
python scripts/automation.py check-exercise --language python --level 01-foundations --module types-and-io --exercise 01
python scripts/automation.py hint-exercise --language python --level 01-foundations --module types-and-io --exercise 01 --stage 1
~~~

All 288 exercises separate compilable guided starters from reference solutions. Hints
progress from conceptual to structural to idiomatic API guidance without returning solved
code. Use `--submission <repo-relative-path>` to check another file. TypeScript submissions
must remain under `languages/typescript` so the track configuration can compile them.
Reference solutions live under each module's `exercises/solutions/` directory and can be
verified with `--solution` after a complete attempt.

Projects and assessments follow the same rule: work in `starter/`, keep `solutions/` closed until review, and check from the root:

~~~bash
python scripts/automation.py check-checkpoint --language python --kind project --level 01-foundations
python scripts/automation.py check-checkpoint --language python --kind assessment --level 01-foundations
~~~

PowerShell and Bash wrappers are also available as `./scripts/check-exercise.ps1` and `bash ./scripts/check-exercise.sh`; pass them the same arguments shown above after `check-exercise`.

### Contributor Path

1. Read [CONTRIBUTING.md](CONTRIBUTING.md).
2. Install the repo prerequisites listed above.
3. Run `./scripts/verify-repo.ps1` plus `./scripts/lint.ps1`, or the Bash equivalents, as the default pre-PR check.
4. Use a narrower script only when you want a faster loop on one part of the repo.

## Language Status

| Language | Current Levels | Coverage | Track Status |
| --- | --- | --- | --- |
| C++ | 00-setup, 01-foundations, 02-core, 03-advanced, 04-expert | Foundations, Core, Advanced, Expert, projects, assessments | Canonical reference track for curriculum order |
| C# | 01-foundations, 02-core, 03-advanced, 04-expert | 8/8 foundations modules, 6/6 core modules, 5/5 advanced modules, 5/5 expert modules, 4/4 projects, 4/4 assessments | Module and checkpoint parity complete through expert |
| Go | 01-foundations, 02-core, 03-advanced, 04-expert | 8/8 foundations modules, 6/6 core modules, 5/5 advanced modules, 5/5 expert modules, 4/4 projects, 4/4 assessments | Module and checkpoint parity complete through expert |
| Java | 01-foundations, 02-core, 03-advanced, 04-expert | 8/8 foundations modules, 6/6 core modules, 5/5 advanced modules, 5/5 expert modules, 4/4 projects, 4/4 assessments | Module and checkpoint parity complete through expert |
| Python | 01-foundations, 02-core, 03-advanced, 04-expert | 8/8 foundations modules, 6/6 core modules, 5/5 advanced modules, 5/5 expert modules, 4/4 projects, 4/4 assessments | Module and checkpoint parity complete through expert |
| TypeScript | 01-foundations, 02-core, 03-advanced, 04-expert | 8/8 foundations modules, 6/6 core modules, 5/5 advanced modules, 5/5 expert modules, 4/4 projects, 4/4 assessments | Module and checkpoint parity complete through expert |

Parity planning reference: [LANGUAGE_PARITY_MATRIX.md](LANGUAGE_PARITY_MATRIX.md)
Browse by concept: [CONCEPT_INDEX.md](CONCEPT_INDEX.md)

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

### Java

~~~bash
javac -d build/java languages/java/01-foundations/types-and-io/example/Main.java
java -cp build/java Main
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
    java/
    python/
    typescript/
~~~

## Documentation Contract

All concept module README files under `languages/<language>/<level>/<module>/README.md` follow one required structure:

1. `## Learning Metadata`
2. `## Learning Outcomes`
3. `## Quick Run`
4. `## Topics Covered`
5. `## Common Pitfalls`
6. `## Cross-Language Notes`
7. `## Exercise Focus`
8. `### Exercise Specs`
9. `## Check Your Work`
10. `## Checkpoint`

Reference: [Module README Style](languages/cpp/MODULE_README_STYLE.md)

A standardized `## Learning Metadata` block is required before `## Quick Run` for implemented modules and checkpoints. Implemented level READMEs should also include it before `## Module Order`. Use these fields:

- modules: difficulty, estimated time, prerequisites, cross-language comparison guidance
- checkpoints: difficulty, estimated time, prerequisites, learning focus
- level READMEs: difficulty, estimated time, prerequisites, study strategy

`## Cross-Language Notes` is required in modules. Keep it short, concrete, native to the
current language, and honest about where concepts do not map one-to-one.

Checkpoint artifacts under `languages/<language>/projects/*` and `languages/<language>/assessments/*` use this course structure:

- `README.md`
- incomplete learner files under `starter/`
- runnable reference implementation under `solutions/`
- the level's shared outcome IDs, with idiomatic scenarios and acceptance expectations for the language

## Example Commenting Standard

Hand-written example code files under `languages/*/*/*/example/` should use intent-first comments to help new developers read code quickly:

- Start each file with a short header comment that explains what the example teaches.
- Place comments before meaningful logic blocks, validation paths, and output/verification sections.
- Use comments to explain concepts, tradeoffs, and language-specific adaptations, not obvious syntax.
- Keep comments short, practical, and in English.
- Avoid empty scaffolding comments such as `Intent:` or line-by-line narration.

## Validation and CI

Use the full repository validation and lint checks before opening a PR:

~~~powershell
./scripts/verify-repo.ps1
./scripts/lint.ps1
~~~

~~~bash
bash ./scripts/verify-repo.sh
bash ./scripts/lint.sh
~~~

`verify-repo` validates curriculum structure, the blocking education-quality gate, example, exercise, and checkpoint output contracts, plus compiled-language builds. `lint` validates formatting and static checks for C++, Python, Go, C#, Java, and TypeScript.

Pull requests and `master` use Linux-only required CI. Windows compatibility runs in a separate workflow every Monday, on every tag, and on demand. Run the manual Windows workflow successfully before publishing a release tag.

Use narrower commands only when you want a faster loop on one area:

~~~powershell
./scripts/check-links.ps1
./scripts/check-readme-structure.ps1
./scripts/check-module-completeness.ps1
./scripts/check-checkpoint-completeness.ps1
./scripts/check-cross-language-parity.ps1
./scripts/check-exercise-parity.ps1
./scripts/check-example-output-contracts.ps1
./scripts/check-exercise-output-contracts.ps1
./scripts/test-automation.ps1
./scripts/audit-education-quality.ps1
./scripts/lint.ps1
./scripts/smoke-languages.ps1
./scripts/build-all.ps1
./scripts/clean-artifacts.ps1
./scripts/verify-repo.ps1
~~~

~~~bash
bash ./scripts/check-links.sh
bash ./scripts/check-readme-structure.sh
bash ./scripts/check-module-completeness.sh
bash ./scripts/check-checkpoint-completeness.sh
bash ./scripts/check-cross-language-parity.sh
bash ./scripts/check-exercise-parity.sh
bash ./scripts/check-example-output-contracts.sh
bash ./scripts/check-exercise-output-contracts.sh
bash ./scripts/test-automation.sh
bash ./scripts/audit-education-quality.sh
bash ./scripts/lint.sh
bash ./scripts/smoke-languages.sh
bash ./scripts/build-all.sh
bash ./scripts/clean-artifacts.sh
bash ./scripts/verify-repo.sh
~~~

GitHub Actions validates links, README structure, module completeness, checkpoint completeness, documentation sync, example/exercise/checkpoint contracts, compiled-language builds, multi-language smoke checks, and Linux lint checks for C++, Python, Go, C#, Java, and TypeScript.

The public PowerShell and Bash scripts remain supported entrypoints. The documented course interface is `python scripts/automation.py`, backed by `scripts/automation_manifest.json`, `scripts/curriculum_outcomes.json`, `scripts/learning_exercises.json`, and `scripts/learning_checkpoints.json`.

Use `clean-artifacts` when you want to remove generated build outputs, reports, temporary binaries, and exercise report files without removing dependencies such as `node_modules`.

The multi-language smoke scripts also compile standalone C# exercises by generating temporary validation projects during the check and compile TypeScript programs before executing their smoke targets, and compile Java single-file programs with Java 21.

Use [EDUCATIONAL_EXAMPLE_REVIEW_RUBRIC.md](EDUCATIONAL_EXAMPLE_REVIEW_RUBRIC.md) to keep entry examples pedagogically consistent during reviews. The education audit command writes markdown/json findings; `verify-repo` fails on blocking findings, while oversized-example findings remain advisory unless you opt into strict mode.
Use [ROADMAP.md](ROADMAP.md) for current priorities. The anti-pattern expansion is intentionally deferred until guided practice and checkpoint validation remain stable.

`verify-repo` now fails on blocking education-quality findings: low example-comment ratio, missing output explanation markers, or boilerplate comments. Oversized example findings remain advisory. When you want the stricter local cleanup mode that also fails on oversized examples, run:

~~~bash
python scripts/automation.py audit-education-quality --fail-on-findings
~~~

Documentation sync also validates that [CONCEPT_INDEX.md](CONCEPT_INDEX.md) covers every implemented module and checkpoint path listed in the automation manifest. Cross-language parity checks validate shared outcome IDs across tracks, while the example, exercise, and checkpoint contracts validate stable learner-visible behavior.

For a complete track-level check, including toolchain, examples, exercises, projects, and assessments, scope validation by language:

~~~bash
python scripts/automation.py verify-language --language java
~~~

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution workflow and documentation requirements.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE).
