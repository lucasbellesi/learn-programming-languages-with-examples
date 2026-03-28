/*
Exercise Guide: languages/cpp/02-core/input-validation/exercises/01.cpp
Goal: Solve the task
 * defined in this module's README Exercise Specs.
Build: g++ -std=c++17 -Wall -Wextra -pedantic
 * languages/cpp/02-core/input-validation/exercises/01.cpp -o 01_exercise
Run: ./01_exercise
 * (Windows MSYS2: ./01_exercise.exe)
Sample Input: Use one of the sample cases from the module
 * README Exercise Specs.
Expected Output: Follow the exact output rules described in the same
 * exercise spec.
*/
#include <iostream>
#include <limits>
using namespace std;

int main() {
    int value = 0;

    while (true) {
        cout << "Enter an integer from 1 to 100: ";
        if (!(cin >> value)) {
            cout << "Invalid input. Please enter an integer.\n";
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
            continue;
        }

        if (value < 1 || value > 100) {
            cout << "Out of range. Try again.\n";
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
            continue;
        }

        break;
    }

    cout << "Square: " << (value * value) << '\n';
    return 0;
}
