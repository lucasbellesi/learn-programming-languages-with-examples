#include <fstream>
#include <iostream>
#include <string>
using namespace std;


int main() {
    string inputPath;
    string outputPath;

    cout << "Input file path: ";
    getline(cin, inputPath);
    cout << "Output file path: ";
    getline(cin, outputPath);

    ifstream input(inputPath);
    if (!input) {
        cout << "Could not open input file.\n";
        return 0;
    }

    ofstream output(outputPath);
    if (!output) {
        cout << "Could not create output file.\n";
        return 0;
    }

    string line;
    int lineNumber = 1;
    while (getline(input, line)) {
        output << lineNumber << ": " << line << '\n';
        ++lineNumber;
    }

    cout << "Copied " << (lineNumber - 1) << " lines.\n";
    return 0;
}
