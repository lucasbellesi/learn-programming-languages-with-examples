// This example demonstrates error handling and defensive programming concepts.
// Example purpose: show the module flow with clear, beginner-friendly steps.

#include <iostream>
#include <limits>
using namespace std;

bool safeDivide(double left, double right, double& result) {
    // Intent: guard invalid or edge-case paths before the main path continues.
    if (right == 0.0) {
        return false;
    }
    result = left / right;
    return true;
}

int main() {
    // Program flow: collect input, apply core logic, then print a verifiable result.
    double a = 0.0;
    double b = 0.0;

    // Intent: print intermediate or final output for quick behavior verification.
    cout << "Enter two numbers: ";
    // Intent: gather typed input first so later operations are predictable.
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
