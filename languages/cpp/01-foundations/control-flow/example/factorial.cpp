#include <iostream>

int main() {
    int value = 0;
    std::cout << "Enter a non-negative integer: ";
    std::cin >> value;
    if (value < 0) {
        std::cout << "Factorial is not defined for negative integers.\n";
        return 0;
    }

    // The accumulator starts at the multiplicative identity so 0! remains 1.
    unsigned long long factorial = 1;
    for (int current = 2; current <= value; ++current) {
        factorial *= static_cast<unsigned long long>(current);
    }
    std::cout << value << "! = " << factorial << '\n';
    return 0;
}
