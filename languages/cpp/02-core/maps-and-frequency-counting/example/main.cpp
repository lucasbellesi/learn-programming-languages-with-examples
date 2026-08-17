// Module focus: Counting repeated values and summarizing them through keyed lookups.
// Why it matters: the example makes it possible to use key-value collections to aggregate
// and retrieve data before the learner tackles the exercises.

#include <iostream>
#include <map>
#include <string>
using namespace std;

// Fixed inputs make the consequence of forgetting that `map[key]` creates missing keys visible
// and repeatable.
int main() {
    // These values exercise the normal path before the exercises vary the documented boundaries.
    string text = "banana bandana";
    map<char, int> frequencies;

    for (char ch : text) {
        if (ch == ' ') {
            continue;
        }
        ++frequencies[ch];
    }

    // The printed result shows whether the program can define normalization and missing-key
    // behavior explicitly.
    cout << "Character frequencies:\n";
    for (const auto& entry : frequencies) {
        cout << entry.first << " -> " << entry.second << '\n';
    }

    return 0;
}
