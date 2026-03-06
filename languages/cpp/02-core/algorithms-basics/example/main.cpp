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

int main() {
    const vector<int> values{4, 7, 4, 1, 9, 4, 2};
    const int target = 4;

    const int firstIndex = linearSearch(values, target);
    cout << "First index of " << target << ": " << firstIndex << '\n';
    cout << "Occurrences of " << target << ": " << countOccurrences(values, target) << '\n';

    printMinMax(values);
    return 0;
}
