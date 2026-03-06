#include <iostream>
#include <vector>
using namespace std;


int main() {
    int n = 0;
    cout << "How many integers? ";
    cin >> n;

    if (n <= 0) {
        cout << "Please enter a positive count.\n";
        return 0;
    }

    vector<int> values;
    values.reserve(static_cast<size_t>(n));

    for (int i = 0; i < n; ++i) {
        int value = 0;
        cout << "Value " << (i + 1) << ": ";
        cin >> value;
        values.push_back(value);
    }

    int target = 0;
    cout << "Target to find: ";
    cin >> target;

    int index = -1;
    for (int i = 0; i < n; ++i) {
        if (values[static_cast<size_t>(i)] == target) {
            index = i;
            break;
        }
    }

    cout << "First index: " << index << '\n';
    return 0;
}
