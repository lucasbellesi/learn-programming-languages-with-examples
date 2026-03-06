#include <iostream>
#include <map>
using namespace std;


int main() {
    int n = 0;
    cout << "How many digits? ";
    cin >> n;

    if (n <= 0) {
        cout << "Please enter a positive count.\n";
        return 0;
    }

    map<int, int> frequency;
    for (int digit = 0; digit <= 9; ++digit) {
        frequency[digit] = 0;
    }

    for (int i = 0; i < n; ++i) {
        int value = 0;
        cin >> value;
        if (value >= 0 && value <= 9) {
            ++frequency[value];
        }
    }

    for (int digit = 0; digit <= 9; ++digit) {
        cout << digit << " -> " << frequency[digit] << '\n';
    }

    return 0;
}
