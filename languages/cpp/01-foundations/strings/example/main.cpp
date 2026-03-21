// Example purpose: show the module flow with clear, beginner-friendly steps.

#include <cctype>
#include <iostream>
#include <limits>
#include <string>
using namespace std;


int main() {
    // Program flow: collect input, apply core logic, then print a verifiable result.
    int year = 0;
    string fullName;
    string sentence;

    // Intent: print intermediate or final output for quick behavior verification.
    cout << "Enter your birth year: ";
    // Intent: gather typed input first so later operations are predictable.
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
    // Intent: guard invalid or edge-case paths before the main path continues.
    if (spacePos != string::npos) {
        const string firstWord = sentence.substr(0, spacePos);
        cout << "First word: " << firstWord << '\n';
    } else {
        cout << "Your sentence has only one word.\n";
    }

    int vowelCount = 0;
    // Intent: iterate through data in a clear and deterministic order.
    for (char ch : sentence) {
        const char lower = static_cast<char>(tolower(static_cast<unsigned char>(ch)));
        if (lower == 'a' || lower == 'e' || lower == 'i' || lower == 'o' || lower == 'u') {
            ++vowelCount;
        }
    }
    cout << "Vowel count: " << vowelCount << '\n';

    return 0;
}
