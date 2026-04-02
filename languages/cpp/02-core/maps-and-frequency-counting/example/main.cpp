// Module focus: Counting repeated values and summarizing them through keyed lookups.
// Why it matters: practicing maps and frequency counting patterns makes exercises and checkpoints
// easier to reason about.

#include <iostream>
#include <map>
#include <string>
using namespace std;

// Walk through one fixed scenario so maps and frequency counting behavior stays repeatable.
int main() {
    // Prepare sample inputs that exercise the key maps and frequency counting path.
    string text = "banana bandana";
    map<char, int> frequencies;

    for (char ch : text) {
        if (ch == ' ') {
            continue;
        }
        ++frequencies[ch];
    }

    // Report values so learners can verify the maps and frequency counting outcome.
    cout << "Character frequencies:\n";
    for (const auto& entry : frequencies) {
        cout << entry.first << " -> " << entry.second << '\n';
    }

    return 0;
}
