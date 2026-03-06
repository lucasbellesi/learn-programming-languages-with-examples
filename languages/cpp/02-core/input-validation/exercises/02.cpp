#include <iostream>
#include <limits>

int main() {
    int count = 0;

    while (true) {
        std::cout << "How many scores (1-50)? ";
        if (!(std::cin >> count)) {
            std::cout << "Invalid input. Please enter an integer.\n";
            std::cin.clear();
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
            continue;
        }

        if (count < 1 || count > 50) {
            std::cout << "Count must be between 1 and 50.\n";
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
            continue;
        }

        break;
    }

    double sum = 0.0;
    for (int i = 0; i < count; ++i) {
        double score = 0.0;

        while (true) {
            std::cout << "Score " << (i + 1) << " (0-100): ";
            if (!(std::cin >> score)) {
                std::cout << "Invalid input. Please enter a number.\n";
                std::cin.clear();
                std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
                continue;
            }

            if (score < 0.0 || score > 100.0) {
                std::cout << "Score must be between 0 and 100.\n";
                std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
                continue;
            }

            break;
        }

        sum += score;
    }

    std::cout << "Average score: " << (sum / count) << '\n';
    return 0;
}
