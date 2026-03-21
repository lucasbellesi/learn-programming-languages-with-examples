# Contributing

Thank you for contributing to this repository.

## Guiding Principles

- Keep content beginner-friendly and technically correct.
- Prefer simple, readable examples over clever implementations.
- Use clear English for all text, comments, and instructions.
- Maintain cross-platform compatibility (Windows MSYS2 + Linux).

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

Run full repository checks with:

- `./scripts/verify-repo.ps1` (PowerShell)
- `bash ./scripts/verify-repo.sh` (Bash)

Run multi-language smoke checks with:

- `./scripts/smoke-languages.ps1` (PowerShell)
- `bash ./scripts/smoke-languages.sh` (Bash)

4. Update related README files when behavior or structure changes.
5. Open a pull request with a clear description of what changed and why.

## Content Expectations

- New concept modules should follow the existing folder layout.
- Every `01-foundations` concept README should include:
  - `## Quick Run`
  - `## Topics Covered`
  - `## Common Pitfalls`
  - `## Exercise Focus`
  - `### Exercise Specs`
  - `## Checkpoint`
- Every exercise file must contain complete, runnable content.
- Avoid external dependencies and test frameworks for C++ modules.
- Keep examples aligned with C++17.
- Keep documentation in English and keep path names consistent with folder names.
- Keep parity planning updated in `LANGUAGE_PARITY_MATRIX.md` when adding modules to non-C++ tracks.

## Commit Messages

Use short, descriptive commit messages that explain intent.

## Code of Conduct

By participating, you agree to follow `CODE_OF_CONDUCT.md`.
