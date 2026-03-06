/*
Exercise Guide: languages/cpp/02-core/sorting-and-searching/exercises/01.cpp
Goal: Solve the task defined in this module's README Exercise Specs.
Build: g++ -std=c++17 -Wall -Wextra -pedantic languages/cpp/02-core/sorting-and-searching/exercises/01.cpp -o 01_exercise
Run: ./01_exercise (Windows MSYS2: ./01_exercise.exe)
Sample Input: Use one of the sample cases from the module README Exercise Specs.
Expected Output: Follow the exact output rules described in the same exercise spec.
*/
#include <iostream>
#include <vector>
using namespace std;


int main() {
    int n = 0;
    cout << "How many numbers? ";
    cin >> n;

    if (n <= 0) {
        cout << "Please enter a positive count.\n";
        return 0;
    }

    vector<int> values;
    values.reserve(static_cast<size_t>(n));

    for (int i = 0; i < n; ++i) {
        int value = 0;
        cin >> value;
        values.push_back(value);
    }

    for (int i = 0; i < n - 1; ++i) {
        int minIndex = i;
        for (int j = i + 1; j < n; ++j) {
            if (values[static_cast<size_t>(j)] < values[static_cast<size_t>(minIndex)]) {
                minIndex = j;
            }
        }

        const int temp = values[static_cast<size_t>(i)];
        values[static_cast<size_t>(i)] = values[static_cast<size_t>(minIndex)];
        values[static_cast<size_t>(minIndex)] = temp;
    }

    for (int value : values) {
        cout << value << ' ';
    }
    cout << '\n';

    return 0;
}
