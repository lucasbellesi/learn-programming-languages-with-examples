#include <cctype>
#include <iostream>
#include <string>
using namespace std;


bool isPalindromeIgnoringNonLetters(const string& text) {
    size_t left = 0;
    size_t right = text.size();

    while (left < right) {
        while (left < right &&
               !isalpha(static_cast<unsigned char>(text[left]))) {
            ++left;
        }
        while (left < right &&
               !isalpha(static_cast<unsigned char>(text[right - 1]))) {
            --right;
        }

        if (left >= right) {
            break;
        }

        const char leftChar =
            static_cast<char>(tolower(static_cast<unsigned char>(text[left])));
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
