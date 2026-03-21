// This example demonstrates functions concepts.
// Example purpose: show the module flow with clear, beginner-friendly steps.

#include <iostream>
#include <vector>
using namespace std;


int sum(int a, int b) {
    return a + b;
}

void swapByReference(int& left, int& right) {
    const int temp = left;
    left = right;
    right = temp;
}

void printVector(const vector<int>& values) {
    // Intent: print intermediate or final output for quick behavior verification.
    cout << "[";
    // Intent: iterate through data in a clear and deterministic order.
    for (size_t i = 0; i < values.size(); ++i) {
        cout << values[i];
        // Intent: guard invalid or edge-case paths before the main path continues.
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

int main() {
    // Program flow: collect input, apply core logic, then print a verifiable result.
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
