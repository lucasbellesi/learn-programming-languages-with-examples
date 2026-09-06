# Self-Directed Study Plan

This course is designed for work from the repository root. Choose one language and keep the same track for a full level before using another language for comparison.

## Choose a Route

The guided route is for a first encounter with the concepts: run each example, complete
exercises 01 and 02, complete the guided project, then take the independent assessment.
Request hint stages in order and stop as soon as you can continue.

The comparative route is for programmers transferring existing knowledge: run the
examples, complete exercise 02, take the independent assessment, and compare the module's
cross-language notes with a language you know. Projects are optional when the assessment
already demonstrates transfer.

## First-Session Walkthrough

1. Open the repository folder in your editor, then open a terminal in that folder.
   You should see `README.md`, `languages`, and `scripts` there. All course commands
   below start from this folder, not the module's `example` directory.
2. Follow your language guide's prerequisites and run `doctor` for that language.
   If the terminal cannot find a command, check the installation and reopen the
   terminal so it picks up your updated PATH.
3. Open the first module's README and its file under `example/` side by side.
   Read **Observe, Predict, Modify**, predict the result, then use **Quick Run**.
   Some examples wait for keyboard input; Java and TypeScript entry examples use
   fixed data and finish immediately.
4. Make the suggested change, explain why the output changes, and restore it.
   If you cannot explain a line, trace the value it reads, computes, or prints.
5. Open exercise `01` under `exercises/` and implement its TODOs. The worked
   example teaches the building blocks; the exercise applies them to a new problem.
   Use the visible input/output cases as a specification, including prompt text
   where the checker compares full output.
6. Run `check-exercise`. A failed case is feedback: compare the named case's input,
   expected output, and actual output. Fix the earliest mismatch and rerun.
   If stuck, request hint stage 1, then 2, then 3 only as needed.
7. Try a new input of your own before opening the reference solution. Passing the
   listed cases is useful evidence, but it does not prove correctness for every input.
   Record your change and one explanation in [the learning log](LEARNING_LOG_TEMPLATE.md).

The folder names are shared comparison keys. Names such as `templates-basics`,
`smart-pointers-in-depth`, and `memory-management-and-raii` originate in C++;
other tracks teach their own approaches. Read each module's title and cross-language
notes rather than assuming that every language has C++ templates, pointers, or RAII.
Likewise, `04-expert` names the final course level, not a guarantee of professional mastery.

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
python scripts/automation.py hint-exercise --language python --level 01-foundations --module types-and-io --exercise 01 --stage 1
python scripts/automation.py check-checkpoint --language python --kind project --level 01-foundations
python scripts/automation.py check-checkpoint --language python --kind assessment --level 01-foundations
```

Reference solutions are intentionally separate. Add `--solution` only after completing and checking your own attempt.

## Completion Standard

- [ ] All 24 module examples run.
- [ ] All 48 exercise starters are implemented and pass their named cases.
- [ ] All four projects and four assessments pass their checkpoint contracts.
- [ ] The track checklist remains an honest record of your own progress.
- [ ] I reviewed my work with `LEARNER_SOLUTION_RUBRIC.md`.
- [ ] You can explain at least one idiomatic difference from another language for each level.
