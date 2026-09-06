// Read a full line and numeric fields, then print a student summary.
// This first example assumes valid input; input-validation teaches stream recovery.

#include <iostream>
#include <limits>
#include <string>
using namespace std;

int main() {
    // Use separate types for text, whole numbers, decimals, and a yes/no answer.
    string fullName;
    int age = 0;
    double gpa = 0.0;
    char enrolledAnswer = 'n';

    // getline preserves spaces in the name; operator >> extracts the numeric fields.
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

    // Print the typed values; normalize either y or Y to the same boolean label.
    cout << "\n--- Student Summary ---\n";
    cout << "Name: " << fullName << '\n';
    cout << "Age: " << age << '\n';
    cout << "GPA: " << gpa << '\n';
    cout << "Enrolled: " << (isEnrolled ? "true" : "false") << '\n';

    return 0;
}
