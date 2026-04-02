// This example shows splitting responsibilities so entrypoints and helpers stay focused.
// In C++, the example keeps value flow, references, and explicit control visible.

#include <iostream>
using namespace std;

// Define the reusable pieces first so the main flow can focus on one observable scenario.
int add(int left, int right) { return left + right; }

int multiply(int left, int right) { return left * right; }

void printReport(int a, int b) {
    cout << "Add: " << add(a, b) << '\n';
    cout << "Multiply: " << multiply(a, b) << '\n';
}

// Run one deterministic scenario so the console output makes splitting responsibilities so
// entrypoints and helpers stay focused easy to verify.
int main() {
    // Build the sample state first, then let the later output confirm the behavior step by step.
    printReport(3, 7);
    return 0;
}
