#include <iostream>
#include <string>
#include <utility>
#include <vector>
using namespace std;

int main() {
    int n = 0;
    cout << "How many strings? ";
    cin >> n;

    if (n <= 0) {
        cout << "Please enter a positive count.\n";
        return 0;
    }

    vector<string> values;
    values.reserve(static_cast<size_t>(n));

    for (int i = 0; i < n; ++i) {
        string temp;
        cout << "String " << (i + 1) << ": ";
        cin >> temp;
        values.push_back(move(temp));
        cout << "Current size: " << values.size() << ", capacity: " << values.capacity() << '\n';
    }

    return 0;
}
