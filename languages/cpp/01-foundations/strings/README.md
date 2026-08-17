# Strings

This module introduces practical text handling with `std::string`.

## Learning Metadata

- Difficulty: Beginner.
- Estimated Time: 20-35 minutes.
- Prerequisites: `01-foundations/types-and-io`, `01-foundations/control-flow`.
- Cross-Language Lens: Compare immutable string handling, indexing rules, and tokenization helpers in each language.

## Learning Outcomes

- `FND-STR-01`: Normalize, inspect, and transform textual data.
- `FND-STR-02`: Handle empty input and character boundaries safely.

## Quick Run

Run from the repository root:

~~~bash
python scripts/automation.py run-module --module-path languages/cpp/01-foundations/strings
~~~

## More Examples

- `example/string-clean-and-tokenize.cpp`:

```bash
g++ -std=c++17 -Wall -Wextra -pedantic example/string-clean-and-tokenize.cpp -o strings_clean_and_tokenize
./strings_clean_and_tokenize
```

- `example/vowel-count.cpp` keeps character classification separate from the main walkthrough.

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

- In C++, read this module through the native focus ?Strings?; the shared folder name remains stable for side-by-side navigation.
- Use explicit value/reference semantics and standard-library types to demonstrate how to normalize, inspect, and transform textual data.
- Compare observable behavior with the other tracks when learning to handle empty input and character boundaries safely; equivalent evidence matters more than identical syntax.

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

## Check Your Work

Run from the repository root after implementing a starter:

```bash
python scripts/automation.py check-exercise --language cpp --level 01-foundations --module strings --exercise 01
```

Change `--exercise 01` to `--exercise 02` for the second task. Consult `exercises/solutions/` only after making a complete attempt.

## Checkpoint

- [ ] I can read and parse full-line text input.
- [ ] I can use `find`/`substr` safely.
- [ ] I can process characters with `std::tolower` and `std::isalpha`.
- [ ] I completed both exercises.
