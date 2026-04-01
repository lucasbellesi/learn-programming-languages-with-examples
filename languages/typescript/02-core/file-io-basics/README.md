# File I/O Basics

This module introduces beginner-friendly file reading and writing in Node-based TypeScript.

## Learning Metadata

- Difficulty: Intermediate.
- Estimated Time: 30-45 minutes.
- Prerequisites: `01-foundations/strings` and `01-foundations/types-and-io`.
- Cross-Language Lens: Compare `fs.readFileSync` and `fs.writeFileSync` with stream-based or line-based file handling in the other tracks.

## Quick Run

~~~bash
npm run build:typescript
node build/typescript/02-core/file-io-basics/example/main.js
~~~

## Topics Covered

- Reading full files as text.
- Splitting file content into lines safely.
- Writing reports back to disk.
- Keeping file-path logic explicit and local.

## Common Pitfalls

- Assuming files always exist.
- Forgetting to normalize line endings.
- Mixing parsing logic directly into I/O calls.

## Exercise Focus

- exercises/01.ts: read a file path and count non-empty lines.
- exercises/02.ts: copy one text file to another in uppercase.

### Exercise Specs

1. exercises/01.ts
- Input: one file path.
- Output: number of non-empty lines.
- Edge cases: missing file; empty file; blank lines between data rows.

2. exercises/02.ts
- Input: source path and destination path.
- Output: confirmation that the uppercase copy was written.
- Edge cases: missing source file; empty content; source and destination paths that differ only by folder.

## Checkpoint

- [ ] I can read file content and split it into usable records.
- [ ] I can write output files without hiding where they are created.
- [ ] I can validate file-path assumptions before parsing.
- [ ] I completed exercises/01.ts.
- [ ] I completed exercises/02.ts.
