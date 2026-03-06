#include <iostream>
using namespace std;


int main() {
    int value = 0;
    int count = 0;
    double sum = 0.0;

    cout << "Enter integers (-1 to stop):\n";
    while (true) {
        cin >> value;

        if (value == -1) {
            break;
        }

        sum += value;
        ++count;
    }

    if (count == 0) {
        cout << "No values were entered before -1.\n";
    } else {
        const double average = sum / count;
        cout << "Average: " << average << '\n';
    }

    return 0;
}
