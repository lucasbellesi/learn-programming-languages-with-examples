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

    int target = 0;
    std::cout << "Target to find: ";
    std::cin >> target;

    int index = -1;
    for (int i = 0; i < n; ++i) {
        if (values[static_cast<std::size_t>(i)] == target) {
            index = i;
            break;
        }
    }

    std::cout << "First index: " << index << '\n';
    return 0;
}
