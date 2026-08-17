// Module focus: Measuring hot paths before changing code for speed.
// Why it matters: the example makes it possible to measure before optimizing and interpret
// timing data cautiously before the learner tackles the exercises.

#include <chrono>
#include <iostream>
#include <vector>
using namespace std;

// Separate helpers keep the main path focused on how to measure before optimizing and interpret
// timing data cautiously.
int linearSearch(const vector<int>& values, int target) {
    for (size_t i = 0; i < values.size(); ++i) {
        if (values[i] == target) {
            return static_cast<int>(i);
        }
    }
    return -1;
}

// Fixed inputs make the consequence of timing too-small workloads visible and repeatable.
int main() {
    // These values exercise the normal path before the exercises vary the documented boundaries.
    vector<int> values;
    values.reserve(100000);
    for (int i = 0; i < 100000; ++i) {
        values.push_back(i);
    }

    const auto start = chrono::high_resolution_clock::now();
    const int index = linearSearch(values, 99999);
    const auto end = chrono::high_resolution_clock::now();

    const auto elapsed = chrono::duration_cast<chrono::microseconds>(end - start);
    // The printed result shows whether the program can relate algorithmic and allocation choices
    // to observed cost.
    cout << "Index: " << index << '\n';
    cout << "Elapsed (microseconds): " << elapsed.count() << '\n';

    return 0;
}
