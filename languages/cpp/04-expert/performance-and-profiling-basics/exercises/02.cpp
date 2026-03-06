#include <chrono>
#include <iostream>
#include <vector>

int main() {
    int n = 0;
    std::cout << "How many push operations? ";
    std::cin >> n;

    if (n < 0) {
        std::cout << "Please enter a non-negative count.\n";
        return 0;
    }

    std::vector<int> withoutReserve;
    const auto startA = std::chrono::high_resolution_clock::now();
    for (int i = 0; i < n; ++i) {
        withoutReserve.push_back(i);
    }
    const auto endA = std::chrono::high_resolution_clock::now();

    std::vector<int> withReserve;
    withReserve.reserve(static_cast<std::size_t>(n));
    const auto startB = std::chrono::high_resolution_clock::now();
    for (int i = 0; i < n; ++i) {
        withReserve.push_back(i);
    }
    const auto endB = std::chrono::high_resolution_clock::now();

    const auto timeA = std::chrono::duration_cast<std::chrono::microseconds>(endA - startA).count();
    const auto timeB = std::chrono::duration_cast<std::chrono::microseconds>(endB - startB).count();

    std::cout << "Without reserve (us): " << timeA << '\n';
    std::cout << "With reserve (us): " << timeB << '\n';

    return 0;
}
