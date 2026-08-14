/*
Exercise Guide: languages/cpp/02-core/file-io-basics/exercises/01.cpp
Goal: Solve the task
 * defined in this module's README Exercise Specs.
Build: g++ -std=c++17 -Wall -Wextra -pedantic
 * languages/cpp/02-core/file-io-basics/exercises/01.cpp -o 01_exercise
Run: ./01_exercise (Windows
 * MSYS2: ./01_exercise.exe)
Sample Input: Use one of the sample cases from the module README
 * Exercise Specs.
Expected Output: Follow the exact output rules described in the same exercise
 * spec.
*/
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
