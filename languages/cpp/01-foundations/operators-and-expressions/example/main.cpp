#include <iostream>

int main() {
    const int a = 17;
    const int b = 5;

    std::cout << "a = " << a << ", b = " << b << "\n\n";
    std::cout << "a + b = " << (a + b) << '\n';
    std::cout << "a - b = " << (a - b) << '\n';
    std::cout << "a * b = " << (a * b) << '\n';
    std::cout << "a / b (integer division) = " << (a / b) << '\n';
    std::cout << "a % b = " << (a % b) << '\n';

    const double preciseDivision = static_cast<double>(a) / b;
    std::cout << "a / b (double division) = " << preciseDivision << "\n\n";

    const bool isPositive = (a > 0);
    const bool isEven = (a % 2 == 0);
    const bool passesRule = isPositive && !isEven;

    std::cout << "isPositive: " << (isPositive ? "true" : "false") << '\n';
    std::cout << "isEven: " << (isEven ? "true" : "false") << '\n';
    std::cout << "passesRule (positive and odd): " << (passesRule ? "true" : "false") << '\n';

    return 0;
}
