# Educational Repository Roadmap

This is the current source of truth for repository improvement work. Prior reviews remain useful as historical context but do not define current status.

## Course Model

- Self-directed practical course, not a reference-only example collection.
- Shared learning outcomes across six languages with explicit idiomatic adaptations.
- Complete examples, incomplete starters, separate reference solutions.
- Projects include milestones and extensions; assessments emphasize criteria and case feedback.

## Delivered Baseline

- 24 modules and eight checkpoints in each language track.
- 144 module examples with executable contracts.
- 288 exercises represented in `scripts/learning_exercises.json` with starter, solution, outcomes, and named cases.
- 48 checkpoints represented in `scripts/learning_checkpoints.json` with starter, solution, outcomes, and runtime cases.
- Root-level `doctor`, `run-module`, `check-exercise`, `check-checkpoint`, and `verify-language` commands.
- Guided and comparative routes, staged hints, a shared rubric, and a learning log.
- Zero solution-oracle cases: deterministic behavior is recorded as explicit assertions.
- Three named contract facets for every checkpoint, with normal, boundary/error, and state/resource coverage.
- First-session guidance and worked input/output observations in all six `types-and-io`
  modules, with visible exercise cases and a predict-modify practice step.
- Corrected entry invoice cases for missing/extra fields in C#, Go, and Python and
  invalid numeric prices in TypeScript, with regression checks on case inputs.

## Current Quality Priorities

1. Replace shared-execution checkpoint facets with distinct parameterized executions, starting with Advanced and Expert assessments.
2. Add mutation checks that prove checkpoint contracts reject hardcoded normal-path output.
3. Keep every documented edge case tied to a named automated case when specifications change.
4. Continue extracting focused automation modules while preserving the public CLI contract.
5. Keep local verification below seven minutes and CI below ten by compiling each target once per job.
6. Review educational size waivers when their explicit trigger conditions are reached.
7. Extend the entry modules' sample runs and visible practice cases to later modules.
   Explain prompts and exact formatting wherever output contracts require them.
8. Audit edge-case inputs against their names, not only their coverage labels.
   The entry invoice review found valid input labeled as malformed input; automated
   structure checks alone did not catch this mismatch.

## Deferred Work

The 120 anti-pattern/corrected-example expansion is deferred. Adding more examples before maintaining guided-practice quality would increase review and navigation cost without improving the main learner workflow.

Reconsider that expansion only after:

- all oracle-backed cases have stable assertions where deterministic output permits it;
- CI remains below the feedback target for four consecutive weeks;
- learner feedback identifies specific misconceptions not addressed by current examples and exercises.

## Change Policy

Every curriculum change should update the canonical JSON contract first, then code and README content. Cross-language parity means equal outcomes and comparable evidence, not literal translations.
