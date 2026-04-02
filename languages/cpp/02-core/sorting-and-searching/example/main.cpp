// This example shows reordering data and locating values with deliberate search logic.
// In C++, the example keeps value flow, references, and explicit control visible.

#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

// Run one deterministic scenario so the console output makes reordering data and locating values
// with deliberate search logic easy to verify.
int main() {
    // Build the sample state first, then let the later output confirm the behavior step by step.
    vector<int> values{7, 2, 9, 4, 2, 8};

    sort(values.begin(), values.end());

    // Print the observed state here so learners can connect the code path to a concrete result.
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
