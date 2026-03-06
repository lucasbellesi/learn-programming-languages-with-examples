#include <chrono>
#include <iostream>
#include <vector>

long long sumByValue(std::vector<int> values) {
    long long sum = 0;
    for (int value : values) {
        sum += value;
    }
    return sum;
}

long long sumByConstRef(const std::vector<int>& values) {
    long long sum = 0;
    for (int value : values) {
        sum += value;
    }
    return sum;
}

int main() {
    int n = 0;
    std::cout << "Vector size: ";
    std::cin >> n;

    if (n <= 0) {
        std::cout << "Please enter a positive size.\n";
        return 0;
    }

    std::vector<int> values(static_cast<std::size_t>(n), 1);

    const auto startValue = std::chrono::high_resolution_clock::now();
    const long long a = sumByValue(values);
    const auto endValue = std::chrono::high_resolution_clock::now();

    const auto startRef = std::chrono::high_resolution_clock::now();
    const long long b = sumByConstRef(values);
    const auto endRef = std::chrono::high_resolution_clock::now();

    (void)a;
    (void)b;

    const auto valueTime = std::chrono::duration_cast<std::chrono::microseconds>(endValue - startValue).count();
    const auto refTime = std::chrono::duration_cast<std::chrono::microseconds>(endRef - startRef).count();

    std::cout << "By value (us): " << valueTime << '\n';
    std::cout << "By const ref (us): " << refTime << '\n';

    return 0;
}
