#include <iostream>
#include <string>
using namespace std;

int add(int left, int right) { return left + right; }

int subtract(int left, int right) { return left - right; }

int main() {
    string op;
    int a = 0;
    int b = 0;

    cout << "Operation (add/sub): ";
    cin >> op;
    cout << "Enter two integers: ";
    cin >> a >> b;

    if (op == "add") {
        cout << "Result: " << add(a, b) << '\n';
    } else if (op == "sub") {
        cout << "Result: " << subtract(a, b) << '\n';
    } else {
        cout << "Unsupported operation.\n";
    }

    return 0;
}
