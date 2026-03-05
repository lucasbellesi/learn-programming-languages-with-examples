#include <iostream>
#include <limits>
#include <string>

int main() {
    std::string fullName;
    int age = 0;
    double gpa = 0.0;
    char enrolledAnswer = 'n';

    std::cout << "Enter your full name: ";
    std::getline(std::cin, fullName);

    std::cout << "Enter your age: ";
    std::cin >> age;

    std::cout << "Enter your GPA: ";
    std::cin >> gpa;

    // Clear the leftover newline before any future getline call.
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');

    std::cout << "Are you currently enrolled? (y/n): ";
    std::cin >> enrolledAnswer;
    const bool isEnrolled = (enrolledAnswer == 'y' || enrolledAnswer == 'Y');

    std::cout << "\n--- Student Summary ---\n";
    std::cout << "Name: " << fullName << '\n';
    std::cout << "Age: " << age << '\n';
    std::cout << "GPA: " << gpa << '\n';
    std::cout << "Enrolled: " << (isEnrolled ? "true" : "false") << '\n';

    return 0;
}
