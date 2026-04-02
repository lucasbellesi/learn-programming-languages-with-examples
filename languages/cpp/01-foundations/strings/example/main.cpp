// This example shows cleaning and combining text while preserving readable string logic.
// In C++, the example keeps value flow, references, and explicit control visible.

#include <cctype>
#include <iostream>
#include <limits>
#include <string>
using namespace std;

// Run one deterministic scenario so the console output makes cleaning and combining text while
// preserving readable string logic easy to verify.
int main() {
    // Build the sample state first, then let the later output confirm the behavior step by step.
    int year = 0;
    string fullName;
    string sentence;

    // Print the observed state here so learners can connect the code path to a concrete result.
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
