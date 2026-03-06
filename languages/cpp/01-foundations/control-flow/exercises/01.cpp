/*
Exercise Guide: languages/cpp/01-foundations/control-flow/exercises/01.cpp
Goal: Solve the task defined in this module's README Exercise Specs.
Build: g++ -std=c++17 -Wall -Wextra -pedantic languages/cpp/01-foundations/control-flow/exercises/01.cpp -o 01_exercise
Run: ./01_exercise (Windows MSYS2: ./01_exercise.exe)
Sample Input: Use one of the sample cases from the module README Exercise Specs.
Expected Output: Follow the exact output rules described in the same exercise spec.
*/
#include <iostream>
using namespace std;


int main() {
    int n = 0;
    cout << "Run FizzBuzz up to: ";
    cin >> n;

    for (int i = 1; i <= n; ++i) {
        if (i % 15 == 0) {
            cout << "FizzBuzz";
        } else if (i % 3 == 0) {
            cout << "Fizz";
        } else if (i % 5 == 0) {
            cout << "Buzz";
        } else {
            cout << i;
        }

        if (i < n) {
            cout << '\n';
        }
    }

    cout << '\n';
    return 0;
}
