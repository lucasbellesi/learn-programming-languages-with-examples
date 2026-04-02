// This example shows rejecting invalid input before the main workflow continues.
// In C++, the example keeps value flow, references, and explicit control visible.

#include <iostream>
#include <limits>
#include <string>
using namespace std;

// Define the reusable pieces first so the main flow can focus on one observable scenario.
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

// Run one deterministic scenario so the console output makes rejecting invalid input before the
// main workflow continues easy to verify.
int main() {
    // Build the sample state first, then let the later output confirm the behavior step by step.
    const int age = readIntInRange("Enter your age (1-120): ", 1, 120);
    const double gpa = readDoubleInRange("Enter your GPA (0.0-4.0): ", 0.0, 4.0);

    // Print the observed state here so learners can connect the code path to a concrete result.
    cout << "\nValidated input summary:\n";
    cout << "Age: " << age << '\n';
    cout << "GPA: " << gpa << '\n';

    return 0;
}
