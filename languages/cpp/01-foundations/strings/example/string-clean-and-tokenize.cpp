#include <cctype>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
    string line;
    cout << "Enter a sentence: ";
    getline(cin, line);

    string cleaned;
    cleaned.reserve(line.size());
    for (char ch : line) {
        if (isalnum(static_cast<unsigned char>(ch))) {
            cleaned.push_back(static_cast<char>(tolower(static_cast<unsigned char>(ch))));
        } else {
            cleaned.push_back(' ');
        }
    }

    vector<string> words;
    string currentWord;
    for (char ch : cleaned) {
        if (ch == ' ') {
            if (!currentWord.empty()) {
                words.push_back(currentWord);
                currentWord.clear();
            }
        } else {
            currentWord.push_back(ch);
        }
    }
    if (!currentWord.empty()) {
        words.push_back(currentWord);
    }

    cout << "Normalized text: " << cleaned << '\n';
    cout << "Tokens (" << words.size() << "):\n";
    for (const string& word : words) {
        cout << "- " << word << '\n';
    }

    return 0;
}
