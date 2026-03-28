// This example demonstrates arrays and vectors concepts.
// Example purpose: show the module flow with clear, beginner-friendly steps.

#include <iostream>
#include <vector>
using namespace std;

int main() {
    // Program flow: collect input, apply core logic, then print a verifiable result.
    const int fixedScores[3] = {72, 88, 95};

    // Intent: print intermediate or final output for quick behavior verification.
    cout << "Fixed array values: ";
    // Intent: iterate through data in a clear and deterministic order.
    for (int i = 0; i < 3; ++i) {
        cout << fixedScores[i];
        // Intent: guard invalid or edge-case paths before the main path continues.
        if (i < 2) {
            cout << ", ";
        }
    }
    cout << '\n';

    int count = 0;
    cout << "How many temperatures do you want to enter? ";
    // Intent: gather typed input first so later operations are predictable.
    cin >> count;

    if (count <= 0) {
        cout << "Nothing to process.\n";
        return 0;
    }

    vector<double> temperatures;
    temperatures.reserve(static_cast<size_t>(count));

    for (int i = 0; i < count; ++i) {
        double value = 0.0;
        cout << "Temperature " << (i + 1) << ": ";
        cin >> value;
        temperatures.push_back(value);
    }

    double sum = 0.0;
    for (double value : temperatures) {
        sum += value;
    }

    const double average = sum / temperatures.size();

    cout << "\nYou entered: ";
    for (size_t i = 0; i < temperatures.size(); ++i) {
        cout << temperatures[i];
        if (i + 1 < temperatures.size()) {
            cout << ", ";
        }
    }
    cout << '\n';
    cout << "Average temperature: " << average << '\n';

    return 0;
}
