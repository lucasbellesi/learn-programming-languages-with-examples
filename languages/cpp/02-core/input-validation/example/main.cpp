// Module focus: Rejecting invalid input before the main workflow continues.
// Why it matters: practicing input validation patterns makes exercises and checkpoints easier to
// reason about.

#include <iostream>
#include <limits>
#include <string>
using namespace std;

// Helper setup for input validation; this keeps the walkthrough readable.
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

// Walk through one fixed scenario so input validation behavior stays repeatable.
int main() {
    // Prepare sample inputs that exercise the key input validation path.
    const int age = readIntInRange("Enter your age (1-120): ", 1, 120);
    const double gpa = readDoubleInRange("Enter your GPA (0.0-4.0): ", 0.0, 4.0);

    // Report values so learners can verify the input validation outcome.
    cout << "\nValidated input summary:\n";
    cout << "Age: " << age << '\n';
    cout << "GPA: " << gpa << '\n';

    return 0;
}
