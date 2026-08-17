// Module focus: Choosing between branches and repeating work with predictable control flow.
// Why it matters: the example makes it possible to select branches that cover normal and boundary
// conditions before the learner tackles the exercises.
// about.

#include <iostream>
using namespace std;

// Fixed inputs make the consequence of missing braces in multi-line branches visible and
// repeatable.
int main() {
    // These values exercise the normal path before the exercises vary the documented boundaries.
    int value = 0;
    // The printed result shows whether the program can write terminating loops and reason about
    // their invariants.
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
    cout << "Enter N for counting: ";
    cin >> n;

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
