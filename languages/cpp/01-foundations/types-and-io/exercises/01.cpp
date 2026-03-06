#include <iostream>
using namespace std;


int main() {
    int n = 0;
    cout << "How many numbers will you enter? ";
    cin >> n;

    if (n <= 0) {
        cout << "Please enter a positive count.\n";
        return 0;
    }

    double value = 0.0;
    double sum = 0.0;
    double minimum = 0.0;
    double maximum = 0.0;

    for (int i = 0; i < n; ++i) {
        cout << "Number " << (i + 1) << ": ";
        cin >> value;

        if (i == 0) {
            minimum = value;
            maximum = value;
        } else {
            if (value < minimum) {
                minimum = value;
            }
            if (value > maximum) {
                maximum = value;
            }
        }

        sum += value;
    }

    const double average = sum / n;

    cout << "\nResults:\n";
    cout << "Sum: " << sum << '\n';
    cout << "Average: " << average << '\n';
    cout << "Minimum: " << minimum << '\n';
    cout << "Maximum: " << maximum << '\n';

    return 0;
}
