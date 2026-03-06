#include <iostream>
using namespace std;


int main() {
    int n = 0;
    cout << "Enter N: ";
    cin >> n;

    if (n <= 0) {
        cout << "N must be positive.\n";
        return 0;
    }

    int sum = 0;
    {
        for (int i = 1; i <= n; ++i) {
            sum += i;
        }
    }

    cout << "Sum 1.." << n << " = " << sum << '\n';
    return 0;
}
