/*
Exercise Guide: languages/cpp/01-foundations/functions/exercises/01.cpp
Goal: Solve the task
 * defined in this module's README Exercise Specs.
Build: g++ -std=c++17 -Wall -Wextra -pedantic
 * languages/cpp/01-foundations/functions/exercises/01.cpp -o 01_exercise
Run: ./01_exercise
 * (Windows MSYS2: ./01_exercise.exe)
Sample Input: Use one of the sample cases from the module
 * README Exercise Specs.
Expected Output: Follow the exact output rules described in the same
 * exercise spec.
*/
#include <iostream>
using namespace std;

int maxOfThree(int a, int b, int c) {
    int currentMax = a;
    if (b > currentMax) {
        currentMax = b;
    }
    if (c > currentMax) {
        currentMax = c;
    }
    return currentMax;
}

int main() {
    int x = 0;
    int y = 0;
    int z = 0;

    cout << "Enter three integers: ";
    cin >> x >> y >> z;

    cout << "Maximum: " << maxOfThree(x, y, z) << '\n';
    return 0;
}
