// This example demonstrates modularization and build structure concepts.
// Example purpose: show the module flow with clear, beginner-friendly steps.

#include <iostream>
using namespace std;

int add(int left, int right) { return left + right; }

int multiply(int left, int right) { return left * right; }

void printReport(int a, int b) {
    // Intent: print intermediate or final output for quick behavior verification.
    cout << "Add: " << add(a, b) << '\n';
    cout << "Multiply: " << multiply(a, b) << '\n';
}

int main() {
    // Program flow: collect input, apply core logic, then print a verifiable result.
    printReport(3, 7);
    return 0;
}
