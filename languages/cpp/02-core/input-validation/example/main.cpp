#include <iostream>
#include <limits>
#include <string>

int readIntInRange(const std::string& label, int minValue, int maxValue) {
    int value = 0;

    while (true) {
        std::cout << label;
        if (!(std::cin >> value)) {
            std::cout << "Invalid input type. Please enter an integer.\n";
            std::cin.clear();
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
            continue;
        }

        if (value < minValue || value > maxValue) {
            std::cout << "Value must be between " << minValue << " and " << maxValue << ".\n";
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
            continue;
        }

        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
        return value;
    }
}

double readDoubleInRange(const std::string& label, double minValue, double maxValue) {
    double value = 0.0;

    while (true) {
        std::cout << label;
        if (!(std::cin >> value)) {
            std::cout << "Invalid input type. Please enter a decimal number.\n";
            std::cin.clear();
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
            continue;
        }

        if (value < minValue || value > maxValue) {
            std::cout << "Value must be between " << minValue << " and " << maxValue << ".\n";
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
            continue;
        }

        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
        return value;
    }
}

int main() {
    const int age = readIntInRange("Enter your age (1-120): ", 1, 120);
    const double gpa = readDoubleInRange("Enter your GPA (0.0-4.0): ", 0.0, 4.0);

    std::cout << "\nValidated input summary:\n";
    std::cout << "Age: " << age << '\n';
    std::cout << "GPA: " << gpa << '\n';

    return 0;
}
