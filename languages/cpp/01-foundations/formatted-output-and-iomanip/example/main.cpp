// Module focus: Formatting values so output is easier to read and compare.
// Why it matters: the example makes it possible to produce stable human-readable tabular and
// numeric output before the learner tackles the exercises.

#include <iomanip>
#include <iostream>
using namespace std;

// Fixed inputs make the consequence of forgetting `<iomanip>` include visible and repeatable.
int main() {
    // These values exercise the normal path before the exercises vary the documented boundaries.
    const char* item1 = "Notebook";
    const char* item2 = "Pen";
    const char* item3 = "Backpack";

    const double p1 = 2.5;
    const double p2 = 1.2;
    const double p3 = 30.0;

    // The printed result shows whether the program can choose precision, alignment, and labels
    // appropriate to the data.
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
