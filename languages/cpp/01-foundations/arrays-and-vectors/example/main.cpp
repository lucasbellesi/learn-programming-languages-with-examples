#include <iostream>
#include <vector>

int main() {
    const int fixedScores[3] = {72, 88, 95};

    std::cout << "Fixed array values: ";
    for (int i = 0; i < 3; ++i) {
        std::cout << fixedScores[i];
        if (i < 2) {
            std::cout << ", ";
        }
    }
    std::cout << '\n';

    int count = 0;
    std::cout << "How many temperatures do you want to enter? ";
    std::cin >> count;

    if (count <= 0) {
        std::cout << "Nothing to process.\n";
        return 0;
    }

    std::vector<double> temperatures;
    temperatures.reserve(static_cast<std::size_t>(count));

    for (int i = 0; i < count; ++i) {
        double value = 0.0;
        std::cout << "Temperature " << (i + 1) << ": ";
        std::cin >> value;
        temperatures.push_back(value);
    }

    double sum = 0.0;
    for (double value : temperatures) {
        sum += value;
    }

    const double average = sum / temperatures.size();

    std::cout << "\nYou entered: ";
    for (std::size_t i = 0; i < temperatures.size(); ++i) {
        std::cout << temperatures[i];
        if (i + 1 < temperatures.size()) {
            std::cout << ", ";
        }
    }
    std::cout << '\n';
    std::cout << "Average temperature: " << average << '\n';

    return 0;
}
