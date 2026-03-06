#include <cctype>
#include <iostream>
#include <limits>
#include <string>

int main() {
    int year = 0;
    std::string fullName;
    std::string sentence;

    std::cout << "Enter your birth year: ";
    std::cin >> year;

    // Clear leftover newline before getline.
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');

    std::cout << "Enter your full name: ";
    std::getline(std::cin, fullName);

    std::cout << "Write a short sentence: ";
    std::getline(std::cin, sentence);

    const std::string greeting = "Hello, " + fullName + "!";
    std::cout << '\n' << greeting << '\n';
    std::cout << "Birth year: " << year << '\n';
    std::cout << "Sentence length: " << sentence.size() << '\n';

    const std::size_t spacePos = sentence.find(' ');
    if (spacePos != std::string::npos) {
        const std::string firstWord = sentence.substr(0, spacePos);
        std::cout << "First word: " << firstWord << '\n';
    } else {
        std::cout << "Your sentence has only one word.\n";
    }

    int vowelCount = 0;
    for (char ch : sentence) {
        const char lower = static_cast<char>(std::tolower(static_cast<unsigned char>(ch)));
        if (lower == 'a' || lower == 'e' || lower == 'i' || lower == 'o' || lower == 'u') {
            ++vowelCount;
        }
    }
    std::cout << "Vowel count: " << vowelCount << '\n';

    return 0;
}
