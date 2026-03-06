#include <iostream>
#include <limits>
#include <string>

using namespace std;

int main() {
    string fullName;
    int age = 0;

    cout << "Enter your full name: ";
    getline(cin, fullName);

    while (true) {
        cout << "Enter your age (1-120): ";
        if (!(cin >> age)) {
            cout << "Invalid input. Please enter a number.\n";
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
            continue;
        }

        if (age < 1 || age > 120) {
            cout << "Age must be between 1 and 120.\n";
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
            continue;
        }

        cin.ignore(numeric_limits<streamsize>::max(), '\n');
        break;
    }

    cout << "\nRegistration summary:\n";
    cout << "Name: " << fullName << '\n';
    cout << "Age: " << age << '\n';

    return 0;
}
