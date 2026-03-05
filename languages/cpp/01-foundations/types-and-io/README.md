# Types and Input/Output

This module introduces basic C++ data types and console input/output.

## Topics Covered

### `cin` and `cout`

- `std::cout` prints text to the console.
- `std::cin` reads formatted input (for example, integers or doubles).

Example:

```cpp
int age = 0;
std::cin >> age;
std::cout << "Age: " << age << "\n";
```

### `getline`

`std::getline(std::cin, text)` reads a full line, including spaces.  
Use it when you need complete text such as full names or sentences.

### Mixing `cin >>` and `getline` (Common Pitfall)

After `cin >> value`, a newline remains in the input buffer.  
If you call `getline` immediately, it may read that leftover newline and return an empty string.

Fix:

```cpp
std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
```

### Basic C++ Types

- `int`: whole numbers (for example, age, count)
- `double`: decimal numbers (for example, GPA, price)
- `char`: single character
- `bool`: true/false values
- `std::string`: text

## Checkpoint

- [ ] I can read and print values using `cin` and `cout`.
- [ ] I know when to use `getline` instead of `cin >>`.
- [ ] I can avoid input buffer issues using `cin.ignore(...)`.
- [ ] I completed `exercises/01.cpp` and `exercises/02.cpp`.
