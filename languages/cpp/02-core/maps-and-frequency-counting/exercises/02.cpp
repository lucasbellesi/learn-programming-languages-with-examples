#include <iostream>
#include <map>
#include <string>
using namespace std;


int main() {
    string text;
    cout << "Enter text: ";
    getline(cin, text);

    map<char, int> frequency;
    for (char ch : text) {
        ++frequency[ch];
    }

    char result = '\0';
    for (char ch : text) {
        if (frequency[ch] == 1) {
            result = ch;
            break;
        }
    }

    if (result == '\0') {
        cout << "No non-repeating character found.\n";
    } else {
        cout << "First non-repeating character: " << result << '\n';
    }

    return 0;
}
