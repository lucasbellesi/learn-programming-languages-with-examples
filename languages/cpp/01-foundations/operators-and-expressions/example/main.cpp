// Module focus: Combining values through expressions and readable calculations.
// Why it matters: practicing operators and expressions patterns makes exercises and checkpoints
// easier to reason about.

#include <iostream>
using namespace std;

// Walk through one fixed scenario so operators and expressions behavior stays repeatable.
int main() {
    // Prepare sample inputs that exercise the key operators and expressions path.
    const int a = 17;
    const int b = 5;

    // Report values so learners can verify the operators and expressions outcome.
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
