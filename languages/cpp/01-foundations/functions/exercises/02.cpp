#include <cctype>
#include <iostream>
#include <limits>
#include <string>

int countVowels(const std::string& text) {
    int count = 0;
    for (char ch : text) {
        const char lower = static_cast<char>(std::tolower(static_cast<unsigned char>(ch)));
        if (lower == 'a' || lower == 'e' || lower == 'i' || lower == 'o' || lower == 'u') {
            ++count;
        }
    }
    return count;
}

int main() {
    std::string line;

    std::cout << "Enter a line of text: ";
    std::getline(std::cin, line);

    // In case this file is run right after formatted extraction in some environments.
    if (line.empty() && std::cin.good()) {
        std::cin.clear();
        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
        std::getline(std::cin, line);
    }

    std::cout << "Number of vowels: " << countVowels(line) << '\n';
    return 0;
}
