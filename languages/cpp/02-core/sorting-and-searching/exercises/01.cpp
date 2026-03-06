#include <iostream>
#include <vector>
using namespace std;


int main() {
    int n = 0;
    cout << "How many numbers? ";
    cin >> n;

    if (n <= 0) {
        cout << "Please enter a positive count.\n";
        return 0;
    }

    vector<int> values;
    values.reserve(static_cast<size_t>(n));

    for (int i = 0; i < n; ++i) {
        int value = 0;
        cin >> value;
        values.push_back(value);
    }

    for (int i = 0; i < n - 1; ++i) {
        int minIndex = i;
        for (int j = i + 1; j < n; ++j) {
            if (values[static_cast<size_t>(j)] < values[static_cast<size_t>(minIndex)]) {
                minIndex = j;
            }
        }

        const int temp = values[static_cast<size_t>(i)];
        values[static_cast<size_t>(i)] = values[static_cast<size_t>(minIndex)];
        values[static_cast<size_t>(minIndex)] = temp;
    }

    for (int value : values) {
        cout << value << ' ';
    }
    cout << '\n';

    return 0;
}
