#include <iostream>
#include <limits>
using namespace std;


int main() {
    while (true) {
        double a = 0.0;
        double b = 0.0;

        cout << "Enter two numbers to divide (a b): ";
        if (!(cin >> a >> b)) {
            cout << "Invalid input type. Try again.\n";
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
            continue;
        }

        if (b == 0.0) {
            cout << "Divisor cannot be zero. Try again.\n";
            continue;
        }

        cout << "Result: " << (a / b) << '\n';
        break;
    }

    return 0;
}
