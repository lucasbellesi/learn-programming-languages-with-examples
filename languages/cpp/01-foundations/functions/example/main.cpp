// Module focus: Breaking behavior into reusable functions with clear inputs and outputs.
// Why it matters: practicing functions patterns makes exercises and checkpoints easier to reason
// about.

#include <iostream>
#include <vector>
using namespace std;

// Helper setup for functions; this keeps the walkthrough readable.
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

void incrementByValue(int number) {
    ++number;
    cout << "Inside incrementByValue: " << number << '\n';
}

void incrementByReference(int& number) {
    ++number;
    cout << "Inside incrementByReference: " << number << '\n';
}

// Walk through one fixed scenario so functions behavior stays repeatable.
int main() {
    // Prepare sample inputs that exercise the key functions path.
    // Report values so learners can verify the functions outcome.
    cout << "sum(4, 6) = " << sum(4, 6) << '\n';

    int first = 10;
    int second = 20;
    cout << "Before swap: first=" << first << ", second=" << second << '\n';
    swapByReference(first, second);
    cout << "After swap:  first=" << first << ", second=" << second << '\n';

    const vector<int> numbers{1, 2, 3, 4, 5};
    cout << "Vector content: ";
    printVector(numbers);

    int value = 5;
    cout << "\nOriginal value: " << value << '\n';
    incrementByValue(value);
    cout << "After incrementByValue: " << value << '\n';
    incrementByReference(value);
    cout << "After incrementByReference: " << value << '\n';

    return 0;
}
