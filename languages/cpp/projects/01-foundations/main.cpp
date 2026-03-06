#include <iostream>
#include <limits>
#include <string>
#include <vector>

struct Student {
    std::string name;
    int score;
};

int readPositiveCount() {
    int count = 0;
    while (true) {
        std::cout << "How many students? ";
        if (!(std::cin >> count)) {
            std::cout << "Invalid number. Try again.\n";
            std::cin.clear();
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
            continue;
        }
        if (count <= 0) {
            std::cout << "Please enter a positive number.\n";
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
            continue;
        }

        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
        return count;
    }
}

int readScore(const std::string& studentName) {
    int score = 0;
    while (true) {
        std::cout << "Score for " << studentName << " (0-100): ";
        if (!(std::cin >> score)) {
            std::cout << "Invalid score. Enter a number from 0 to 100.\n";
            std::cin.clear();
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
            continue;
        }
        if (score < 0 || score > 100) {
            std::cout << "Score out of range. Enter a value from 0 to 100.\n";
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
            continue;
        }

        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
        return score;
    }
}

int main() {
    const int count = readPositiveCount();

    std::vector<Student> students;
    students.reserve(static_cast<std::size_t>(count));

    for (int i = 0; i < count; ++i) {
        Student student;
        std::cout << "Student name " << (i + 1) << ": ";
        std::getline(std::cin, student.name);
        student.score = readScore(student.name);

        students.push_back(student);
    }

    int minScore = students[0].score;
    int maxScore = students[0].score;
    int sum = 0;

    std::cout << "\nStudents:\n";
    for (const Student& student : students) {
        std::cout << "- " << student.name << ": " << student.score << '\n';
        sum += student.score;
        if (student.score < minScore) {
            minScore = student.score;
        }
        if (student.score > maxScore) {
            maxScore = student.score;
        }
    }

    const double average = static_cast<double>(sum) / students.size();
    std::cout << "Average: " << average << '\n';
    std::cout << "Minimum: " << minScore << '\n';
    std::cout << "Maximum: " << maxScore << '\n';

    return 0;
}
