# C++ Level Assessments

Use these assessments after finishing each level to check practical readiness.

## Assessment Order

1. [01-foundations](./01-foundations/README.md)
2. [02-core](./02-core/README.md)
3. [03-advanced](./03-advanced/README.md)
4. [04-expert](./04-expert/README.md)

Each assessment contains:

- `README.md` with requirements and sample input/output.
- an incomplete `starter/main.cpp` for the learner attempt.
- a runnable reference implementation under `solutions/` for post-attempt review.
- named normal and edge cases checked through `check-checkpoint`.

Run an assessment from the repository root:

```bash
python scripts/automation.py check-checkpoint --language cpp --kind assessment --level 01-foundations
```

Change `--level` for later assessments. Add `--solution` only after completing an attempt.
