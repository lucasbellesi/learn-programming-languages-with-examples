/*
Exercise Guide: languages/cpp/01-foundations/strings/exercises/01.cpp
Goal: Solve the task defined in this module's README Exercise Specs.
Build: g++ -std=c++17 -Wall -Wextra -pedantic languages/cpp/01-foundations/strings/exercises/01.cpp -o 01_exercise
Run: ./01_exercise (Windows MSYS2: ./01_exercise.exe)
Sample Input: Use one of the sample cases from the module README Exercise Specs.
Expected Output: Follow the exact output rules described in the same exercise spec.
*/
#include <iostream>
#include <string>
using namespace std;


int main() {
    string sentence;
    cout << "Enter a sentence: ";
    getline(cin, sentence);

    int wordCount = 0;
    bool insideWord = false;

    for (char ch : sentence) {
        if (ch == ' ' || ch == '\t' || ch == '\n') {
            insideWord = false;
        } else if (!insideWord) {
            insideWord = true;
            ++wordCount;
        }
    }

    cout << "Word count: " << wordCount << '\n';
    return 0;
}
