#include <fstream>
#include <iostream>
#include <string>

int main() {
    const std::string inputPath = "scores.txt";
    std::ifstream input(inputPath);

    if (!input) {
        std::cout << "Could not open " << inputPath << "\n";
        std::cout << "Create a file named scores.txt with lines like: name score\n";
        return 0;
    }

    std::string name;
    int score = 0;
    int count = 0;
    int sum = 0;

    while (input >> name >> score) {
        std::cout << name << " -> " << score << '\n';
        sum += score;
        ++count;
    }

    if (count == 0) {
        std::cout << "No valid rows found.\n";
        return 0;
    }

    const double average = static_cast<double>(sum) / count;

    std::ofstream output("summary.txt");
    if (!output) {
        std::cout << "Could not create summary.txt\n";
        return 0;
    }

    output << "Rows: " << count << '\n';
    output << "Average: " << average << '\n';

    std::cout << "Summary written to summary.txt\n";
    return 0;
}
