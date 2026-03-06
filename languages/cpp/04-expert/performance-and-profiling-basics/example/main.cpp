#include <chrono>
#include <iostream>
#include <vector>

int linearSearch(const std::vector<int>& values, int target) {
    for (std::size_t i = 0; i < values.size(); ++i) {
        if (values[i] == target) {
            return static_cast<int>(i);
        }
    }
    return -1;
}

int main() {
    std::vector<int> values;
    values.reserve(100000);
    for (int i = 0; i < 100000; ++i) {
        values.push_back(i);
    }

    const auto start = std::chrono::high_resolution_clock::now();
    const int index = linearSearch(values, 99999);
    const auto end = std::chrono::high_resolution_clock::now();

    const auto elapsed = std::chrono::duration_cast<std::chrono::microseconds>(end - start);
    std::cout << "Index: " << index << '\n';
    std::cout << "Elapsed (microseconds): " << elapsed.count() << '\n';

    return 0;
}
