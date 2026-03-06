#include <iomanip>
#include <iostream>

int main() {
    int precision = 2;
    std::cout << "Enter precision (0-6): ";
    std::cin >> precision;

    if (precision < 0 || precision > 6) {
        std::cout << "Precision must be between 0 and 6.\n";
        return 0;
    }

    int n = 0;
    std::cout << "How many numbers? ";
    std::cin >> n;
    if (n <= 0) {
        std::cout << "Please enter a positive count.\n";
        return 0;
    }

    double value = 0.0;
    double sum = 0.0;
    double minValue = 0.0;
    double maxValue = 0.0;

    for (int i = 0; i < n; ++i) {
        std::cout << "Value " << (i + 1) << ": ";
        std::cin >> value;

        if (i == 0) {
            minValue = value;
            maxValue = value;
        } else {
            if (value < minValue) {
                minValue = value;
            }
            if (value > maxValue) {
                maxValue = value;
            }
        }

        sum += value;
    }

    const double average = sum / n;

    std::cout << std::fixed << std::setprecision(precision);
    std::cout << "Average: " << average << '\n';
    std::cout << "Minimum: " << minValue << '\n';
    std::cout << "Maximum: " << maxValue << '\n';

    return 0;
}
