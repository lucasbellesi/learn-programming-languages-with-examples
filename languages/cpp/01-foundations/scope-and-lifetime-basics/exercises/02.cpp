#include <iostream>

int main() {
    int n = 0;
    std::cout << "Enter N: ";
    std::cin >> n;

    if (n <= 0) {
        std::cout << "N must be positive.\n";
        return 0;
    }

    int sum = 0;
    {
        for (int i = 1; i <= n; ++i) {
            sum += i;
        }
    }

    std::cout << "Sum 1.." << n << " = " << sum << '\n';
    return 0;
}
