// This example demonstrates scope and lifetime basics concepts.
// Example purpose: show the module flow with clear, beginner-friendly steps.

#include <iostream>
using namespace std;


void printRangeSum(int from, int to) {
    int sum = 0;
    // Intent: iterate through data in a clear and deterministic order.
    for (int value = from; value <= to; ++value) {
        sum += value;
    }
    // Intent: print intermediate or final output for quick behavior verification.
    cout << "Sum from " << from << " to " << to << " = " << sum << '\n';
}

int main() {
    // Program flow: collect input, apply core logic, then print a verifiable result.
    int value = 10;
    cout << "Outer value: " << value << '\n';

    {
        int value = 20;
        cout << "Inner shadowed value: " << value << '\n';
    }

    cout << "Outer value again: " << value << '\n';

    printRangeSum(1, 5);
    return 0;
}
