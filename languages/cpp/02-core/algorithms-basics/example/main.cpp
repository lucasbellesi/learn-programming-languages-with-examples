// This example shows walking data step by step to compute summaries and decisions.
// In C++, the example keeps value flow, references, and explicit control visible.

#include <iostream>
#include <vector>
using namespace std;

// Define the reusable pieces first so the main flow can focus on one observable scenario.
int linearSearch(const vector<int>& values, int target) {
    for (size_t i = 0; i < values.size(); ++i) {
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

// Run one deterministic scenario so the console output makes walking data step by step to compute
// summaries and decisions easy to verify.
int main() {
    // Build the sample state first, then let the later output confirm the behavior step by step.
    const vector<int> values{4, 7, 4, 1, 9, 4, 2};
    const int target = 4;

    const int firstIndex = linearSearch(values, target);
    // Print the observed state here so learners can connect the code path to a concrete result.
    cout << "First index of " << target << ": " << firstIndex << '\n';
    cout << "Occurrences of " << target << ": " << countOccurrences(values, target) << '\n';

    printMinMax(values);
    return 0;
}
