#include <iostream>
#include <vector>

int main() {
    int n = 0;
    std::cout << "How many sorted values? ";
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

    int target = 0;
    std::cout << "Target: ";
    std::cin >> target;

    int left = 0;
    int right = n - 1;
    int index = -1;

    while (left <= right) {
        const int mid = left + (right - left) / 2;
        const int midValue = values[static_cast<std::size_t>(mid)];

        if (midValue == target) {
            index = mid;
            break;
        }

        if (midValue < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }

    std::cout << "Index: " << index << '\n';
    return 0;
}
