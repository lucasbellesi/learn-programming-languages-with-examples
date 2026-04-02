// This example shows reading plain-text files, parsing rows, and writing clear results.
// In C++, the example keeps value flow, references, and explicit control visible.

#include <fstream>
#include <iostream>
#include <string>
using namespace std;

// Run one deterministic scenario so the console output makes reading plain-text files, parsing
// rows, and writing clear results easy to verify.
int main() {
    // Build the sample state first, then let the later output confirm the behavior step by step.
    const string inputPath = "scores.txt";
    ifstream input(inputPath);

    if (!input) {
        // Print the observed state here so learners can connect the code path to a concrete result.
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
