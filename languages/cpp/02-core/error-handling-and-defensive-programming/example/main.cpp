// This example demonstrates error handling and defensive programming concepts.

#include <iostream>
#include <limits>
using namespace std;


bool safeDivide(double left, double right, double& result) {
    if (right == 0.0) {
        return false;
    }
    result = left / right;
    return true;
}

int main() {
    double a = 0.0;
    double b = 0.0;

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
