#include <iostream>
using namespace std;


int main() {
    int n = 0;
    cout << "Run FizzBuzz up to: ";
    cin >> n;

    for (int i = 1; i <= n; ++i) {
        if (i % 15 == 0) {
            cout << "FizzBuzz";
        } else if (i % 3 == 0) {
            cout << "Fizz";
        } else if (i % 5 == 0) {
            cout << "Buzz";
        } else {
            cout << i;
        }

        if (i < n) {
            cout << '\n';
        }
    }

    cout << '\n';
    return 0;
}
