#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;


int main() {
    vector<int> values{7, 2, 9, 4, 2, 8};

    sort(values.begin(), values.end());

    cout << "Sorted: ";
    for (int value : values) {
        cout << value << ' ';
    }
    cout << '\n';

    const int target = 4;
    auto it = lower_bound(values.begin(), values.end(), target);

    if (it != values.end() && *it == target) {
        const size_t index = static_cast<size_t>(it - values.begin());
        cout << "Found " << target << " at index " << index << '\n';
    } else {
        cout << target << " not found\n";
    }

    return 0;
}
