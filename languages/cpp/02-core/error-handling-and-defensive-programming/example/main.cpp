// Module focus: Guarding risky inputs so failures stay explicit and controlled.
// Why it matters: practicing error handling and defensive programming patterns makes exercises and
// checkpoints easier to reason about.

#include <iostream>
#include <limits>
using namespace std;

// Helper setup for error handling and defensive programming; this keeps the walkthrough readable.
bool safeDivide(double left, double right, double& result) {
    if (right == 0.0) {
        return false;
    }
    result = left / right;
    return true;
}

// Walk through one fixed scenario so error handling and defensive programming behavior stays
// repeatable.
int main() {
    // Prepare sample inputs that exercise the key error handling and defensive programming path.
    double a = 0.0;
    double b = 0.0;

    // Report values so learners can verify the error handling and defensive programming outcome.
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
