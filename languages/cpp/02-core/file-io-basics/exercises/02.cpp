#include <fstream>
#include <iostream>
#include <limits>
#include <string>
using namespace std;


int main() {
    string path;
    cout << "Enter file path (name score rows): ";
    getline(cin, path);

    ifstream input(path);
    if (!input) {
        cout << "Could not open file.\n";
        return 0;
    }

    string name;
    int score = 0;
    int validRows = 0;
    int invalidRows = 0;
    int sum = 0;

    while (true) {
        if (input >> name >> score) {
            sum += score;
            ++validRows;
        } else {
            if (input.eof()) {
                break;
            }
            ++invalidRows;
            input.clear();
            input.ignore(numeric_limits<streamsize>::max(), '\n');
        }
    }

    cout << "Valid rows: " << validRows << '\n';
    cout << "Invalid rows: " << invalidRows << '\n';

    if (validRows > 0) {
        const double average = static_cast<double>(sum) / validRows;
        cout << "Average score: " << average << '\n';
    } else {
        cout << "No valid rows found.\n";
    }

    return 0;
}
