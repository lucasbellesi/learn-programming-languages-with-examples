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

4. Update related README files when behavior or structure changes.
5. Open a pull request with a clear description of what changed and why.

## Content Expectations

- New concept modules should follow the existing folder layout.
- Every exercise file must contain complete, runnable content.
- Avoid external dependencies and test frameworks for C++ modules.
- Keep examples aligned with C++17.

## Commit Messages

Use short, descriptive commit messages that explain intent.

## Code of Conduct

By participating, you agree to follow `CODE_OF_CONDUCT.md`.
