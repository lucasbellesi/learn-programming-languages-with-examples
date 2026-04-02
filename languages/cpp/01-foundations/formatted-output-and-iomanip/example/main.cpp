// This example shows formatting values so output is easier to read and compare.
// In C++, the example keeps value flow, references, and explicit control visible.

#include <iomanip>
#include <iostream>
using namespace std;

// Run one deterministic scenario so the console output makes formatting values so output is easier
// to read and compare easy to verify.
int main() {
    // Build the sample state first, then let the later output confirm the behavior step by step.
    const char* item1 = "Notebook";
    const char* item2 = "Pen";
    const char* item3 = "Backpack";

    const double p1 = 2.5;
    const double p2 = 1.2;
    const double p3 = 30.0;

    // Print the observed state here so learners can connect the code path to a concrete result.
    cout << left << setw(12) << "Item" << right << setw(10) << "Price" << '\n';
    cout << "----------------------\n";

    cout << left << setw(12) << item1 << right << setw(10) << fixed << setprecision(2) << p1
         << '\n';
    cout << left << setw(12) << item2 << right << setw(10) << fixed << setprecision(2) << p2
         << '\n';
    cout << left << setw(12) << item3 << right << setw(10) << fixed << setprecision(2) << p3
         << '\n';

    return 0;
}
