#include <iomanip>
#include <iostream>
using namespace std;


int main() {
    int precision = 2;
    cout << "Enter precision (0-6): ";
    cin >> precision;

    if (precision < 0 || precision > 6) {
        cout << "Precision must be between 0 and 6.\n";
        return 0;
    }

    int n = 0;
    cout << "How many numbers? ";
    cin >> n;
    if (n <= 0) {
        cout << "Please enter a positive count.\n";
        return 0;
    }

    double value = 0.0;
    double sum = 0.0;
    double minValue = 0.0;
    double maxValue = 0.0;

    for (int i = 0; i < n; ++i) {
        cout << "Value " << (i + 1) << ": ";
        cin >> value;

        if (i == 0) {
            minValue = value;
            maxValue = value;
        } else {
            if (value < minValue) {
                minValue = value;
            }
            if (value > maxValue) {
                maxValue = value;
            }
        }

        sum += value;
    }

    const double average = sum / n;

    cout << fixed << setprecision(precision);
    cout << "Average: " << average << '\n';
    cout << "Minimum: " << minValue << '\n';
    cout << "Maximum: " << maxValue << '\n';

    return 0;
}
