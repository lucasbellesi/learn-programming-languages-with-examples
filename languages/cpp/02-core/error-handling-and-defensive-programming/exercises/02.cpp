#include <iostream>
#include <limits>

int main() {
    while (true) {
        double a = 0.0;
        double b = 0.0;

        std::cout << "Enter two numbers to divide (a b): ";
        if (!(std::cin >> a >> b)) {
            std::cout << "Invalid input type. Try again.\n";
            std::cin.clear();
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
            continue;
        }

        if (b == 0.0) {
            std::cout << "Divisor cannot be zero. Try again.\n";
            continue;
        }

        std::cout << "Result: " << (a / b) << '\n';
        break;
    }

    return 0;
}
