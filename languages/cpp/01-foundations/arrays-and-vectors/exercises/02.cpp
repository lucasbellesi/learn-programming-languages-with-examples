/*
Exercise Guide: languages/cpp/01-foundations/arrays-and-vectors/exercises/02.cpp
Goal: Solve the task defined in this module's README Exercise Specs.
Build: g++ -std=c++17 -Wall -Wextra -pedantic languages/cpp/01-foundations/arrays-and-vectors/exercises/02.cpp -o 02_exercise
Run: ./02_exercise (Windows MSYS2: ./02_exercise.exe)
Sample Input: Use one of the sample cases from the module README Exercise Specs.
Expected Output: Follow the exact output rules described in the same exercise spec.
*/
#include <iostream>
#include <vector>
using namespace std;


int main() {
    int n = 0;
    cout << "How many integers will you enter? ";
    cin >> n;

    if (n <= 0) {
        cout << "Please enter a positive number.\n";
        return 0;
    }

    vector<int> values;
    values.reserve(static_cast<size_t>(n));

    for (int i = 0; i < n; ++i) {
        int number = 0;
        cout << "Number " << (i + 1) << ": ";
        cin >> number;
        values.push_back(number);
    }

    int target = 0;
    cout << "Enter the number to count: ";
    cin >> target;

    int frequency = 0;
    for (int value : values) {
        if (value == target) {
            ++frequency;
        }
    }

    cout << target << " appears " << frequency << " time(s).\n";
    return 0;
}
