# Module README Style (All Languages)

Use this structure for every concept module under:

- `languages/cpp/01-foundations`, `02-core`, `03-advanced`, `04-expert`
- `languages/csharp/01-foundations` and newer implemented levels
- `languages/go/01-foundations` and newer implemented levels
- `languages/java/01-foundations` and newer implemented levels
- `languages/python/01-foundations` and newer implemented levels
- `languages/typescript/01-foundations` and newer implemented levels

This structure is required for all implemented concept modules.

## Required Sections

1. `## Learning Metadata`
2. `## Learning Outcomes`
3. `## Quick Run`
4. `## Topics Covered`
5. `## Common Pitfalls`
6. `## Exercise Focus`
7. `### Exercise Specs`
8. `## Check Your Work`
9. `## Checkpoint`

## Section Rules

- `Learning Metadata` (required): include `Difficulty`, `Estimated Time`, `Prerequisites`, and `Cross-Language Lens` before `Quick Run`.
- `Learning Outcomes`: list the shared outcome IDs assigned to the module in `scripts/curriculum_outcomes.json`.
- `Quick Run`: use `python scripts/automation.py run-module --module-path ...` from the repository root.
- `Topics Covered`: concise bullets of concepts practiced in the module.
- `Common Pitfalls`: practical mistakes beginners frequently make.
- `Cross-Language Notes` (recommended): place after `Common Pitfalls` and before `Exercise Focus`; keep it to 3-5 concrete bullets.
- `Exercise Focus`: one bullet per exercise with a clear task summary.
- `Exercise Specs`: for each exercise define input, output, and at least two edge cases.
- `Check Your Work`: show the exact root-level `check-exercise` command and defer the reference solution until after a complete attempt.
- `Checkpoint`: 3-5 measurable outcomes as checkboxes.

## Writing Guidelines

- Keep explanations practical and short.
- Align language with beginner readability.
- Keep content in English.
- Use folder names exactly as they appear in paths.
- Hand-written files under `example/` should use medium-density, intent-first comments: one short header comment plus comments before meaningful logic or validation blocks.
- Comments should explain concepts, tradeoffs, or observable behavior, not narrate syntax line by line.
