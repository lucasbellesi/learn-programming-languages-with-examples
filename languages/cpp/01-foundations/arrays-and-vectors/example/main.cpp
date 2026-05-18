// Module focus: Storing related values in ordered collections and iterating safely.
// Why it matters: practicing arrays and vectors patterns makes exercises and checkpoints easier to
// reason about.

#include <iostream>
#include <vector>

#include "temperature_report.hpp"

using namespace std;

// Walk through one fixed scenario so arrays and vectors behavior stays repeatable.
int main() {
    // Prepare sample inputs that exercise the key arrays and vectors path.
    const int fixedScores[3] = {72, 88, 95};

    // Report values so learners can verify the arrays and vectors outcome.
    print_fixed_scores(fixedScores, 3);

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

    print_temperature_report(temperatures);

    return 0;
}
