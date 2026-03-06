#include <algorithm>
#include <iostream>
#include <vector>

int main() {
    std::vector<int> values{7, 2, 9, 4, 2, 8};

    std::sort(values.begin(), values.end());

    std::cout << "Sorted: ";
    for (int value : values) {
        std::cout << value << ' ';
    }
    std::cout << '\n';

    const int target = 4;
    auto it = std::lower_bound(values.begin(), values.end(), target);

    if (it != values.end() && *it == target) {
        const std::size_t index = static_cast<std::size_t>(it - values.begin());
        std::cout << "Found " << target << " at index " << index << '\n';
    } else {
        std::cout << target << " not found\n";
    }

    return 0;
}
