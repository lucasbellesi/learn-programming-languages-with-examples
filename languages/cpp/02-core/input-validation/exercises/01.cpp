#include <iostream>
#include <limits>
using namespace std;


int main() {
    int value = 0;

    while (true) {
        cout << "Enter an integer from 1 to 100: ";
        if (!(cin >> value)) {
            cout << "Invalid input. Please enter an integer.\n";
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
            continue;
        }

        if (value < 1 || value > 100) {
            cout << "Out of range. Try again.\n";
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
            continue;
        }

        break;
    }

    cout << "Square: " << (value * value) << '\n';
    return 0;
}
