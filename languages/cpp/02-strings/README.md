# 02 Strings

This module introduces practical string handling in C++.

## Learning Goals

- Read full-line text safely with `std::getline`.
- Understand `std::string` size and indexing basics.
- Use common operations: concatenation, `find`, `substr`.
- Avoid common input bugs when mixing `cin >>` and `getline`.

## Quick Run (Terminal)

From this folder:

```bash
g++ -std=c++17 -Wall -Wextra -pedantic example/main.cpp -o strings_example
./strings_example
```

On Windows (MSYS2 shell), run:

```bash
./strings_example.exe
```

## Run In VS Code

1. Open `example/main.cpp`.
2. Press `Ctrl+Shift+B` to build.
3. Run task `Run active C++ file`.
4. For one step, run task `Build and run active C++ file`.

## Topics Covered

### Read Full Text Input

Use `getline` for names and sentences with spaces:

```cpp
std::string line;
std::getline(std::cin, line);
```

### Basic Operations

- `text.size()` for length
- `left + right` for concatenation
- `text.find("word")` to search
- `text.substr(start, length)` to slice

### Common Pitfalls

- Mixing `cin >>` and `getline` without clearing leftover newline.
- Accessing string indexes without checking boundaries.
- Assuming `find` always succeeds (it returns `std::string::npos` when not found).

## Exercise Focus

- `exercises/01.cpp`: count words in a sentence robustly.
- `exercises/02.cpp`: test whether text is a palindrome ignoring case and non-letters.

## Checkpoint

- [ ] I can read and process full sentences.
- [ ] I can use `find` and handle the "not found" case.
- [ ] I can slice text with `substr` when indexes are valid.
- [ ] I completed both exercises and understand each step.
