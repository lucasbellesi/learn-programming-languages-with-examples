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

    int minValue = values[0];
    int maxValue = values[0];
    int evenCount = 0;

    for (int value : values) {
        if (value < minValue) {
            minValue = value;
        }
        if (value > maxValue) {
            maxValue = value;
        }
        if (value % 2 == 0) {
            ++evenCount;
        }
    }

    cout << "Minimum: " << minValue << '\n';
    cout << "Maximum: " << maxValue << '\n';
    cout << "Even numbers: " << evenCount << '\n';
    return 0;
}
