#include <cstddef>
#include <iostream>
#include <memory>
using namespace std;

int main() {
    int n = 0;
    cout << "How many integers? ";
    cin >> n;

    if (n <= 0) {
        cout << "Please enter a positive count.\n";
        return 0;
    }

    unique_ptr<int[]> values(new int[static_cast<size_t>(n)]);

    for (int i = 0; i < n; ++i) {
        cout << "Value " << (i + 1) << ": ";
        cin >> values[static_cast<size_t>(i)];
    }

    long long sum = 0;
    for (int i = 0; i < n; ++i) {
        sum += values[static_cast<size_t>(i)];
    }

    cout << "Sum: " << sum << '\n';
    cout << "Reversed: ";
    for (int i = n - 1; i >= 0; --i) {
        cout << values[static_cast<size_t>(i)];
        if (i > 0) {
            cout << ' ';
        }
    }
    cout << '\n';

    return 0;
}
