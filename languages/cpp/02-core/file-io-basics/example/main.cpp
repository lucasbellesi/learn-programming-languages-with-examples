#include <fstream>
#include <iostream>
#include <string>
using namespace std;


int main() {
    const string inputPath = "scores.txt";
    ifstream input(inputPath);

    if (!input) {
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
