// This example shows guarding risky inputs so failures stay explicit and controlled.
// In C++, the example keeps value flow, references, and explicit control visible.

#include <iostream>
#include <limits>
using namespace std;

// Define the reusable pieces first so the main flow can focus on one observable scenario.
bool safeDivide(double left, double right, double& result) {
    if (right == 0.0) {
        return false;
    }
    result = left / right;
    return true;
}

// Run one deterministic scenario so the console output makes guarding risky inputs so failures stay
// explicit and controlled easy to verify.
int main() {
    // Build the sample state first, then let the later output confirm the behavior step by step.
    double a = 0.0;
    double b = 0.0;

    // Print the observed state here so learners can connect the code path to a concrete result.
    cout << "Enter two numbers: ";
    if (!(cin >> a >> b)) {
        cout << "Invalid numeric input.\n";
        return 0;
    }

    double quotient = 0.0;
    if (!safeDivide(a, b, quotient)) {
        cout << "Cannot divide by zero.\n";
        return 0;
    }

    cout << "Result: " << quotient << '\n';

    cin.ignore(numeric_limits<streamsize>::max(), '\n');
    return 0;
}
