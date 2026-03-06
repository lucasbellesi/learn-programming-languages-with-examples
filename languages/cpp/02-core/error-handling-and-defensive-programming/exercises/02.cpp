/*
Exercise Guide: languages/cpp/02-core/error-handling-and-defensive-programming/exercises/02.cpp
Goal: Solve the task defined in this module's README Exercise Specs.
Build: g++ -std=c++17 -Wall -Wextra -pedantic languages/cpp/02-core/error-handling-and-defensive-programming/exercises/02.cpp -o 02_exercise
Run: ./02_exercise (Windows MSYS2: ./02_exercise.exe)
Sample Input: Use one of the sample cases from the module README Exercise Specs.
Expected Output: Follow the exact output rules described in the same exercise spec.
*/
#include <iostream>
#include <limits>
using namespace std;


int main() {
    while (true) {
        double a = 0.0;
        double b = 0.0;

        cout << "Enter two numbers to divide (a b): ";
        if (!(cin >> a >> b)) {
            cout << "Invalid input type. Try again.\n";
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
            continue;
        }

        if (b == 0.0) {
            cout << "Divisor cannot be zero. Try again.\n";
            continue;
        }

        cout << "Result: " << (a / b) << '\n';
        break;
    }

    return 0;
}
