// Module focus: Reordering data and locating values with deliberate search logic.
// Why it matters: the example makes it possible to choose and apply sorting and searching
// operations correctly before the learner tackles the exercises.

#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

// Fixed inputs make the consequence of running binary search on unsorted data visible and
// repeatable.
int main() {
    // These values exercise the normal path before the exercises vary the documented boundaries.
    vector<int> values{7, 2, 9, 4, 2, 8};

    sort(values.begin(), values.end());

    // The printed result shows whether the program can explain ordering, duplicates, missing
    // values, and stability tradeoffs.
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
