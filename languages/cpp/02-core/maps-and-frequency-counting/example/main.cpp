// This example shows counting repeated values and summarizing them through keyed lookups.
// In C++, the example keeps value flow, references, and explicit control visible.

#include <iostream>
#include <map>
#include <string>
using namespace std;

// Run one deterministic scenario so the console output makes counting repeated values and
// summarizing them through keyed lookups easy to verify.
int main() {
    // Build the sample state first, then let the later output confirm the behavior step by step.
    string text = "banana bandana";
    map<char, int> frequencies;

    for (char ch : text) {
        if (ch == ' ') {
            continue;
        }
        ++frequencies[ch];
    }

    // Print the observed state here so learners can connect the code path to a concrete result.
    cout << "Character frequencies:\n";
    for (const auto& entry : frequencies) {
        cout << entry.first << " -> " << entry.second << '\n';
    }

    return 0;
}
