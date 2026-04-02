// This helper example focuses on separating row parsing from the higher-level file workflow.

#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

struct StudentScore {
    string name;
    int score;
};

int main() {
    string path;
    cout << "CSV-like input file path (name,score): ";
    getline(cin, path);

    ifstream input(path);
    if (!input) {
        cout << "Could not open file: " << path << '\n';
        return 0;
    }

    vector<StudentScore> rows;
    string line;
    int lineNumber = 0;

    while (getline(input, line)) {
        ++lineNumber;
        if (line.empty()) {
            continue;
        }

        istringstream row(line);
        string name;
        string scoreText;

        if (!getline(row, name, ',') || !getline(row, scoreText)) {
            cout << "Skipping malformed line " << lineNumber << ": " << line << '\n';
            continue;
        }

        istringstream scoreStream(scoreText);
        int score = 0;
        if (!(scoreStream >> score) || score < 0 || score > 100) {
            cout << "Skipping invalid score on line " << lineNumber << ": " << scoreText << '\n';
            continue;
        }

        rows.push_back({name, score});
    }

    cout << "\nValid rows: " << rows.size() << '\n';
    for (const StudentScore& row : rows) {
        cout << "- " << row.name << ": " << row.score << '\n';
    }

    return 0;
}
