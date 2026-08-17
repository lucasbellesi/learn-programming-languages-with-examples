// Module focus: Walking data step by step to compute summaries and decisions.
// Why it matters: the example makes it possible to implement linear scans and accumulations with
// clear invariants before the learner tackles the exercises.

#include <iostream>
#include <vector>
using namespace std;

// Separate helpers keep the main path focused on how to implement linear scans and accumulations
// with clear invariants.
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

// Fixed inputs make the consequence of forgetting to handle empty input visible and repeatable.
int main() {
    // These values exercise the normal path before the exercises vary the documented boundaries.
    const vector<int> values{4, 7, 4, 1, 9, 4, 2};
    const int target = 4;

    const int firstIndex = linearSearch(values, target);
    // The printed result shows whether the program can analyze behavior for empty, duplicate, and
    // missing values.
    cout << "First index of " << target << ": " << firstIndex << '\n';
    cout << "Occurrences of " << target << ": " << countOccurrences(values, target) << '\n';

    printMinMax(values);
    return 0;
}
