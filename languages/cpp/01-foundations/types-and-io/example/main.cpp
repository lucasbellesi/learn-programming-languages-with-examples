// This example shows reading typed input carefully and turning raw text into values.
// In C++, the example keeps value flow, references, and explicit control visible.

#include <iostream>
#include <limits>
#include <string>
using namespace std;

// Run one deterministic scenario so the console output makes reading typed input carefully and
// turning raw text into values easy to verify.
int main() {
    // Build the sample state first, then let the later output confirm the behavior step by step.
    string fullName;
    int age = 0;
    double gpa = 0.0;
    char enrolledAnswer = 'n';

    // Print the observed state here so learners can connect the code path to a concrete result.
    cout << "Enter your full name: ";
    getline(cin, fullName);

    cout << "Enter your age: ";
    cin >> age;

    cout << "Enter your GPA: ";
    cin >> gpa;

    // Clear the leftover newline before any future getline call.
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    cout << "Are you currently enrolled? (y/n): ";
    cin >> enrolledAnswer;
    const bool isEnrolled = (enrolledAnswer == 'y' || enrolledAnswer == 'Y');

    cout << "\n--- Student Summary ---\n";
    cout << "Name: " << fullName << '\n';
    cout << "Age: " << age << '\n';
    cout << "GPA: " << gpa << '\n';
    cout << "Enrolled: " << (isEnrolled ? "true" : "false") << '\n';

    return 0;
}
