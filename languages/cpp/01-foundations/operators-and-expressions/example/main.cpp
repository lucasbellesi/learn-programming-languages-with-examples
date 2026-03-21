// This example demonstrates operators and expressions concepts.
// Example purpose: show the module flow with clear, beginner-friendly steps.

#include <iostream>
using namespace std;


int main() {
    // Program flow: collect input, apply core logic, then print a verifiable result.
    const int a = 17;
    const int b = 5;

    // Intent: print intermediate or final output for quick behavior verification.
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
