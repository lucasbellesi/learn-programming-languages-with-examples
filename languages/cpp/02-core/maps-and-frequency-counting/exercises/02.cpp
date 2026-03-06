#include <iostream>
#include <map>
#include <string>

int main() {
    std::string text;
    std::cout << "Enter text: ";
    std::getline(std::cin, text);

    std::map<char, int> frequency;
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
        std::cout << "No non-repeating character found.\n";
    } else {
        std::cout << "First non-repeating character: " << result << '\n';
    }

    return 0;
}
