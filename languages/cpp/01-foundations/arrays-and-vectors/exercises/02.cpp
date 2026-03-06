#include <iostream>
#include <vector>
using namespace std;


int main() {
    int n = 0;
    cout << "How many integers will you enter? ";
    cin >> n;

    if (n <= 0) {
        cout << "Please enter a positive number.\n";
        return 0;
    }

    vector<int> values;
    values.reserve(static_cast<size_t>(n));

    for (int i = 0; i < n; ++i) {
        int number = 0;
        cout << "Number " << (i + 1) << ": ";
        cin >> number;
        values.push_back(number);
    }

    int target = 0;
    cout << "Enter the number to count: ";
    cin >> target;

    int frequency = 0;
    for (int value : values) {
        if (value == target) {
            ++frequency;
        }
    }

    cout << target << " appears " << frequency << " time(s).\n";
    return 0;
}
