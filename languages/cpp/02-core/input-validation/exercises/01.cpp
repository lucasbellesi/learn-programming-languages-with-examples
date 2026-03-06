#include <iostream>
#include <limits>

int main() {
    int value = 0;

    while (true) {
        std::cout << "Enter an integer from 1 to 100: ";
        if (!(std::cin >> value)) {
            std::cout << "Invalid input. Please enter an integer.\n";
            std::cin.clear();
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
            continue;
        }

        if (value < 1 || value > 100) {
            std::cout << "Out of range. Try again.\n";
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
            continue;
        }

        break;
    }

    std::cout << "Square: " << (value * value) << '\n';
    return 0;
}
