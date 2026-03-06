/*
Exercise Guide: languages/cpp/01-foundations/scope-and-lifetime-basics/exercises/01.cpp
Goal: Solve the task defined in this module's README Exercise Specs.
Build: g++ -std=c++17 -Wall -Wextra -pedantic languages/cpp/01-foundations/scope-and-lifetime-basics/exercises/01.cpp -o 01_exercise
Run: ./01_exercise (Windows MSYS2: ./01_exercise.exe)
Sample Input: Use one of the sample cases from the module README Exercise Specs.
Expected Output: Follow the exact output rules described in the same exercise spec.
*/
#include <iostream>
using namespace std;


int main() {
    int score = 0;
    cout << "Enter score (0-100): ";
    cin >> score;

    if (score < 0 || score > 100) {
        cout << "Invalid score.\n";
        return 0;
    }

    char grade = 'F';
    if (score >= 90) {
        grade = 'A';
    } else if (score >= 80) {
        grade = 'B';
    } else if (score >= 70) {
        grade = 'C';
    } else if (score >= 60) {
        grade = 'D';
    }

    cout << "Grade: " << grade << '\n';
    return 0;
}
