// Module focus: Storing related values in ordered collections and iterating safely.
// Why it matters: the example makes it possible to store and traverse ordered collections safely
// before the learner tackles the exercises.

#include <iostream>
#include <vector>

#include "temperature_report.hpp"

using namespace std;

// Fixed inputs make the consequence of accessing out-of-range indexes visible and repeatable.
int main() {
    // These values exercise the normal path before the exercises vary the documented boundaries.
    const int fixedScores[3] = {72, 88, 95};

    // The printed result shows whether the program can handle empty collections and index
    // boundaries explicitly.
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
