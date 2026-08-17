// Module focus: Reading plain-text files, parsing rows, and writing clear results.
// Why it matters: the example makes it possible to read and write explicit paths while reporting
// I/O failures before the learner tackles the exercises.

#include <fstream>
#include <iostream>
#include <string>
using namespace std;

// Fixed inputs make the consequence of assuming files always open successfully visible and
// repeatable.
int main() {
    // These values exercise the normal path before the exercises vary the documented boundaries.
    const string inputPath = "scores.txt";
    ifstream input(inputPath);

    if (!input) {
        // The printed result shows whether the program can parse records defensively and
        // distinguish valid from rejected rows.
        cout << "Could not open " << inputPath << "\n";
        cout << "Create a file named scores.txt with lines like: name score\n";
        return 0;
    }

    string name;
    int score = 0;
    int count = 0;
    int sum = 0;

    while (input >> name >> score) {
        cout << name << " -> " << score << '\n';
        sum += score;
        ++count;
    }

    if (count == 0) {
        cout << "No valid rows found.\n";
        return 0;
    }

    const double average = static_cast<double>(sum) / count;

    ofstream output("summary.txt");
    if (!output) {
        cout << "Could not create summary.txt\n";
        return 0;
    }

    output << "Rows: " << count << '\n';
    output << "Average: " << average << '\n';

    cout << "Summary written to summary.txt\n";
    return 0;
}
