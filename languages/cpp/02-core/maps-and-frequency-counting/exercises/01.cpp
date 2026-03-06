#include <iostream>
#include <map>

int main() {
    int n = 0;
    std::cout << "How many digits? ";
    std::cin >> n;

    if (n <= 0) {
        std::cout << "Please enter a positive count.\n";
        return 0;
    }

    std::map<int, int> frequency;
    for (int digit = 0; digit <= 9; ++digit) {
        frequency[digit] = 0;
    }

    for (int i = 0; i < n; ++i) {
        int value = 0;
        std::cin >> value;
        if (value >= 0 && value <= 9) {
            ++frequency[value];
        }
    }

    for (int digit = 0; digit <= 9; ++digit) {
        std::cout << digit << " -> " << frequency[digit] << '\n';
    }

    return 0;
}
