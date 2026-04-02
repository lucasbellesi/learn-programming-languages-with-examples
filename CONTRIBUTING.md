# Contributing

Thank you for contributing to this repository.

## Guiding Principles

- Keep content beginner-friendly and technically correct.
- Prefer simple, readable examples over clever implementations.
- Use clear English for all text, comments, and instructions.
- Maintain cross-platform compatibility (Windows MSYS2 + Linux).
- Keep Node-based tooling simple and explicit when touching the TypeScript track.

## Workflow

1. Fork the repository and create a branch for your change.
2. Make focused updates (one topic per pull request when possible).
3. Verify C++ code compiles with:

```bash
g++ -std=c++17 -Wall -Wextra -pedantic <file>.cpp -o <output>
```

You can also validate all C++ files with:

- `./scripts/build-all.ps1` (PowerShell)
- `bash ./scripts/build-all.sh` (Bash)

Validate markdown links with:

- `./scripts/check-links.ps1` (PowerShell)
- `bash ./scripts/check-links.sh` (Bash)

Validate README structure with:

- `./scripts/check-readme-structure.ps1` (PowerShell)
- `bash ./scripts/check-readme-structure.sh` (Bash)

Validate module completeness with:

- `./scripts/check-module-completeness.ps1` (PowerShell)
- `bash ./scripts/check-module-completeness.sh` (Bash)

Validate checkpoint completeness with:

- `./scripts/check-checkpoint-completeness.ps1` (PowerShell)
- `bash ./scripts/check-checkpoint-completeness.sh` (Bash)

Run full repository checks with:

- `./scripts/verify-repo.ps1` (PowerShell)
- `bash ./scripts/verify-repo.sh` (Bash)

Run multi-language smoke checks with:

- `./scripts/smoke-languages.ps1` (PowerShell)
- `bash ./scripts/smoke-languages.sh` (Bash)

Run language lint checks with:

- `./scripts/lint.ps1` (PowerShell)
- `bash ./scripts/lint.sh` (Bash)

These smoke checks also compile standalone C# exercises by generating temporary validation projects during the check.
TypeScript checks restore Node dependencies from `package-lock.json`, compile with `tsc`, and execute the emitted JavaScript with `node`.

The public PowerShell and Bash scripts are thin wrappers over the shared Python automation core in `scripts/automation.py`. Curriculum validation and smoke target metadata live in `scripts/automation_manifest.json`.

4. Update related README files when behavior or structure changes.
5. Open a pull request with a clear description of what changed and why.

## Content Expectations

- New concept modules should follow the existing folder layout.
- Every concept README in implemented levels should include:
  - required `## Learning Metadata` before `## Quick Run` with `Difficulty`, `Estimated Time`, `Prerequisites`, and `Cross-Language Lens`
  - recommended `## Cross-Language Notes` after `## Common Pitfalls` and before `## Exercise Focus`
  - `## Quick Run`
  - `## Topics Covered`
  - `## Common Pitfalls`
  - `## Exercise Focus`
  - `### Exercise Specs`
  - `## Checkpoint`
- Every project or assessment checkpoint should include:
  - `README.md`
  - runnable entrypoint (`main.cs` + `.csproj`, `main.go`, `main.py`, or `main.ts`)
  - the same learner goal, input/output shape, and acceptance expectations as the corresponding C++ checkpoint
  - required `## Learning Metadata` before `## Quick Run` with `Difficulty`, `Estimated Time`, `Prerequisites`, and `Learning Focus`
  - recommended `## Cross-Language Notes` before `## What To Check`
- Every implemented level README should include required `## Learning Metadata` before `## Module Order` with `Difficulty`, `Estimated Time`, `Prerequisites`, and `Study Strategy`.
- Checkpoint README structure should mirror the matching C++ checkpoint style, not the module README contract.
- Every hand-written code file under `example/` should include intent-first comments:
  - a short file header comment that explains what the example teaches
  - comments before program flow, validation, core transformation, branching, or output blocks when those blocks are non-trivial
  - language-specific notes when the example is an adaptation rather than a direct translation of the C++ concept
  - no empty scaffolding comments such as `Intent:` and no line-by-line narration of obvious syntax
- Every exercise file must contain complete, runnable content.
- Avoid external dependencies and test frameworks for C++ modules.
- Avoid external dependencies and test frameworks for non-C++ checkpoints.
- Keep the TypeScript track on plain Node console programs; do not introduce browser, DOM, or framework dependencies.
- Keep examples aligned with C++17.
- Keep documentation in English and keep path names consistent with folder names.
- Keep parity planning updated in `LANGUAGE_PARITY_MATRIX.md` when adding modules or checkpoints to non-C++ tracks.
- Keep root and language README status sections aligned with project and assessment coverage when those directories change.
- Keep [CONCEPT_INDEX.md](CONCEPT_INDEX.md) aligned with any new or renamed module/checkpoint paths.

## Commit Messages

Use short, descriptive commit messages that explain intent.

## Code of Conduct

By participating, you agree to follow `CODE_OF_CONDUCT.md`.
