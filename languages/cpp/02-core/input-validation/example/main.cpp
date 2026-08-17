// Module focus: Rejecting invalid input before the main workflow continues.
// Why it matters: the example makes it possible to reject malformed and out-of-domain input
// without corrupting state before the learner tackles the exercises.

#include <iostream>
#include <limits>
#include <string>
using namespace std;

// Separate helpers keep the main path focused on how to reject malformed and out-of-domain input
// without corrupting state.
int readIntInRange(const string& label, int minValue, int maxValue) {
    int value = 0;

    while (true) {
        cout << label;
        if (!(cin >> value)) {
            cout << "Invalid input type. Please enter an integer.\n";
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
            continue;
        }

        if (value < minValue || value > maxValue) {
            cout << "Value must be between " << minValue << " and " << maxValue << ".\n";
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
            continue;
        }

        cin.ignore(numeric_limits<streamsize>::max(), '\n');
        return value;
    }
}

double readDoubleInRange(const string& label, double minValue, double maxValue) {
    double value = 0.0;

    while (true) {
        cout << label;
        if (!(cin >> value)) {
            cout << "Invalid input type. Please enter a decimal number.\n";
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
            continue;
        }

        if (value < minValue || value > maxValue) {
            cout << "Value must be between " << minValue << " and " << maxValue << ".\n";
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
            continue;
        }

        cin.ignore(numeric_limits<streamsize>::max(), '\n');
        return value;
    }
}

// Fixed inputs make the consequence of continuing reads without clearing failed stream state
// visible and repeatable.
int main() {
    // These values exercise the normal path before the exercises vary the documented boundaries.
    const int age = readIntInRange("Enter your age (1-120): ", 1, 120);
    const double gpa = readDoubleInRange("Enter your GPA (0.0-4.0): ", 0.0, 4.0);

    // The printed result shows whether the program can design retry and termination behavior that
    // cannot loop accidentally.
    cout << "\nValidated input summary:\n";
    cout << "Age: " << age << '\n';
    cout << "GPA: " << gpa << '\n';

    return 0;
}
