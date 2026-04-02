// This example shows measuring hot paths before changing code for speed.
// In C++, the example keeps value flow, references, and explicit control visible.

#include <chrono>
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

// Run one deterministic scenario so the console output makes measuring hot paths before changing
// code for speed easy to verify.
int main() {
    // Build the sample state first, then let the later output confirm the behavior step by step.
    vector<int> values;
    values.reserve(100000);
    for (int i = 0; i < 100000; ++i) {
        values.push_back(i);
    }

    const auto start = chrono::high_resolution_clock::now();
    const int index = linearSearch(values, 99999);
    const auto end = chrono::high_resolution_clock::now();

    const auto elapsed = chrono::duration_cast<chrono::microseconds>(end - start);
    // Print the observed state here so learners can connect the code path to a concrete result.
    cout << "Index: " << index << '\n';
    cout << "Elapsed (microseconds): " << elapsed.count() << '\n';

    return 0;
}
