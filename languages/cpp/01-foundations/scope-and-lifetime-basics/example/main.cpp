#include <iostream>

void printRangeSum(int from, int to) {
    int sum = 0;
    for (int value = from; value <= to; ++value) {
        sum += value;
    }
    std::cout << "Sum from " << from << " to " << to << " = " << sum << '\n';
}

int main() {
    int value = 10;
    std::cout << "Outer value: " << value << '\n';

    {
        int value = 20;
        std::cout << "Inner shadowed value: " << value << '\n';
    }

    std::cout << "Outer value again: " << value << '\n';

    printRangeSum(1, 5);
    return 0;
}
