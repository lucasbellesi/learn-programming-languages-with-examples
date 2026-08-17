// Module focus: Guarding risky inputs so failures stay explicit and controlled.
// Why it matters: the example makes it possible to separate expected failures from
// programming defects before the learner tackles the exercises.

#include <iostream>
#include <limits>
using namespace std;

// Separate helpers keep the main path focused on how to separate expected failures from
// programming defects.
bool safeDivide(double left, double right, double& result) {
    if (right == 0.0) {
        return false;
    }
    result = left / right;
    return true;
}

// A fixed scenario makes the main decision path visible and repeatable.
int main() {
    // These values exercise the normal path before the exercises vary the documented boundaries.
    double a = 0.0;
    double b = 0.0;

    // The printed result shows whether the program can preserve valid state and useful
    // diagnostics when operations fail.
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
