/*
Exercise Guide: languages/cpp/02-core/maps-and-frequency-counting/exercises/02.cpp
Goal: Solve the task defined in this module's README Exercise Specs.
Build: g++ -std=c++17 -Wall -Wextra -pedantic languages/cpp/02-core/maps-and-frequency-counting/exercises/02.cpp -o 02_exercise
Run: ./02_exercise (Windows MSYS2: ./02_exercise.exe)
Sample Input: Use one of the sample cases from the module README Exercise Specs.
Expected Output: Follow the exact output rules described in the same exercise spec.
*/
#include <iostream>
#include <map>
#include <string>
using namespace std;


int main() {
    string text;
    cout << "Enter text: ";
    getline(cin, text);

    map<char, int> frequency;
    for (char ch : text) {
        ++frequency[ch];
    }

    char result = '\0';
    for (char ch : text) {
        if (frequency[ch] == 1) {
            result = ch;
            break;
        }
    }

    if (result == '\0') {
        cout << "No non-repeating character found.\n";
    } else {
        cout << "First non-repeating character: " << result << '\n';
    }

    return 0;
}
