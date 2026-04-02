// Module focus: Choosing between branches and repeating work with predictable control flow.
// Why it matters: practicing control flow patterns makes exercises and checkpoints easier to reason
// about.

#include <iostream>
using namespace std;

// Walk through one fixed scenario so control flow behavior stays repeatable.
int main() {
    // Prepare sample inputs that exercise the key control flow path.
    int value = 0;
    // Report values so learners can verify the control flow outcome.
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
