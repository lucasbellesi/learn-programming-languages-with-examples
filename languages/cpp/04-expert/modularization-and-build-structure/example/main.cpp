// This example demonstrates modularization and build structure concepts.

#include <iostream>
using namespace std;


int add(int left, int right) {
    return left + right;
}

int multiply(int left, int right) {
    return left * right;
}

void printReport(int a, int b) {
    cout << "Add: " << add(a, b) << '\n';
    cout << "Multiply: " << multiply(a, b) << '\n';
}

int main() {
    printReport(3, 7);
    return 0;
}
