// This helper example focuses on isolating the reusable generic behavior before the example wires
// it together.

#include <iostream>
#include <string>
#include <vector>

using namespace std;

// Keep this helper separate so the main example can focus on the larger idea without extra noise.
template <typename T> void printVector(const vector<T>& values, const string& label) {
    cout << label << ": [";
    for (size_t i = 0; i < values.size(); ++i) {
        cout << values[i];
        if (i + 1 < values.size()) {
            cout << ", ";
        }
    }
    cout << "]\n";
}

template <typename T> T sumVector(const vector<T>& values) {
    T total = T{};
    for (const T& value : values) {
        total += value;
    }
    return total;
}

int main() {
    vector<int> numbers = {2, 4, 6, 8};
    vector<double> prices = {1.5, 2.25, 3.75};

    printVector(numbers, "Numbers");
    printVector(prices, "Prices");

    cout << "Sum of numbers: " << sumVector(numbers) << '\n';
    cout << "Sum of prices: " << sumVector(prices) << '\n';

    return 0;
}
