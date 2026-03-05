#include <iostream>

int main() {
    int value = 0;
    std::cout << "Enter an integer: ";
    std::cin >> value;

    if (value > 0) {
        std::cout << value << " is positive.\n";
    } else if (value < 0) {
        std::cout << value << " is negative.\n";
    } else {
        std::cout << "The value is zero.\n";
    }

    int n = 0;
    std::cout << "Enter N for factorial and counting: ";
    std::cin >> n;

    if (n < 0) {
        std::cout << "Factorial is not defined for negative integers.\n";
    } else {
        unsigned long long factorial = 1;
        for (int i = 1; i <= n; ++i) {
            factorial *= static_cast<unsigned long long>(i);
        }
        std::cout << n << "! = " << factorial << '\n';
    }

    std::cout << "Numbers from 1 to " << n << ": ";
    if (n > 0) {
        for (int i = 1; i <= n; ++i) {
            std::cout << i;
            if (i < n) {
                std::cout << ' ';
            }
        }
    }
    std::cout << '\n';

    return 0;
}
