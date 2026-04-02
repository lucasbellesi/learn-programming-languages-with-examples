// Module focus: Cleaning and combining text while preserving readable string logic.
// Why it matters: practicing strings patterns makes exercises and checkpoints easier to reason
// about.

#include <cctype>
#include <iostream>
#include <limits>
#include <string>
using namespace std;

// Walk through one fixed scenario so strings behavior stays repeatable.
int main() {
    // Prepare sample inputs that exercise the key strings path.
    int year = 0;
    string fullName;
    string sentence;

    // Report values so learners can verify the strings outcome.
    cout << "Enter your birth year: ";
    cin >> year;

    // Clear leftover newline before getline.
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    cout << "Enter your full name: ";
    getline(cin, fullName);

    cout << "Write a short sentence: ";
    getline(cin, sentence);

    const string greeting = "Hello, " + fullName + "!";
    cout << '\n' << greeting << '\n';
    cout << "Birth year: " << year << '\n';
    cout << "Sentence length: " << sentence.size() << '\n';

    const size_t spacePos = sentence.find(' ');
    if (spacePos != string::npos) {
        const string firstWord = sentence.substr(0, spacePos);
        cout << "First word: " << firstWord << '\n';
    } else {
        cout << "Your sentence has only one word.\n";
    }

    int vowelCount = 0;
    for (char ch : sentence) {
        const char lower = static_cast<char>(tolower(static_cast<unsigned char>(ch)));
        if (lower == 'a' || lower == 'e' || lower == 'i' || lower == 'o' || lower == 'u') {
            ++vowelCount;
        }
    }
    cout << "Vowel count: " << vowelCount << '\n';

    return 0;
}
