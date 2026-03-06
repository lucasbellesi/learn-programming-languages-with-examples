#include <iostream>
using namespace std;


int main() {
    int score = 0;
    cout << "Enter score (0-100): ";
    cin >> score;

    if (score < 0 || score > 100) {
        cout << "Invalid score.\n";
        return 0;
    }

    char grade = 'F';
    if (score >= 90) {
        grade = 'A';
    } else if (score >= 80) {
        grade = 'B';
    } else if (score >= 70) {
        grade = 'C';
    } else if (score >= 60) {
        grade = 'D';
    }

    cout << "Grade: " << grade << '\n';
    return 0;
}
