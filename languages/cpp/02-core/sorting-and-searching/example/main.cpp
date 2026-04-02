// Module focus: Reordering data and locating values with deliberate search logic.
// Why it matters: practicing sorting and searching patterns makes exercises and checkpoints easier
// to reason about.

#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

// Walk through one fixed scenario so sorting and searching behavior stays repeatable.
int main() {
    // Prepare sample inputs that exercise the key sorting and searching path.
    vector<int> values{7, 2, 9, 4, 2, 8};

    sort(values.begin(), values.end());

    // Report values so learners can verify the sorting and searching outcome.
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
