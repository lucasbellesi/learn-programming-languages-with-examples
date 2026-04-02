// Module focus: Walking data step by step to compute summaries and decisions.
// Why it matters: practicing algorithms basics patterns makes exercises and checkpoints easier to
// reason about.

#include <iostream>
#include <vector>
using namespace std;

// Helper setup for algorithms basics; this keeps the walkthrough readable.
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

// Walk through one fixed scenario so algorithms basics behavior stays repeatable.
int main() {
    // Prepare sample inputs that exercise the key algorithms basics path.
    const vector<int> values{4, 7, 4, 1, 9, 4, 2};
    const int target = 4;

    const int firstIndex = linearSearch(values, target);
    // Report values so learners can verify the algorithms basics outcome.
    cout << "First index of " << target << ": " << firstIndex << '\n';
    cout << "Occurrences of " << target << ": " << countOccurrences(values, target) << '\n';

    printMinMax(values);
    return 0;
}
