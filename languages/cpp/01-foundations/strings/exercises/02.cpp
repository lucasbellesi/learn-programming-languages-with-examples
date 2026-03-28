/*
Exercise Guide: languages/cpp/01-foundations/strings/exercises/02.cpp
Goal: Solve the task
 * defined in this module's README Exercise Specs.
Build: g++ -std=c++17 -Wall -Wextra -pedantic
 * languages/cpp/01-foundations/strings/exercises/02.cpp -o 02_exercise
Run: ./02_exercise (Windows
 * MSYS2: ./02_exercise.exe)
Sample Input: Use one of the sample cases from the module README
 * Exercise Specs.
Expected Output: Follow the exact output rules described in the same exercise
 * spec.
*/
#include <cctype>
#include <iostream>
#include <string>
using namespace std;

bool isPalindromeIgnoringNonLetters(const string& text) {
    size_t left = 0;
    size_t right = text.size();

    while (left < right) {
        while (left < right && !isalpha(static_cast<unsigned char>(text[left]))) {
            ++left;
        }
        while (left < right && !isalpha(static_cast<unsigned char>(text[right - 1]))) {
            --right;
        }

        if (left >= right) {
            break;
        }

        const char leftChar = static_cast<char>(tolower(static_cast<unsigned char>(text[left])));
        const char rightChar =
            static_cast<char>(tolower(static_cast<unsigned char>(text[right - 1])));

        if (leftChar != rightChar) {
            return false;
        }

        ++left;
        --right;
    }

    return true;
}

int main() {
    string text;
    cout << "Enter text: ";
    getline(cin, text);

    if (isPalindromeIgnoringNonLetters(text)) {
        cout << "Palindrome: true\n";
    } else {
        cout << "Palindrome: false\n";
    }

    return 0;
}
