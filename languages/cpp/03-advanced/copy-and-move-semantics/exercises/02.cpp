#include <iostream>
#include <string>
#include <utility>
#include <vector>

int main() {
    int n = 0;
    std::cout << "How many strings? ";
    std::cin >> n;

    if (n <= 0) {
        std::cout << "Please enter a positive count.\n";
        return 0;
    }

    std::vector<std::string> values;
    values.reserve(static_cast<std::size_t>(n));

    for (int i = 0; i < n; ++i) {
        std::string temp;
        std::cout << "String " << (i + 1) << ": ";
        std::cin >> temp;
        values.push_back(std::move(temp));
        std::cout << "Current size: " << values.size() << ", capacity: " << values.capacity() << '\n';
    }

    return 0;
}
