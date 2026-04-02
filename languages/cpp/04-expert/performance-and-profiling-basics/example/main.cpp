// Module focus: Measuring hot paths before changing code for speed.
// Why it matters: practicing performance and profiling basics patterns makes exercises and
// checkpoints easier to reason about.

#include <chrono>
#include <iostream>
#include <vector>
using namespace std;

// Helper setup for performance and profiling basics; this keeps the walkthrough readable.
int linearSearch(const vector<int>& values, int target) {
    for (size_t i = 0; i < values.size(); ++i) {
        if (values[i] == target) {
            return static_cast<int>(i);
        }
    }
    return -1;
}

// Walk through one fixed scenario so performance and profiling basics behavior stays repeatable.
int main() {
    // Prepare sample inputs that exercise the key performance and profiling basics path.
    vector<int> values;
    values.reserve(100000);
    for (int i = 0; i < 100000; ++i) {
        values.push_back(i);
    }

    const auto start = chrono::high_resolution_clock::now();
    const int index = linearSearch(values, 99999);
    const auto end = chrono::high_resolution_clock::now();

    const auto elapsed = chrono::duration_cast<chrono::microseconds>(end - start);
    // Report values so learners can verify the performance and profiling basics outcome.
    cout << "Index: " << index << '\n';
    cout << "Elapsed (microseconds): " << elapsed.count() << '\n';

    return 0;
}
