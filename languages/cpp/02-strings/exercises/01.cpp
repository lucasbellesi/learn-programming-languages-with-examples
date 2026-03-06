#include <iostream>
#include <string>

int main() {
    std::string sentence;
    std::cout << "Enter a sentence: ";
    std::getline(std::cin, sentence);

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

    std::cout << "Word count: " << wordCount << '\n';
    return 0;
}
