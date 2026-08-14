# Modularization and Build Structure (Java)

This module shows how to split a Java console program into focused source files with explicit responsibility boundaries.

## Learning Metadata

- Difficulty: Advanced.
- Estimated Time: 45-60 minutes.
- Prerequisites: `02-core/file-io-basics`, `03-advanced/structs-and-classes`, `04-expert/performance-and-profiling-basics`.
- Cross-Language Lens: Compare Java source sets and packages with C++ compilation units, C# projects, Go packages, Python modules, and TypeScript imports.

## Learning Outcomes

- `EXP-MOD-01`: Separate public contracts from implementation details.
- `EXP-MOD-02`: Organize a multi-file program with an explicit build boundary.

## Quick Run

Run from the repository root:

~~~bash
python scripts/automation.py run-module --module-path languages/java/04-expert/modularization-and-build-structure
~~~

## Topics Covered

- Separating domain calculation, formatting, and application flow across files.
- Keeping `Main` focused on orchestration.
- Compiling a source set into one class-output directory.
- Using package-private types to keep a small example API intentional.
- Choosing boundaries by responsibility instead of file size alone.

## Common Pitfalls

- Putting every class into `Main.java` after responsibilities have diverged.
- Creating utility classes that mix calculation, formatting, and input handling.
- Compiling only one source without making sibling sources discoverable.
- Introducing circular dependencies between packages.
- Making every helper public without defining a stable API boundary.

## Cross-Language Notes

- Java compiles source files into classes and normally organizes larger systems through packages and build tools.
- Compared with C++, Java has no header/source split, but source discovery and classpaths still shape the build.
- Compared with TypeScript or Python, Java makes compilation and class-output boundaries more explicit.
- This example stays in the default package for a direct `javac` workflow; a production project should use named packages and Maven or Gradle.

## Exercise Focus

- exercises/Exercise01.java: separate invoice calculation from presentation.
- exercises/Exercise02.java: dispatch reusable arithmetic operations through a registry.

### Exercise Specs

1. exercises/Exercise01.java
- Input: subtotal, discount percent, and tax percent.
- Output: pricing breakdown and final total.
- Edge cases: negative subtotal; percentages outside valid ranges.

2. exercises/Exercise02.java
- Input: command name and two integers.
- Output: result from the registered operation.
- Edge cases: unsupported command; division by zero.

## Check Your Work

Run from the repository root after implementing a starter:

```bash
python scripts/automation.py check-exercise --language java --level 04-expert --module modularization-and-build-structure --exercise 01
```

Change `--exercise 01` to `--exercise 02` for the second task. Consult `exercises/solutions/` only after making a complete attempt.

## Checkpoint

- [ ] I can keep an entrypoint focused on coordination.
- [ ] I can separate calculation and formatting responsibilities.
- [ ] I can compile and run a multi-file Java source set.
- [ ] I can explain when named packages and a build tool become useful.
- [ ] I completed exercises/Exercise01.java.
- [ ] I completed exercises/Exercise02.java.
