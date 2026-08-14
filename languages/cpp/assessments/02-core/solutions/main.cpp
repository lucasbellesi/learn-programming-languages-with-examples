#include <fstream>
#include <iostream>
#include <limits>
#include <string>
#include <vector>

using namespace std;

void printAndWriteLine(ostream& out, ofstream& file, const string& line) {
    out << line << '\n';
    file << line << '\n';
}

int bucketForScore(int score) {
    if (score == 100) {
        return 9;
    }
    return score / 10;
}

int main() {
    ofstream report("core_assessment_report.txt");
    if (!report) {
        cout << "Could not create report file.\n";
        return 1;
    }

    vector<int> values;
    vector<int> buckets(10, 0);

    cout << "Enter integer values (0-100). End with -1.\n";
    while (true) {
        int value = 0;
        if (!(cin >> value)) {
            cout << "Invalid input. Stopping read.\n";
            break;
        }

        if (value == -1) {
            break;
        }

        if (value < 0 || value > 100) {
            cout << "Ignoring out-of-range value: " << value << '\n';
            continue;
        }

        values.push_back(value);
        ++buckets[bucketForScore(value)];
    }

    if (values.empty()) {
        printAndWriteLine(cout, report, "No valid values were entered.");
        printAndWriteLine(cout, report, "Report saved to core_assessment_report.txt");
        return 0;
    }

    int minValue = values[0];
    int maxValue = values[0];
    int sum = 0;
    for (int value : values) {
        sum += value;
        if (value < minValue) {
            minValue = value;
        }
        if (value > maxValue) {
            maxValue = value;
        }
    }

    const double average = static_cast<double>(sum) / values.size();

    printAndWriteLine(cout, report, "Valid count: " + to_string(values.size()));
    printAndWriteLine(cout, report, "Minimum: " + to_string(minValue));
    printAndWriteLine(cout, report, "Maximum: " + to_string(maxValue));
    printAndWriteLine(cout, report, "Average: " + to_string(average));
    printAndWriteLine(cout, report, "Frequency table:");

    for (int i = 0; i < 10; ++i) {
        int start = i * 10;
        int end = (i == 9) ? 100 : (start + 9);
        string label = to_string(start) + "-" + to_string(end) + ": " + to_string(buckets[i]);
        printAndWriteLine(cout, report, label);
    }

    printAndWriteLine(cout, report, "Report saved to core_assessment_report.txt");
    return 0;
}
