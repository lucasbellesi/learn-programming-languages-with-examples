#include <fstream>
#include <iostream>
#include <string>

int main() {
    std::string inputPath;
    std::string outputPath;

    std::cout << "Input file path: ";
    std::getline(std::cin, inputPath);
    std::cout << "Output file path: ";
    std::getline(std::cin, outputPath);

    std::ifstream input(inputPath);
    if (!input) {
        std::cout << "Could not open input file.\n";
        return 0;
    }

    std::ofstream output(outputPath);
    if (!output) {
        std::cout << "Could not create output file.\n";
        return 0;
    }

    std::string line;
    int lineNumber = 1;
    while (std::getline(input, line)) {
        output << lineNumber << ": " << line << '\n';
        ++lineNumber;
    }

    std::cout << "Copied " << (lineNumber - 1) << " lines.\n";
    return 0;
}
