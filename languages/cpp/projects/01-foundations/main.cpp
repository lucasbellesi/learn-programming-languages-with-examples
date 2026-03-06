#include <iostream>
#include <limits>
#include <string>
#include <vector>

struct Student {
    std::string name;
    int score;
};

int main() {
    int count = 0;
    std::cout << "How many students? ";
    std::cin >> count;

    if (count <= 0) {
        std::cout << "Please enter a positive number.\n";
        return 0;
    }

    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');

    std::vector<Student> students;
    students.reserve(static_cast<std::size_t>(count));

    for (int i = 0; i < count; ++i) {
        Student student;
        std::cout << "Student name " << (i + 1) << ": ";
        std::getline(std::cin, student.name);

        std::cout << "Score for " << student.name << " (0-100): ";
        std::cin >> student.score;
        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');

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
