// This example demonstrates formatted output and iomanip concepts.
// Example purpose: show the module flow with clear, beginner-friendly steps.

#include <iomanip>
#include <iostream>
using namespace std;

int main() {
    // Program flow: collect input, apply core logic, then print a verifiable result.
    const char* item1 = "Notebook";
    const char* item2 = "Pen";
    const char* item3 = "Backpack";

    const double p1 = 2.5;
    const double p2 = 1.2;
    const double p3 = 30.0;

    // Intent: print intermediate or final output for quick behavior verification.
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
