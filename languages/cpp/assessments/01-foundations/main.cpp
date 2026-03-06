#include <iostream>
#include <limits>
#include <string>
#include <vector>

using namespace std;

struct Student {
    string name;
    int score;
};

int readPositiveCount() {
    int count = 0;
    while (true) {
        cout << "How many students? ";
        if (!(cin >> count)) {
            cout << "Invalid number. Try again.\n";
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
            continue;
        }
        if (count <= 0) {
            cout << "Please enter a positive number.\n";
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
            continue;
        }

        cin.ignore(numeric_limits<streamsize>::max(), '\n');
        return count;
    }
}

int readScore(const string& studentName) {
    int score = 0;
    while (true) {
        cout << "Score for " << studentName << " (0-100): ";
        if (!(cin >> score)) {
            cout << "Invalid score. Enter a number from 0 to 100.\n";
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
            continue;
        }
        if (score < 0 || score > 100) {
            cout << "Score out of range. Enter a value from 0 to 100.\n";
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
            continue;
        }

        cin.ignore(numeric_limits<streamsize>::max(), '\n');
        return score;
    }
}

int main() {
    const int count = readPositiveCount();
    vector<Student> students;
    students.reserve(static_cast<size_t>(count));

    for (int i = 0; i < count; ++i) {
        Student student;
        cout << "Student name " << (i + 1) << ": ";
        getline(cin, student.name);
        student.score = readScore(student.name);
        students.push_back(student);
    }

    int total = 0;
    int passCount = 0;
    size_t highestIndex = 0;
    size_t lowestIndex = 0;

    for (size_t i = 0; i < students.size(); ++i) {
        total += students[i].score;
        if (students[i].score >= 60) {
            ++passCount;
        }
        if (students[i].score > students[highestIndex].score) {
            highestIndex = i;
        }
        if (students[i].score < students[lowestIndex].score) {
            lowestIndex = i;
        }
    }

    const double average = static_cast<double>(total) / students.size();

    cout << "\nStudents:\n";
    for (const Student& student : students) {
        cout << "- " << student.name << ": " << student.score << '\n';
    }

    cout << "Average: " << average << '\n';
    cout << "Highest: " << students[highestIndex].name
         << " (" << students[highestIndex].score << ")\n";
    cout << "Lowest: " << students[lowestIndex].name
         << " (" << students[lowestIndex].score << ")\n";
    cout << "Passed: " << passCount << "/" << students.size() << '\n';

    return 0;
}
