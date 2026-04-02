// This helper example focuses on focusing on the frequency summary without repeating the full
// program flow.

#include <algorithm>
#include <iostream>
#include <map>
#include <string>
#include <vector>

using namespace std;

struct FrequencyItem {
    string word;
    int count;
};

int main() {
    int n = 0;
    cout << "How many words? ";
    cin >> n;

    if (n <= 0) {
        cout << "Please enter a positive number.\n";
        return 0;
    }

    map<string, int> frequency;
    for (int i = 0; i < n; ++i) {
        string word;
        cout << "Word " << (i + 1) << ": ";
        cin >> word;
        ++frequency[word];
    }

    int k = 0;
    cout << "How many top words to show? ";
    cin >> k;

    if (k <= 0) {
        cout << "Please enter a positive value for k.\n";
        return 0;
    }

    vector<FrequencyItem> items;
    items.reserve(frequency.size());
    for (const pair<const string, int>& entry : frequency) {
        items.push_back({entry.first, entry.second});
    }

    sort(items.begin(), items.end(), [](const FrequencyItem& a, const FrequencyItem& b) {
        if (a.count != b.count) {
            return a.count > b.count;
        }
        return a.word < b.word;
    });

    if (k > static_cast<int>(items.size())) {
        k = static_cast<int>(items.size());
    }

    cout << "\nTop " << k << " words:\n";
    for (int i = 0; i < k; ++i) {
        cout << (i + 1) << ". " << items[i].word << " -> " << items[i].count << '\n';
    }

    return 0;
}
