#include <iostream>
#include <vector>

int main() {
    int n = 0;
    std::cout << "How many values? ";
    std::cin >> n;

    if (n <= 0) {
        std::cout << "No data to sum.\n";
        return 0;
    }

    std::vector<int> values;
    values.reserve(static_cast<std::size_t>(n));

    for (int i = 0; i < n; ++i) {
        int value = 0;
        std::cin >> value;
        values.push_back(value);
    }

    int chunkSize = 0;
    std::cout << "Chunk size: ";
    std::cin >> chunkSize;

    if (chunkSize <= 0) {
        std::cout << "Chunk size must be positive.\n";
        return 0;
    }

    int total = 0;
    for (int start = 0; start < n; start += chunkSize) {
        int partial = 0;
        const int end = (start + chunkSize < n) ? (start + chunkSize) : n;
        for (int i = start; i < end; ++i) {
            partial += values[static_cast<std::size_t>(i)];
        }
        std::cout << "Partial sum [" << start << ", " << (end - 1) << "]: " << partial << '\n';
        total += partial;
    }

    std::cout << "Total sum: " << total << '\n';
    return 0;
}
