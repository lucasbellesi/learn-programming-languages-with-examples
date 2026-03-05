#include <iostream>

int maxOfThree(int a, int b, int c) {
    int currentMax = a;
    if (b > currentMax) {
        currentMax = b;
    }
    if (c > currentMax) {
        currentMax = c;
    }
    return currentMax;
}

int main() {
    int x = 0;
    int y = 0;
    int z = 0;

    std::cout << "Enter three integers: ";
    std::cin >> x >> y >> z;

    std::cout << "Maximum: " << maxOfThree(x, y, z) << '\n';
    return 0;
}
