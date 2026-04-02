# Strings

This module introduces practical text handling with `std::string`.

## Learning Metadata

- Difficulty: Beginner.
- Estimated Time: 20-35 minutes.
- Prerequisites: `01-foundations/types-and-io`, `01-foundations/control-flow`.
- Cross-Language Lens: Compare immutable string handling, indexing rules, and tokenization helpers in each language.

## Quick Run

```bash
g++ -std=c++17 -Wall -Wextra -pedantic example/main.cpp -o strings_example
./strings_example
```

## More Examples

- `example/string-clean-and-tokenize.cpp`:

```bash
g++ -std=c++17 -Wall -Wextra -pedantic example/string-clean-and-tokenize.cpp -o strings_clean_and_tokenize
./strings_clean_and_tokenize
```

## Topics Covered

- Reading full lines with `std::getline`.
- `size`, `find`, and `substr`.
- Character inspection with `<cctype>`.
- Case-insensitive comparisons.

## Common Pitfalls

- Forgetting to clear newline before `getline`.
- Using string indexes without boundary checks.
- Not checking for `std::string::npos` after `find`.

## Cross-Language Notes

- Compared with C++, the other tracks usually hide more of the low-level string-management cost while keeping the same parsing goals.
- Relative to Python and TypeScript, C# and Go keep more explicit API choices around splitting, trimming, and rebuilding text.
- The main comparison is text-processing convenience versus how visible allocation and mutation remain.

## Exercise Focus

- `exercises/01.cpp`: count words in a sentence.
- `exercises/02.cpp`: palindrome check ignoring case and non-letters.

### Exercise Specs

1. `exercises/01.cpp`
- Input: one line of text.
- Output: integer word count.
- Edge cases: multiple spaces between words; empty or whitespace-only lines.

2. `exercises/02.cpp`
- Input: one line of text.
- Output: `Palindrome: true` or `Palindrome: false`.
- Edge cases: mixed case letters; punctuation and spaces should be ignored.

## Checkpoint

- [ ] I can read and parse full-line text input.
- [ ] I can use `find`/`substr` safely.
- [ ] I can process characters with `std::tolower` and `std::isalpha`.
- [ ] I completed both exercises.
