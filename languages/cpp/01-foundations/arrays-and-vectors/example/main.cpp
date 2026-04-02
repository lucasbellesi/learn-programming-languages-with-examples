// Module focus: Storing related values in ordered collections and iterating safely.
// Why it matters: practicing arrays and vectors patterns makes exercises and checkpoints easier to
// reason about.

#include <iostream>
#include <vector>
using namespace std;

// Walk through one fixed scenario so arrays and vectors behavior stays repeatable.
int main() {
    // Prepare sample inputs that exercise the key arrays and vectors path.
    const int fixedScores[3] = {72, 88, 95};

    // Report values so learners can verify the arrays and vectors outcome.
    cout << "Fixed array values: ";
    for (int i = 0; i < 3; ++i) {
        cout << fixedScores[i];
        if (i < 2) {
            cout << ", ";
        }
    }
    cout << '\n';

    int count = 0;
    cout << "How many temperatures do you want to enter? ";
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
