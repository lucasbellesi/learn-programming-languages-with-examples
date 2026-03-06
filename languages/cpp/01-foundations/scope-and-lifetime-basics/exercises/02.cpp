/*
Exercise Guide: languages/cpp/01-foundations/scope-and-lifetime-basics/exercises/02.cpp
Goal: Solve the task defined in this module's README Exercise Specs.
Build: g++ -std=c++17 -Wall -Wextra -pedantic languages/cpp/01-foundations/scope-and-lifetime-basics/exercises/02.cpp -o 02_exercise
Run: ./02_exercise (Windows MSYS2: ./02_exercise.exe)
Sample Input: Use one of the sample cases from the module README Exercise Specs.
Expected Output: Follow the exact output rules described in the same exercise spec.
*/
#include <iostream>
using namespace std;


int main() {
    int n = 0;
    cout << "Enter N: ";
    cin >> n;

    if (n <= 0) {
        cout << "N must be positive.\n";
        return 0;
    }

    int sum = 0;
    {
        for (int i = 1; i <= n; ++i) {
            sum += i;
        }
    }

    cout << "Sum 1.." << n << " = " << sum << '\n';
    return 0;
}
