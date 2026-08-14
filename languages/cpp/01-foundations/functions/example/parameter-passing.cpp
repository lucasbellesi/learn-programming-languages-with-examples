#include <iostream>

void incrementByValue(int number) { ++number; }

void incrementByReference(int& number) { ++number; }

int main() {
    int value = 5;
    // Compare a copied argument with an alias to the caller's original value.
    incrementByValue(value);
    std::cout << "After pass-by-value: " << value << '\n';
    incrementByReference(value);
    std::cout << "After pass-by-reference: " << value << '\n';
    return 0;
}
