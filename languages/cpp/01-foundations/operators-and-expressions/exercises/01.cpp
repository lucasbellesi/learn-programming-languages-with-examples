/*
Exercise Guide: languages/cpp/01-foundations/operators-and-expressions/exercises/01.cpp
Goal: Solve the task defined in this module's README Exercise Specs.
Build: g++ -std=c++17 -Wall -Wextra -pedantic languages/cpp/01-foundations/operators-and-expressions/exercises/01.cpp -o 01_exercise
Run: ./01_exercise (Windows MSYS2: ./01_exercise.exe)
Sample Input: Use one of the sample cases from the module README Exercise Specs.
Expected Output: Follow the exact output rules described in the same exercise spec.
*/
#include <iostream>
using namespace std;


int main() {
    int totalSeconds = 0;
    cout << "Enter total seconds: ";
    cin >> totalSeconds;

    if (totalSeconds < 0) {
        cout << "Please enter a non-negative value.\n";
        return 0;
    }

    const int hours = totalSeconds / 3600;
    const int minutes = (totalSeconds % 3600) / 60;
    const int seconds = totalSeconds % 60;

    cout << "Converted time: " << hours << ":" << minutes << ":" << seconds << '\n';
    return 0;
}
