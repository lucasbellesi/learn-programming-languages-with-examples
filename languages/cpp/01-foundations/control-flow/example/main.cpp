// This example demonstrates control flow concepts.
// Example purpose: show the module flow with clear, beginner-friendly steps.

#include <iostream>
using namespace std;

int main() {
    // Program flow: collect input, apply core logic, then print a verifiable result.
    int value = 0;
    // Intent: print intermediate or final output for quick behavior verification.
    cout << "Enter an integer: ";
    // Intent: gather typed input first so later operations are predictable.
    cin >> value;

    // Intent: guard invalid or edge-case paths before the main path continues.
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
        // Intent: iterate through data in a clear and deterministic order.
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
