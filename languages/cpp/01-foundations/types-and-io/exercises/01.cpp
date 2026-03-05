#include <iostream>

int main() {
    int n = 0;
    std::cout << "How many numbers will you enter? ";
    std::cin >> n;

    if (n <= 0) {
        std::cout << "Please enter a positive count.\n";
        return 0;
    }

    double value = 0.0;
    double sum = 0.0;
    double minimum = 0.0;
    double maximum = 0.0;

    for (int i = 0; i < n; ++i) {
        std::cout << "Number " << (i + 1) << ": ";
        std::cin >> value;

        if (i == 0) {
            minimum = value;
            maximum = value;
        } else {
            if (value < minimum) {
                minimum = value;
            }
            if (value > maximum) {
                maximum = value;
            }
        }

        sum += value;
    }

    const double average = sum / n;

    std::cout << "\nResults:\n";
    std::cout << "Sum: " << sum << '\n';
    std::cout << "Average: " << average << '\n';
    std::cout << "Minimum: " << minimum << '\n';
    std::cout << "Maximum: " << maximum << '\n';

    return 0;
}
