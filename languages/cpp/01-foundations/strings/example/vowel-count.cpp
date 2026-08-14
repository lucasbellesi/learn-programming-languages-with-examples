#include <cctype>
#include <iostream>
#include <string>

int main() {
    std::string sentence;
    std::cout << "Write a short sentence: ";
    std::getline(std::cin, sentence);

    int vowelCount = 0;
    for (char character : sentence) {
        // Convert through unsigned char because cctype functions reject negative char values.
        const char lower = static_cast<char>(std::tolower(static_cast<unsigned char>(character)));
        if (lower == 'a' || lower == 'e' || lower == 'i' || lower == 'o' || lower == 'u') {
            ++vowelCount;
        }
    }
    std::cout << "Vowel count: " << vowelCount << '\n';
    return 0;
}
