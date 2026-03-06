#include <iostream>
#include <map>
#include <string>

int main() {
    std::string text = "banana bandana";
    std::map<char, int> frequencies;

    for (char ch : text) {
        if (ch == ' ') {
            continue;
        }
        ++frequencies[ch];
    }

    std::cout << "Character frequencies:\n";
    for (const auto& entry : frequencies) {
        std::cout << entry.first << " -> " << entry.second << '\n';
    }

    return 0;
}
