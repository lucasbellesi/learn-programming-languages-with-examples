// This example demonstrates maps and frequency counting concepts.

#include <iostream>
#include <map>
#include <string>
using namespace std;


int main() {
    string text = "banana bandana";
    map<char, int> frequencies;

    for (char ch : text) {
        if (ch == ' ') {
            continue;
        }
        ++frequencies[ch];
    }

    cout << "Character frequencies:\n";
    for (const auto& entry : frequencies) {
        cout << entry.first << " -> " << entry.second << '\n';
    }

    return 0;
}
