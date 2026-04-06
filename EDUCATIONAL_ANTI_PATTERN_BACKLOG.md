# Educational Anti-Pattern Backlog

## Goal

Add one focused **anti-pattern vs corrected version** example pair to the highest-leverage modules, while preserving cross-language parity and stable runnable behavior.

This backlog prioritizes learning impact over raw file count.

## Selection Rules

- Keep each pair short and runnable.
- Keep one teaching point per pair.
- Keep observable output deterministic.
- Keep scenario and output intent aligned across C++, C#, Go, Python, and TypeScript.
- Keep contracts updated for any new runnable entrypoint.

## Top 10 Modules (Priority Order)

1. `02-core/input-validation`
- Anti-pattern: trusting raw input and mixing parsing, validation, and business logic.
- Correct version: parse -> validate -> normalize -> execute.
- Why now: this is the most common beginner failure mode across tracks.

2. `02-core/error-handling-and-defensive-programming`
- Anti-pattern: swallowed errors or generic catch with no actionable context.
- Correct version: specific error paths, explicit fallback, and user-facing explanation.
- Why now: improves debugging habits early.

3. `02-core/file-io-basics`
- Anti-pattern: assume file exists and format is always valid.
- Correct version: file open checks, parse guards, and malformed-row handling.
- Why now: real-world robustness appears here first.

4. `02-core/sorting-and-searching`
- Anti-pattern: use linear search repeatedly after sorting; unstable assumptions on order.
- Correct version: choose algorithm based on data shape and required guarantees.
- Why now: teaches algorithm choice, not only implementation.

5. `02-core/maps-and-frequency-counting`
- Anti-pattern: manual counters with nested loops and missed edge cases.
- Correct version: map-first counting, explicit tie/ordering policy.
- Why now: foundational pattern reused in later projects.

6. `03-advanced/constructors-and-invariants`
- Anti-pattern: allow partially valid objects and patch later.
- Correct version: enforce invariants at creation, reject invalid state early.
- Why now: critical OOP mindset shift.

7. `03-advanced/copy-and-move-semantics`
- Anti-pattern: accidental expensive copies or broken ownership assumptions.
- Correct version: explicit copy/move intent with observable lifecycle behavior.
- Why now: frequent source of confusion and performance regressions.

8. `03-advanced/inheritance-and-polymorphism`
- Anti-pattern: brittle type checks / branching by concrete type.
- Correct version: polymorphic dispatch and interface-driven design.
- Why now: moves learners away from condition-heavy OOP.

9. `04-expert/concurrency-basics`
- Anti-pattern: unsynchronized shared state and race-prone updates.
- Correct version: scoped synchronization and deterministic aggregation path.
- Why now: high-impact correctness topic with subtle bugs.

10. `04-expert/performance-and-profiling-basics`
- Anti-pattern: optimize before measuring, micro-optimize wrong hotspot.
- Correct version: baseline -> measure -> target bottleneck -> re-measure.
- Why now: prevents cargo-cult “performance tuning”.

## Deliverable Shape Per Module

Add one pair under `example/` with naming that stays language-neutral:

- `anti-pattern-main.*`
- `corrected-main.*`

Each file should include:

- module-specific header comment,
- short “what goes wrong / what is fixed” note,
- deterministic output section.

If a track cannot map the exact mechanism (language constraint), keep the same teaching intent and note adaptation in comments.

## PR Plan

### PR 1: Core Defensive Thinking

Modules:
- `02-core/input-validation`
- `02-core/error-handling-and-defensive-programming`
- `02-core/file-io-basics`

Checks:
- `python scripts/automation.py check-cross-language-parity`
- `python scripts/automation.py check-example-output-contracts`
- `python scripts/automation.py check-exercise-parity`
- `python scripts/automation.py verify-repo`

### PR 2: Core Algorithm Decisions

Modules:
- `02-core/sorting-and-searching`
- `02-core/maps-and-frequency-counting`

Checks:
- same as PR 1

### PR 3: Advanced Object Design

Modules:
- `03-advanced/constructors-and-invariants`
- `03-advanced/copy-and-move-semantics`
- `03-advanced/inheritance-and-polymorphism`

Checks:
- same as PR 1

### PR 4: Expert Correctness and Performance

Modules:
- `04-expert/concurrency-basics`
- `04-expert/performance-and-profiling-basics`

Checks:
- same as PR 1

## Definition of Done

- Anti-pattern and corrected examples exist for all 10 modules across all 5 tracks.
- Output contracts cover any new runnable example entrypoints.
- Cross-language parity checks remain green.
- Full `verify-repo` passes.
- README/module notes mention the new pair for discoverability.
