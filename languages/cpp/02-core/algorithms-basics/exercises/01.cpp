/*
Exercise Guide: languages/cpp/02-core/algorithms-basics/exercises/01.cpp
Goal: Solve the task defined in this module's README Exercise Specs.
Build: g++ -std=c++17 -Wall -Wextra -pedantic languages/cpp/02-core/algorithms-basics/exercises/01.cpp -o 01_exercise
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

    int target = 0;
    cout << "Target to find: ";
    cin >> target;

    int index = -1;
    for (int i = 0; i < n; ++i) {
        if (values[static_cast<size_t>(i)] == target) {
            index = i;
            break;
        }
    }

    cout << "First index: " << index << '\n';
    return 0;
}
