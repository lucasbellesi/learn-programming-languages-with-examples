/*
Exercise Guide: languages/cpp/02-core/maps-and-frequency-counting/exercises/01.cpp
Goal: Solve the task defined in this module's README Exercise Specs.
Build: g++ -std=c++17 -Wall -Wextra -pedantic languages/cpp/02-core/maps-and-frequency-counting/exercises/01.cpp -o 01_exercise
Run: ./01_exercise (Windows MSYS2: ./01_exercise.exe)
Sample Input: Use one of the sample cases from the module README Exercise Specs.
Expected Output: Follow the exact output rules described in the same exercise spec.
*/
#include <iostream>
#include <map>
using namespace std;


int main() {
    int n = 0;
    cout << "How many digits? ";
    cin >> n;

    if (n <= 0) {
        cout << "Please enter a positive count.\n";
        return 0;
    }

    map<int, int> frequency;
    for (int digit = 0; digit <= 9; ++digit) {
        frequency[digit] = 0;
    }

    for (int i = 0; i < n; ++i) {
        int value = 0;
        cin >> value;
        if (value >= 0 && value <= 9) {
            ++frequency[value];
        }
    }

    for (int digit = 0; digit <= 9; ++digit) {
        cout << digit << " -> " << frequency[digit] << '\n';
    }

    return 0;
}
