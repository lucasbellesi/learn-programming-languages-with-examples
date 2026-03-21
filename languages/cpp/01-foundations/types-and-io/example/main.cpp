// Example purpose: show the module flow with clear, beginner-friendly steps.

#include <iostream>
#include <limits>
#include <string>
using namespace std;


int main() {
    // Program flow: collect input, apply core logic, then print a verifiable result.
    string fullName;
    int age = 0;
    double gpa = 0.0;
    char enrolledAnswer = 'n';

    // Intent: print intermediate or final output for quick behavior verification.
    cout << "Enter your full name: ";
    // Intent: gather typed input first so later operations are predictable.
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
