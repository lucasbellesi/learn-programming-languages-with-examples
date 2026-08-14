#include <fstream>
#include <iostream>
#include <limits>
#include <string>

int main() {
    std::string inputPath;
    std::cout << "Enter input file path: ";
    std::getline(std::cin, inputPath);

    std::ifstream input(inputPath);
    if (!input) {
        std::cout << "Could not open input file.\n";
        return 0;
    }

    int validRows = 0;
    int invalidRows = 0;
    int minScore = 0;
    int maxScore = 0;
    int sum = 0;

    std::string name;
    int score = 0;

    while (true) {
        if (input >> name >> score) {
            if (validRows == 0) {
                minScore = score;
                maxScore = score;
            } else {
                if (score < minScore) {
                    minScore = score;
                }
                if (score > maxScore) {
                    maxScore = score;
                }
            }
            sum += score;
            ++validRows;
        } else {
            if (input.eof()) {
                break;
            }
            ++invalidRows;
            input.clear();
            input.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
        }
    }

    std::ofstream report("report.txt");
    if (!report) {
        std::cout << "Could not create report.txt\n";
        return 0;
    }

    report << "Valid rows: " << validRows << '\n';
    report << "Invalid rows: " << invalidRows << '\n';

    if (validRows > 0) {
        const double average = static_cast<double>(sum) / validRows;
        report << "Average: " << average << '\n';
        report << "Minimum: " << minScore << '\n';
        report << "Maximum: " << maxScore << '\n';
    } else {
        report << "No valid rows found.\n";
    }

    std::cout << "Report generated: report.txt\n";
    return 0;
}
