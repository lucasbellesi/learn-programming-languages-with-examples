// Module focus: Formatting values so output is easier to read and compare.
// Why it matters: practicing formatted output and iomanip patterns makes exercises and checkpoints
// easier to reason about.

#include <iomanip>
#include <iostream>
using namespace std;

// Walk through one fixed scenario so formatted output and iomanip behavior stays repeatable.
int main() {
    // Prepare sample inputs that exercise the key formatted output and iomanip path.
    const char* item1 = "Notebook";
    const char* item2 = "Pen";
    const char* item3 = "Backpack";

    const double p1 = 2.5;
    const double p2 = 1.2;
    const double p3 = 30.0;

    // Report values so learners can verify the formatted output and iomanip outcome.
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
