# Contributing

Thank you for contributing to this repository.

## Guiding Principles

- Keep content beginner-friendly and technically correct.
- Prefer simple, readable examples over clever implementations.
- Use clear English for all text, comments, and instructions.
- Maintain cross-platform compatibility (Windows MSYS2 + Linux).
- Keep Node-based tooling simple and explicit when touching the TypeScript track.
- Keep Java modules on plain `javac`/`java` until the track intentionally adopts build tooling.

## Workflow

1. Fetch the latest `origin/master` and create a new branch from it for each new
   set of changes. Use the `codex/` prefix for agent-created branches. External
   contributors can fork first and branch from the latest upstream `master`.
   Do not make changes or commits directly on `master`.
2. Make focused updates (one topic per pull request when possible).
3. Run the full repository validation and lint checks first:

```powershell
./scripts/verify-repo.ps1
./scripts/lint.ps1
```

```bash
bash ./scripts/verify-repo.sh
bash ./scripts/lint.sh
```

For a faster loop while you are iterating, use a narrower command on the area you changed:

- Links: `./scripts/check-links.ps1` or `bash ./scripts/check-links.sh`
- Module README structure: `./scripts/check-readme-structure.ps1` or `bash ./scripts/check-readme-structure.sh`
- Module completeness: `./scripts/check-module-completeness.ps1` or `bash ./scripts/check-module-completeness.sh`
- Checkpoint completeness: `./scripts/check-checkpoint-completeness.ps1` or `bash ./scripts/check-checkpoint-completeness.sh`
- Cross-language parity: `./scripts/check-cross-language-parity.ps1` or `bash ./scripts/check-cross-language-parity.sh`
- Exercise parity: `./scripts/check-exercise-parity.ps1` or `bash ./scripts/check-exercise-parity.sh`
- Example output contracts: `./scripts/check-example-output-contracts.ps1` or `bash ./scripts/check-example-output-contracts.sh`
- Exercise output contracts: `./scripts/check-exercise-output-contracts.ps1` or `bash ./scripts/check-exercise-output-contracts.sh`
- Education audit: `./scripts/audit-education-quality.ps1` or `bash ./scripts/audit-education-quality.sh`
- Lint: `./scripts/lint.ps1` or `bash ./scripts/lint.sh`
- Smoke checks: `./scripts/smoke-languages.ps1` or `bash ./scripts/smoke-languages.sh`
- Compiled-language builds: `./scripts/build-all.ps1` or `bash ./scripts/build-all.sh`
- Generated artifact cleanup: `./scripts/clean-artifacts.ps1` or `bash ./scripts/clean-artifacts.sh`

If you are changing one C++ file and want a local spot check before the full pass, you can still compile it directly with:

```bash
g++ -std=c++17 -Wall -Wextra -pedantic <file>.cpp -o <output>
```

For large changes, you can run one language at a time before the full check:

- `python scripts/automation.py verify-language --language <cpp|csharp|go|java|python|typescript>`

`verify-language` checks the selected toolchain, compiles the track where required, and runs its example, exercise, project, and assessment contracts. C# validation generates temporary projects for standalone exercises. TypeScript restores dependencies from `package-lock.json` and runs emitted JavaScript with `node`; Java compiles package-free single-file programs with Java 21.

The public PowerShell and Bash scripts are thin wrappers over the shared Python automation core in `scripts/automation.py`. Repository structure and smoke targets live in `scripts/automation_manifest.json`; shared outcomes, exercise contracts, and checkpoint contracts live in `scripts/curriculum_outcomes.json`, `scripts/learning_exercises.json`, and `scripts/learning_checkpoints.json`.
The artifact cleanup command removes generated build outputs, reports, temporary binaries, and exercise report files while keeping restored dependencies such as `node_modules`.

Required pull-request and `master` checks run on Linux. Windows compatibility is verified by the separate `Windows Compatibility` workflow every Monday, for every pushed tag, and through `workflow_dispatch`. Before publishing a release tag, run that workflow manually against the commit you intend to tag and confirm that all six language jobs pass.

Use [EDUCATIONAL_EXAMPLE_REVIEW_RUBRIC.md](EDUCATIONAL_EXAMPLE_REVIEW_RUBRIC.md) when reviewing `example/main.*` files for teaching clarity and parity.
`verify-repo` fails on blocking education-quality findings: low example-comment ratio, missing output explanation markers, or boilerplate comments. Oversized example findings remain advisory. During focused cleanup work, run `python scripts/automation.py audit-education-quality --fail-on-findings` to make every learner-quality finding fail locally.

4. Update related README files when behavior or structure changes.
5. Commit and push your working branch, then open a pull request targeting `master`
   with a clear description of what changed and why. Keep follow-up revisions on
   that branch. Agents must not merge the pull request without an explicit user request.

## Content Expectations

- New concept modules should follow the existing folder layout.
- Every concept README in implemented levels should include:
  - required `## Learning Metadata` before `## Quick Run` with `Difficulty`, `Estimated Time`, `Prerequisites`, and `Cross-Language Lens`
  - `## Learning Outcomes` with IDs from `scripts/curriculum_outcomes.json`
  - required `## Cross-Language Notes` after `## Common Pitfalls` and before `## Exercise Focus`; notes must describe the current language rather than copy another track
  - `## Quick Run`
  - `## Topics Covered`
  - `## Common Pitfalls`
  - `## Exercise Focus`
  - `### Exercise Specs`
  - `## Check Your Work`
  - `## Checkpoint`
- Every project or assessment checkpoint should include:
  - `README.md`
  - incomplete learner files under `starter/`
  - a runnable reference implementation under `solutions/`
  - the language entrypoint in both trees (`main.cpp`, `main.cs` + `.csproj`, `main.go`, `Main.java`, `main.py`, or `main.ts`)
  - shared outcome IDs and named normal/edge cases registered in `scripts/learning_checkpoints.json`
  - the same learning outcomes as the corresponding checkpoint in other tracks, with idiomatic scenarios where appropriate
  - required `## Learning Metadata` before `## Quick Run` with `Difficulty`, `Estimated Time`, `Prerequisites`, and `Learning Focus`
  - recommended `## Cross-Language Notes` before `## What To Check`
- Every implemented level README should include required `## Learning Metadata` before `## Module Order` with `Difficulty`, `Estimated Time`, `Prerequisites`, and `Study Strategy`.
- Checkpoint README structure should mirror the matching C++ checkpoint style, not the module README contract.
- Every hand-written code file under `example/` should include intent-first comments:
  - a short file header comment that explains what the example teaches
  - comments before program flow, validation, core transformation, branching, or output blocks when those blocks are non-trivial
  - language-specific notes when the example is an adaptation rather than a direct translation of the C++ concept
  - no empty scaffolding comments such as `Intent:` and no line-by-line narration of obvious syntax
- Exercise starters must compile, contain at least three behavior-specific TODOs, and remain incomplete; generic “implement the README” prompts are rejected and full implementations belong in `exercises/solutions/`.
- Guided-practice modules keep compilable starters at the documented exercise paths and complete reference implementations under `exercises/solutions/`.
- Add starter, solution, outcome IDs, `route_role`, `starter_mode`, and named normal/edge cases to `scripts/learning_exercises.json`; it is the canonical exercise contract.
- Projects use guided starters and assessments use independent starters. Checkpoint contracts require named normal, boundary/error, and state/resource cases.
- Add or update automation unit tests under `scripts/tests/` when changing the guided exercise runner or configuration contract.
- Avoid external dependencies and test frameworks for C++ modules.
- Avoid external dependencies and test frameworks for non-C++ checkpoints.
- Keep the TypeScript track on plain Node console programs; do not introduce browser, DOM, or framework dependencies.
- Keep the Java track on package-free single-file programs; do not introduce Maven, Gradle, or `src/main/java` until the curriculum intentionally adds build tooling.
- Keep examples aligned with C++17.
- For beginner modules, include a sample run, an explanation of the result, and one
  small modification for the learner to predict. State whether input is interactive
  or fixed and which invalid inputs the example does not yet handle.
- Show exercise input/output cases without revealing the solution. Copy expectations
  from the canonical contract and distinguish full-output comparisons from fragments.
- Review the actual inputs of named edge cases: a malformed-field test must contain
  missing or extra fields, and an invalid-price test must reach numeric validation.
  A matching case name alone is not evidence that the behavior was tested.
- Keep documentation in English and keep path names consistent with folder names.
- Keep parity planning updated in `LANGUAGE_PARITY_MATRIX.md` when adding modules or checkpoints to non-C++ tracks.
- Keep root and language README status sections aligned with project and assessment coverage when those directories change.
- Keep [CONCEPT_INDEX.md](CONCEPT_INDEX.md) aligned with any new or renamed module/checkpoint paths.

## Commit Messages

Use short, descriptive commit messages that explain intent.

## Code of Conduct

By participating, you agree to follow `CODE_OF_CONDUCT.md`.
