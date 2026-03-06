#include <iostream>
#include <vector>

int main() {
    int n = 0;
    std::cout << "How many numbers? ";
    std::cin >> n;

    if (n <= 0) {
        std::cout << "Please enter a positive count.\n";
        return 0;
    }

    std::vector<int> values;
    values.reserve(static_cast<std::size_t>(n));

    for (int i = 0; i < n; ++i) {
        int value = 0;
        std::cin >> value;
        values.push_back(value);
    }

    for (int i = 0; i < n - 1; ++i) {
        int minIndex = i;
        for (int j = i + 1; j < n; ++j) {
            if (values[static_cast<std::size_t>(j)] < values[static_cast<std::size_t>(minIndex)]) {
                minIndex = j;
            }
        }

        const int temp = values[static_cast<std::size_t>(i)];
        values[static_cast<std::size_t>(i)] = values[static_cast<std::size_t>(minIndex)];
        values[static_cast<std::size_t>(minIndex)] = temp;
    }

    for (int value : values) {
        std::cout << value << ' ';
    }
    std::cout << '\n';

    return 0;
}
