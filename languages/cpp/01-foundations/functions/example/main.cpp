// Module focus: Breaking behavior into reusable functions with clear inputs and outputs.
// Why it matters: the example makes it possible to decompose a problem into focused functions
// with explicit contracts before the learner tackles the exercises.
// about.

#include <iostream>
#include <vector>
using namespace std;

// Separate helpers keep the main path focused on how to decompose a problem into focused
// functions with explicit contracts.
int sum(int a, int b) { return a + b; }

void swapByReference(int& left, int& right) {
    const int temp = left;
    left = right;
    right = temp;
}

void printVector(const vector<int>& values) {
    cout << "[";
    for (size_t i = 0; i < values.size(); ++i) {
        cout << values[i];
        if (i + 1 < values.size()) {
            cout << ", ";
        }
    }
    cout << "]\n";
}

// Fixed inputs make the consequence of unnecessary copies of large objects visible and
// repeatable.
int main() {
    // These values exercise the normal path before the exercises vary the documented boundaries.
    // The printed result shows whether the program can use parameters and return values without
    // hidden state changes.
    cout << "sum(4, 6) = " << sum(4, 6) << '\n';

    int first = 10;
    int second = 20;
    cout << "Before swap: first=" << first << ", second=" << second << '\n';
    swapByReference(first, second);
    cout << "After swap:  first=" << first << ", second=" << second << '\n';

    const vector<int> numbers{1, 2, 3, 4, 5};
    cout << "Vector content: ";
    printVector(numbers);

    return 0;
}
