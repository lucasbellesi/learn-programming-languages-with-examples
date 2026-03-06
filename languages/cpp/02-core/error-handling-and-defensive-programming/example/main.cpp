#include <iostream>
#include <limits>

bool safeDivide(double left, double right, double& result) {
    if (right == 0.0) {
        return false;
    }
    result = left / right;
    return true;
}

int main() {
    double a = 0.0;
    double b = 0.0;

    std::cout << "Enter two numbers: ";
    if (!(std::cin >> a >> b)) {
        std::cout << "Invalid numeric input.\n";
        return 0;
    }

    double quotient = 0.0;
    if (!safeDivide(a, b, quotient)) {
        std::cout << "Cannot divide by zero.\n";
        return 0;
    }

    std::cout << "Result: " << quotient << '\n';

    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
    return 0;
}
