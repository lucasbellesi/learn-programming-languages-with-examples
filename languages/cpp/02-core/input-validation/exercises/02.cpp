#include <iostream>
#include <limits>
using namespace std;


int main() {
    int count = 0;

    while (true) {
        cout << "How many scores (1-50)? ";
        if (!(cin >> count)) {
            cout << "Invalid input. Please enter an integer.\n";
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
            continue;
        }

        if (count < 1 || count > 50) {
            cout << "Count must be between 1 and 50.\n";
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
            continue;
        }

        break;
    }

    double sum = 0.0;
    for (int i = 0; i < count; ++i) {
        double score = 0.0;

        while (true) {
            cout << "Score " << (i + 1) << " (0-100): ";
            if (!(cin >> score)) {
                cout << "Invalid input. Please enter a number.\n";
                cin.clear();
                cin.ignore(numeric_limits<streamsize>::max(), '\n');
                continue;
            }

            if (score < 0.0 || score > 100.0) {
                cout << "Score must be between 0 and 100.\n";
                cin.ignore(numeric_limits<streamsize>::max(), '\n');
                continue;
            }

            break;
        }

        sum += score;
    }

    cout << "Average score: " << (sum / count) << '\n';
    return 0;
}
