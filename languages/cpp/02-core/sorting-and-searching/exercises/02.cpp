#include <iostream>
#include <vector>
using namespace std;


int main() {
    int n = 0;
    cout << "How many sorted values? ";
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

    int target = 0;
    cout << "Target: ";
    cin >> target;

    int left = 0;
    int right = n - 1;
    int index = -1;

    while (left <= right) {
        const int mid = left + (right - left) / 2;
        const int midValue = values[static_cast<size_t>(mid)];

        if (midValue == target) {
            index = mid;
            break;
        }

        if (midValue < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }

    cout << "Index: " << index << '\n';
    return 0;
}
