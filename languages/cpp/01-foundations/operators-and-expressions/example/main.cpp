// Module focus: Combining values through expressions and readable calculations.
// Why it matters: the example makes it possible to build expressions with correct precedence
// and explicit intent before the learner tackles the exercises.

#include <iostream>
using namespace std;

// Fixed inputs make the consequence of integer division when a decimal result is expected visible
// and repeatable.
int main() {
    // These values exercise the normal path before the exercises vary the documented boundaries.
    const int a = 17;
    const int b = 5;

    // The printed result shows whether the program can distinguish arithmetic, comparison, and
    // logical operations.
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
