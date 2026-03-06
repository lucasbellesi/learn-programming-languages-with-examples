#include <iostream>
#include <string>
using namespace std;


int main() {
    string sentence;
    cout << "Enter a sentence: ";
    getline(cin, sentence);

    int wordCount = 0;
    bool insideWord = false;

    for (char ch : sentence) {
        if (ch == ' ' || ch == '\t' || ch == '\n') {
            insideWord = false;
        } else if (!insideWord) {
            insideWord = true;
            ++wordCount;
        }
    }

    cout << "Word count: " << wordCount << '\n';
    return 0;
}
