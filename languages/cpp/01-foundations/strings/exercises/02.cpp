#include <cctype>
#include <iostream>
#include <string>

bool isPalindromeIgnoringNonLetters(const std::string& text) {
    std::size_t left = 0;
    std::size_t right = text.size();

    while (left < right) {
        while (left < right &&
               !std::isalpha(static_cast<unsigned char>(text[left]))) {
            ++left;
        }
        while (left < right &&
               !std::isalpha(static_cast<unsigned char>(text[right - 1]))) {
            --right;
        }

        if (left >= right) {
            break;
        }

        const char leftChar =
            static_cast<char>(std::tolower(static_cast<unsigned char>(text[left])));
        const char rightChar =
            static_cast<char>(std::tolower(static_cast<unsigned char>(text[right - 1])));

        if (leftChar != rightChar) {
            return false;
        }

        ++left;
        --right;
    }

    return true;
}

int main() {
    std::string text;
    std::cout << "Enter text: ";
    std::getline(std::cin, text);

    if (isPalindromeIgnoringNonLetters(text)) {
        std::cout << "Palindrome: true\n";
    } else {
        std::cout << "Palindrome: false\n";
    }

    return 0;
}
