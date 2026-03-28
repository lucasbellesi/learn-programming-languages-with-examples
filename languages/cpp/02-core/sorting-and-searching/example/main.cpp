// This example demonstrates sorting and searching concepts.
// Example purpose: show the module flow with clear, beginner-friendly steps.

#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int main() {
    // Program flow: collect input, apply core logic, then print a verifiable result.
    vector<int> values{7, 2, 9, 4, 2, 8};

    sort(values.begin(), values.end());

    // Intent: print intermediate or final output for quick behavior verification.
    cout << "Sorted: ";
    // Intent: iterate through data in a clear and deterministic order.
    for (int value : values) {
        cout << value << ' ';
    }
    cout << '\n';

    const int target = 4;
    auto it = lower_bound(values.begin(), values.end(), target);

    // Intent: guard invalid or edge-case paths before the main path continues.
    if (it != values.end() && *it == target) {
        const size_t index = static_cast<size_t>(it - values.begin());
        cout << "Found " << target << " at index " << index << '\n';
    } else {
        cout << target << " not found\n";
    }

    return 0;
}
