# Functions

Functions let you organize reusable logic with clear inputs and outputs.

## Topics Covered

### Pass by Value

A copy of the argument is passed into the function.  
Changes inside the function do not affect the original variable.

### Pass by Reference

A reference (`&`) gives direct access to the original variable.  
Changes inside the function affect the caller's variable.

### Const Reference

A `const T&` avoids copying while preventing modifications.  
Useful for large objects like `std::vector` and `std::string`.

### Returning Values

Functions can return computed results and keep `main` cleaner.

## Checkpoint

- [ ] I understand pass by value vs pass by reference.
- [ ] I know when to use `const` references.
- [ ] I can design a function that returns a value.
- [ ] I completed `exercises/01.cpp` and `exercises/02.cpp`.
