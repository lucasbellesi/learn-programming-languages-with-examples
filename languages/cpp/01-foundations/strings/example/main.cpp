// Module focus: Cleaning and combining text while preserving readable string logic.
// Why it matters: the example makes it possible to normalize, inspect, and transform textual data
// before the learner tackles the exercises.
// about.

#include <iostream>
#include <limits>
#include <string>
using namespace std;

// Fixed inputs make the consequence of forgetting to clear newline before `getline` visible and
// repeatable.
int main() {
    // These values exercise the normal path before the exercises vary the documented boundaries.
    int year = 0;
    string fullName;
    string sentence;

    // The printed result shows whether the program can handle empty input and character
    // boundaries safely.
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

    return 0;
}
