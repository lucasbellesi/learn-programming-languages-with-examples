#include <cstddef>
#include <iostream>
#include <memory>

int main() {
    int n = 0;
    std::cout << "How many integers? ";
    std::cin >> n;

    if (n <= 0) {
        std::cout << "Please enter a positive count.\n";
        return 0;
    }

    std::unique_ptr<int[]> values(new int[static_cast<std::size_t>(n)]);

    for (int i = 0; i < n; ++i) {
        std::cout << "Value " << (i + 1) << ": ";
        std::cin >> values[static_cast<std::size_t>(i)];
    }

    long long sum = 0;
    for (int i = 0; i < n; ++i) {
        sum += values[static_cast<std::size_t>(i)];
    }

    std::cout << "Sum: " << sum << '\n';
    std::cout << "Reversed: ";
    for (int i = n - 1; i >= 0; --i) {
        std::cout << values[static_cast<std::size_t>(i)];
        if (i > 0) {
            std::cout << ' ';
        }
    }
    std::cout << '\n';

    return 0;
}
