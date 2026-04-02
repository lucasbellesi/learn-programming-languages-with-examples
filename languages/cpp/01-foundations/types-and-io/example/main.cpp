// Module focus: Reading typed input carefully and turning raw text into values.
// Why it matters: practicing types and io patterns makes exercises and checkpoints easier to reason
// about.

#include <iostream>
#include <limits>
#include <string>
using namespace std;

// Walk through one fixed scenario so types and io behavior stays repeatable.
int main() {
    // Prepare sample inputs that exercise the key types and io path.
    string fullName;
    int age = 0;
    double gpa = 0.0;
    char enrolledAnswer = 'n';

    // Report values so learners can verify the types and io outcome.
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
