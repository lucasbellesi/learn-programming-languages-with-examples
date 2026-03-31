# Modularization and Build Structure (Python)

This module introduces splitting a Python program into focused modules.

## Learning Metadata

- Difficulty: Expert.
- Estimated Time: 30-45 minutes.
- Prerequisites: `02-core/file-io-basics`, `03-advanced/structs-and-classes`.
- Cross-Language Lens: Compare headers and source files, project references, packages, and Python modules as ways to separate responsibilities.
## Quick Run

~~~bash
python example/main.py
~~~

## Topics Covered

- Separating pricing, formatting, and orchestration across files.
- Importing reusable helpers from sibling modules.
- Keeping the entrypoint focused on flow.
- Treating module layout as part of design, not just organization.

## Common Pitfalls

- Putting every concern directly into `main.py`.
- Mixing calculations, formatting, and coordination in one function.
- Creating helper modules with hidden side effects at import time.
- Treating file structure as irrelevant to maintainability.

## Exercise Focus

- exercises/01.py: separate invoice calculations into focused helpers.
- exercises/02.py: build reusable command operations consumed by one caller.

### Exercise Specs

1. exercises/01.py
- Input: subtotal, discount percent, tax percent.
- Output: subtotal breakdown and final total.
- Edge cases: negative subtotal; percentages outside valid ranges.

2. exercises/02.py
- Input: command name and integer operands.
- Output: result from a reusable operation registry.
- Edge cases: unsupported command; division by zero.

## Checkpoint

- [ ] I can separate coordination code from reusable modules.
- [ ] I can explain why a helper module exists.
- [ ] I can keep `main.py` focused on flow rather than every detail.
- [ ] I completed exercises/01.py.
- [ ] I completed exercises/02.py.
