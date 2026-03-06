#include <iostream>
#include <vector>
using namespace std;


int main() {
    int n = 0;
    cout << "How many integers? ";
    cin >> n;

    if (n <= 0) {
        cout << "Please enter a positive number.\n";
        return 0;
    }

    vector<int> values;
    values.reserve(static_cast<size_t>(n));

    for (int i = 0; i < n; ++i) {
        int current = 0;
        cout << "Value " << (i + 1) << ": ";
        cin >> current;
        values.push_back(current);
    }

    cout << "Reversed order: ";
    for (int i = n - 1; i >= 0; --i) {
        cout << values[static_cast<size_t>(i)];
        if (i > 0) {
            cout << ' ';
        }
    }
    cout << '\n';

    return 0;
}
