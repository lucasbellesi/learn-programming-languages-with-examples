// This example demonstrates maps and frequency counting concepts.
// Example purpose: show the module flow with clear, beginner-friendly steps.

#include <iostream>
#include <map>
#include <string>
using namespace std;


int main() {
    // Program flow: collect input, apply core logic, then print a verifiable result.
    string text = "banana bandana";
    map<char, int> frequencies;

    // Intent: iterate through data in a clear and deterministic order.
    for (char ch : text) {
        // Intent: guard invalid or edge-case paths before the main path continues.
        if (ch == ' ') {
            continue;
        }
        ++frequencies[ch];
    }

    // Intent: print intermediate or final output for quick behavior verification.
    cout << "Character frequencies:\n";
    for (const auto& entry : frequencies) {
        cout << entry.first << " -> " << entry.second << '\n';
    }

    return 0;
}
