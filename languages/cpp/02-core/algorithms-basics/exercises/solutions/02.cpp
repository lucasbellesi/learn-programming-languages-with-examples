/*
Exercise Guide: languages/cpp/02-core/algorithms-basics/exercises/02.cpp
Goal: Solve the task
 * defined in this module's README Exercise Specs.
Build: g++ -std=c++17 -Wall -Wextra -pedantic
 * languages/cpp/02-core/algorithms-basics/exercises/02.cpp -o 02_exercise
Run: ./02_exercise
 * (Windows MSYS2: ./02_exercise.exe)
Sample Input: Use one of the sample cases from the module
 * README Exercise Specs.
Expected Output: Follow the exact output rules described in the same
 * exercise spec.
*/
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n = 0;
    cout << "How many integers? ";
    cin >> n;

    if (n <= 0) {
        cout << "Please enter a positive count.\n";
        return 0;
    }

    vector<int> values;
    values.reserve(static_cast<size_t>(n));

    for (int i = 0; i < n; ++i) {
        int value = 0;
        cout << "Value " << (i + 1) << ": ";
        cin >> value;
        values.push_back(value);
    }

    int minValue = values[0];
    int maxValue = values[0];
    int evenCount = 0;

    for (int value : values) {
        if (value < minValue) {
            minValue = value;
        }
        if (value > maxValue) {
            maxValue = value;
        }
        if (value % 2 == 0) {
            ++evenCount;
        }
    }

    cout << "Minimum: " << minValue << '\n';
    cout << "Maximum: " << maxValue << '\n';
    cout << "Even numbers: " << evenCount << '\n';
    return 0;
}
