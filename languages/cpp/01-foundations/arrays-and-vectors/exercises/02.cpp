#include <iostream>
#include <vector>

int main() {
    int n = 0;
    std::cout << "How many integers will you enter? ";
    std::cin >> n;

    if (n <= 0) {
        std::cout << "Please enter a positive number.\n";
        return 0;
    }

    std::vector<int> values;
    values.reserve(static_cast<std::size_t>(n));

    for (int i = 0; i < n; ++i) {
        int number = 0;
        std::cout << "Number " << (i + 1) << ": ";
        std::cin >> number;
        values.push_back(number);
    }

    int target = 0;
    std::cout << "Enter the number to count: ";
    std::cin >> target;

    int frequency = 0;
    for (int value : values) {
        if (value == target) {
            ++frequency;
        }
    }

    std::cout << target << " appears " << frequency << " time(s).\n";
    return 0;
}
