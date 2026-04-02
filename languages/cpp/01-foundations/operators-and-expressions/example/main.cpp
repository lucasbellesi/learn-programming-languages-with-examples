// This example shows combining values through expressions and readable calculations.
// In C++, the example keeps value flow, references, and explicit control visible.

#include <iostream>
using namespace std;

// Run one deterministic scenario so the console output makes combining values through expressions
// and readable calculations easy to verify.
int main() {
    // Build the sample state first, then let the later output confirm the behavior step by step.
    const int a = 17;
    const int b = 5;

    // Print the observed state here so learners can connect the code path to a concrete result.
    cout << "a = " << a << ", b = " << b << "\n\n";
    cout << "a + b = " << (a + b) << '\n';
    cout << "a - b = " << (a - b) << '\n';
    cout << "a * b = " << (a * b) << '\n';
    cout << "a / b (integer division) = " << (a / b) << '\n';
    cout << "a % b = " << (a % b) << '\n';

    const double preciseDivision = static_cast<double>(a) / b;
    cout << "a / b (double division) = " << preciseDivision << "\n\n";

    const bool isPositive = (a > 0);
    const bool isEven = (a % 2 == 0);
    const bool passesRule = isPositive && !isEven;

    cout << "isPositive: " << (isPositive ? "true" : "false") << '\n';
    cout << "isEven: " << (isEven ? "true" : "false") << '\n';
    cout << "passesRule (positive and odd): " << (passesRule ? "true" : "false") << '\n';

    return 0;
}
