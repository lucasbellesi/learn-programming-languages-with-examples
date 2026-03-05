#include <iostream>
#include <vector>

int main() {
    int n = 0;
    std::cout << "How many integers? ";
    std::cin >> n;

    if (n <= 0) {
        std::cout << "Please enter a positive number.\n";
        return 0;
    }

    std::vector<int> values;
    values.reserve(static_cast<std::size_t>(n));

    for (int i = 0; i < n; ++i) {
        int current = 0;
        std::cout << "Value " << (i + 1) << ": ";
        std::cin >> current;
        values.push_back(current);
    }

    std::cout << "Reversed order: ";
    for (int i = n - 1; i >= 0; --i) {
        std::cout << values[static_cast<std::size_t>(i)];
        if (i > 0) {
            std::cout << ' ';
        }
    }
    std::cout << '\n';

    return 0;
}
