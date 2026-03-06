/*
Exercise Guide: languages/cpp/01-foundations/control-flow/exercises/02.cpp
Goal: Solve the task defined in this module's README Exercise Specs.
Build: g++ -std=c++17 -Wall -Wextra -pedantic languages/cpp/01-foundations/control-flow/exercises/02.cpp -o 02_exercise
Run: ./02_exercise (Windows MSYS2: ./02_exercise.exe)
Sample Input: Use one of the sample cases from the module README Exercise Specs.
Expected Output: Follow the exact output rules described in the same exercise spec.
*/
#include <iostream>
using namespace std;


int main() {
    int value = 0;
    int count = 0;
    double sum = 0.0;

    cout << "Enter integers (-1 to stop):\n";
    while (true) {
        cin >> value;

        if (value == -1) {
            break;
        }

        sum += value;
        ++count;
    }

    if (count == 0) {
        cout << "No values were entered before -1.\n";
    } else {
        const double average = sum / count;
        cout << "Average: " << average << '\n';
    }

    return 0;
}
