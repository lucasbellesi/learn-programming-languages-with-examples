#include <iostream>
#include <vector>

int main() {
    int n = 0;
    std::cout << "How many integers? ";
    std::cin >> n;

    if (n <= 0) {
        std::cout << "Please enter a positive count.\n";
        return 0;
    }

    std::vector<int> values;
    values.reserve(static_cast<std::size_t>(n));

    for (int i = 0; i < n; ++i) {
        int value = 0;
        std::cout << "Value " << (i + 1) << ": ";
        std::cin >> value;
        values.push_back(value);
    }

    int minValue = values[0];
    int maxValue = values[0];
    int evenCount = 0;

    for (int value : values) {
        if (value < minValue) {
            minValue = value;
        }
        if (value > maxValue) {
            maxValue = value;
        }
        if (value % 2 == 0) {
            ++evenCount;
        }
    }

    std::cout << "Minimum: " << minValue << '\n';
    std::cout << "Maximum: " << maxValue << '\n';
    std::cout << "Even numbers: " << evenCount << '\n';
    return 0;
}
