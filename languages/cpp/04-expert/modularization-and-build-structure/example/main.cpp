#include <iostream>

int add(int left, int right) {
    return left + right;
}

int multiply(int left, int right) {
    return left * right;
}

void printReport(int a, int b) {
    std::cout << "Add: " << add(a, b) << '\n';
    std::cout << "Multiply: " << multiply(a, b) << '\n';
}

int main() {
    printReport(3, 7);
    return 0;
}
