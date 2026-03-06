#include <fstream>
#include <iostream>
#include <limits>
#include <string>

int main() {
    std::string path;
    std::cout << "Enter file path (name score rows): ";
    std::getline(std::cin, path);

    std::ifstream input(path);
    if (!input) {
        std::cout << "Could not open file.\n";
        return 0;
    }

    std::string name;
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
            input.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
        }
    }

    std::cout << "Valid rows: " << validRows << '\n';
    std::cout << "Invalid rows: " << invalidRows << '\n';

    if (validRows > 0) {
        const double average = static_cast<double>(sum) / validRows;
        std::cout << "Average score: " << average << '\n';
    } else {
        std::cout << "No valid rows found.\n";
    }

    return 0;
}
