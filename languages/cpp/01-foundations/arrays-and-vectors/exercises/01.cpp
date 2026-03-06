/*
Exercise Guide: languages/cpp/01-foundations/arrays-and-vectors/exercises/01.cpp
Goal: Solve the task defined in this module's README Exercise Specs.
Build: g++ -std=c++17 -Wall -Wextra -pedantic languages/cpp/01-foundations/arrays-and-vectors/exercises/01.cpp -o 01_exercise
Run: ./01_exercise (Windows MSYS2: ./01_exercise.exe)
Sample Input: Use one of the sample cases from the module README Exercise Specs.
Expected Output: Follow the exact output rules described in the same exercise spec.
*/
#include <iostream>
#include <vector>
using namespace std;


int main() {
    int n = 0;
    cout << "How many integers? ";
    cin >> n;

    if (n <= 0) {
        cout << "Please enter a positive number.\n";
        return 0;
    }

    vector<int> values;
    values.reserve(static_cast<size_t>(n));

    for (int i = 0; i < n; ++i) {
        int current = 0;
        cout << "Value " << (i + 1) << ": ";
        cin >> current;
        values.push_back(current);
    }

    cout << "Reversed order: ";
    for (int i = n - 1; i >= 0; --i) {
        cout << values[static_cast<size_t>(i)];
        if (i > 0) {
            cout << ' ';
        }
    }
    cout << '\n';

    return 0;
}
