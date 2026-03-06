#include <chrono>
#include <iostream>
#include <vector>
using namespace std;


int linearSearch(const vector<int>& values, int target) {
    for (size_t i = 0; i < values.size(); ++i) {
        if (values[i] == target) {
            return static_cast<int>(i);
        }
    }
    return -1;
}

int main() {
    vector<int> values;
    values.reserve(100000);
    for (int i = 0; i < 100000; ++i) {
        values.push_back(i);
    }

    const auto start = chrono::high_resolution_clock::now();
    const int index = linearSearch(values, 99999);
    const auto end = chrono::high_resolution_clock::now();

    const auto elapsed = chrono::duration_cast<chrono::microseconds>(end - start);
    cout << "Index: " << index << '\n';
    cout << "Elapsed (microseconds): " << elapsed.count() << '\n';

    return 0;
}
