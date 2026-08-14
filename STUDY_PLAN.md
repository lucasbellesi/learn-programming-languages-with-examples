# Self-Directed Study Plan

This course is designed for work from the repository root. Choose one language and keep the same track for a full level before using another language for comparison.

## Standard Pace: 8 Weeks

Plan for five sessions of 60-90 minutes each week. For every module: read the README, run the example, implement both starters, run `check-exercise`, and record one mistake or tradeoff you learned.

### Week 1 - Foundations I

- `types-and-io`
- `operators-and-expressions`
- `control-flow`
- `functions`

### Week 2 - Foundations II

- `arrays-and-vectors`
- `strings`
- `scope-and-lifetime-basics`
- `formatted-output-and-iomanip`
- Foundations project and assessment

### Week 3 - Core I

- `input-validation`
- `algorithms-basics`
- `file-io-basics`

### Week 4 - Core II

- `sorting-and-searching`
- `maps-and-frequency-counting`
- `error-handling-and-defensive-programming`
- Core project and assessment

### Week 5 - Advanced I

- `structs-and-classes`
- `constructors-and-invariants`
- `copy-and-move-semantics`

### Week 6 - Advanced II

- `inheritance-and-polymorphism`
- `templates-basics`
- Advanced project and assessment

### Week 7 - Expert I

- `memory-management-and-raii`
- `smart-pointers-in-depth`
- `concurrency-basics`

### Week 8 - Expert II

- `performance-and-profiling-basics`
- `modularization-and-build-structure`
- Expert project and assessment
- Final review of the language checklist

## Accelerated Pace: 4 Weeks

Use this only if you already program in another language. Complete two standard weeks per week:

1. Week 1: all foundations modules, project, and assessment.
2. Week 2: all core modules, project, and assessment.
3. Week 3: all advanced modules, project, and assessment.
4. Week 4: all expert modules, project, and assessment.

Do not skip automated cases. Reduce written reflection and companion examples before reducing exercise or checkpoint coverage.

## Course Commands

Replace the sample language and module identifiers while keeping the commands at the repository root:

```bash
python scripts/automation.py doctor --language python
python scripts/automation.py run-module --module-path languages/python/01-foundations/types-and-io
python scripts/automation.py check-exercise --language python --level 01-foundations --module types-and-io --exercise 01
python scripts/automation.py check-checkpoint --language python --kind project --level 01-foundations
python scripts/automation.py check-checkpoint --language python --kind assessment --level 01-foundations
```

Reference solutions are intentionally separate. Add `--solution` only after completing and checking your own attempt.

## Completion Standard

- [ ] All 24 module examples run.
- [ ] All 48 exercise starters are implemented and pass their named cases.
- [ ] All four projects and four assessments pass their checkpoint contracts.
- [ ] The track checklist remains an honest record of your own progress.
- [ ] You can explain at least one idiomatic difference from another language for each level.
