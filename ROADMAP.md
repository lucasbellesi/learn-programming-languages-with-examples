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
- Standard eight-week plan and accelerated four-week variant.

## Current Quality Priorities

1. Promote deterministic dynamic-oracle cases to stable positive, negative, regex, or generated-file assertions when that makes feedback more specific.
2. Keep every documented edge case tied to a named automated case when specifications change.
3. Split automation internals only when focused tests preserve the public CLI contract.
4. Keep PR feedback below ten minutes by compiling each target once per job.
5. Review educational size waivers when their explicit trigger conditions are reached.

## Deferred Work

The 120 anti-pattern/corrected-example expansion is deferred. Adding more examples before maintaining guided-practice quality would increase review and navigation cost without improving the main learner workflow.

Reconsider that expansion only after:

- all oracle-backed cases have stable assertions where deterministic output permits it;
- CI remains below the feedback target for four consecutive weeks;
- learner feedback identifies specific misconceptions not addressed by current examples and exercises.

## Change Policy

Every curriculum change should update the canonical JSON contract first, then code and README content. Cross-language parity means equal outcomes and comparable evidence, not literal translations.
