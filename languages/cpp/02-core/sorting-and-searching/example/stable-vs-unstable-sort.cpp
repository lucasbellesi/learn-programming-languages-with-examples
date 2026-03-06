#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

struct Record {
    int score;
    string name;
};

void printRecords(const vector<Record>& records, const string& title) {
    cout << title << '\n';
    for (const Record& record : records) {
        cout << "- score=" << record.score << ", name=" << record.name << '\n';
    }
    cout << '\n';
}

int main() {
    vector<Record> records = {
        {90, "Ana"},
        {75, "Bob"},
        {90, "Carla"},
        {75, "Diego"},
        {90, "Emma"}
    };

    printRecords(records, "Original order:");

    vector<Record> unstable = records;
    sort(unstable.begin(), unstable.end(), [](const Record& a, const Record& b) {
        return a.score < b.score;
    });
    printRecords(unstable, "After std::sort (not guaranteed stable):");

    vector<Record> stable = records;
    stable_sort(stable.begin(), stable.end(), [](const Record& a, const Record& b) {
        return a.score < b.score;
    });
    printRecords(stable, "After std::stable_sort:");

    cout << "Notice how records with equal scores keep relative order with stable_sort.\n";
    return 0;
}
