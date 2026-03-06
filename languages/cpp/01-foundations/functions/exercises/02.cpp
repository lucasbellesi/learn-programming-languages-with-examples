#include <cctype>
#include <iostream>
#include <limits>
#include <string>
using namespace std;


int countVowels(const string& text) {
    int count = 0;
    for (char ch : text) {
        const char lower = static_cast<char>(tolower(static_cast<unsigned char>(ch)));
        if (lower == 'a' || lower == 'e' || lower == 'i' || lower == 'o' || lower == 'u') {
            ++count;
        }
    }
    return count;
}

int main() {
    string line;

    cout << "Enter a line of text: ";
    getline(cin, line);

    // In case this file is run right after formatted extraction in some environments.
    if (line.empty() && cin.good()) {
        cin.clear();
        cin.ignore(numeric_limits<streamsize>::max(), '\n');
        getline(cin, line);
    }

    cout << "Number of vowels: " << countVowels(line) << '\n';
    return 0;
}
