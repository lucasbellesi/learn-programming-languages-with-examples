// Module focus: Reading typed input carefully and turning raw text into values.
// Why it matters: the example makes it possible to choose suitable primitive values and variables
// for a small problem before the learner tackles the exercises.
// about.

#include <iostream>
#include <limits>
#include <string>
using namespace std;

// Fixed inputs make the consequence of mixing `cin >>` and `getline` without clearing newline
// visible and repeatable.
int main() {
    // These values exercise the normal path before the exercises vary the documented boundaries.
    string fullName;
    int age = 0;
    double gpa = 0.0;
    char enrolledAnswer = 'n';

    // The printed result shows whether the program can read, validate, transform, and present
    // console data.
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
