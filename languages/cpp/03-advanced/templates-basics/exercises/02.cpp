#include <iostream>
#include <vector>
using namespace std;

template <typename T> double averageOf(const vector<T>& values) {
    if (values.empty()) {
        return 0.0;
    }

    double sum = 0.0;
    for (const T& value : values) {
        sum += static_cast<double>(value);
    }

    return sum / values.size();
}

int main() {
    int n = 0;
    cout << "How many numbers? ";
    cin >> n;

    if (n <= 0) {
        cout << "Please enter a positive count.\n";
        return 0;
    }

    vector<double> values;
    values.reserve(static_cast<size_t>(n));

    for (int i = 0; i < n; ++i) {
        double value = 0.0;
        cin >> value;
        values.push_back(value);
    }

    cout << "Average: " << averageOf(values) << '\n';
    return 0;
}
