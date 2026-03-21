// This example demonstrates algorithms basics concepts.
// Example purpose: show the module flow with clear, beginner-friendly steps.

#include <iostream>
#include <vector>
using namespace std;


int linearSearch(const vector<int>& values, int target) {
    // Intent: iterate through data in a clear and deterministic order.
    for (size_t i = 0; i < values.size(); ++i) {
        // Intent: guard invalid or edge-case paths before the main path continues.
        if (values[i] == target) {
            return static_cast<int>(i);
        }
    }
    return -1;
}

int countOccurrences(const vector<int>& values, int target) {
    int count = 0;
    for (int value : values) {
        if (value == target) {
            ++count;
        }
    }
    return count;
}

void printMinMax(const vector<int>& values) {
    if (values.empty()) {
        // Intent: print intermediate or final output for quick behavior verification.
        cout << "No values to process.\n";
        return;
    }

    int minValue = values[0];
    int maxValue = values[0];
    for (int value : values) {
        if (value < minValue) {
            minValue = value;
        }
        if (value > maxValue) {
            maxValue = value;
        }
    }

    cout << "Minimum: " << minValue << '\n';
    cout << "Maximum: " << maxValue << '\n';
}

int main() {
    // Program flow: collect input, apply core logic, then print a verifiable result.
    const vector<int> values{4, 7, 4, 1, 9, 4, 2};
    const int target = 4;

    const int firstIndex = linearSearch(values, target);
    cout << "First index of " << target << ": " << firstIndex << '\n';
    cout << "Occurrences of " << target << ": " << countOccurrences(values, target) << '\n';

    printMinMax(values);
    return 0;
}
