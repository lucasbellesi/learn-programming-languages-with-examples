// This example shows choosing between branches and repeating work with predictable control flow.
// In C++, the example keeps value flow, references, and explicit control visible.

#include <iostream>
using namespace std;

// Run one deterministic scenario so the console output makes choosing between branches and
// repeating work with predictable control flow easy to verify.
int main() {
    // Build the sample state first, then let the later output confirm the behavior step by step.
    int value = 0;
    // Print the observed state here so learners can connect the code path to a concrete result.
    cout << "Enter an integer: ";
    cin >> value;

    if (value > 0) {
        cout << value << " is positive.\n";
    } else if (value < 0) {
        cout << value << " is negative.\n";
    } else {
        cout << "The value is zero.\n";
    }

    int n = 0;
    cout << "Enter N for factorial and counting: ";
    cin >> n;

    if (n < 0) {
        cout << "Factorial is not defined for negative integers.\n";
    } else {
        unsigned long long factorial = 1;
        for (int i = 1; i <= n; ++i) {
            factorial *= static_cast<unsigned long long>(i);
        }
        cout << n << "! = " << factorial << '\n';
    }

    cout << "Numbers from 1 to " << n << ": ";
    if (n > 0) {
        for (int i = 1; i <= n; ++i) {
            cout << i;
            if (i < n) {
                cout << ' ';
            }
        }
    }
    cout << '\n';

    return 0;
}
