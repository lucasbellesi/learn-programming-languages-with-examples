#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n = 0;
    cout << "How many numbers? ";
    cin >> n;

    if (n <= 0) {
        cout << "Please enter a positive count.\n";
        return 0;
    }

    vector<int> values;
    values.reserve(static_cast<size_t>(n));

    for (int i = 0; i < n; ++i) {
        int value = 0;
        cout << "Value " << (i + 1) << ": ";
        cin >> value;
        values.push_back(value);
    }

    int threshold = 0;
    cout << "Filter values greater than or equal to: ";
    cin >> threshold;

    cout << "Filtered values: ";
    bool printedAny = false;
    for (size_t i = 0; i < values.size(); ++i) {
        if (values[i] >= threshold) {
            if (printedAny) {
                cout << ", ";
            }
            cout << values[i];
            printedAny = true;
        }
    }

    if (!printedAny) {
        cout << "none";
    }
    cout << '\n';

    return 0;
}
