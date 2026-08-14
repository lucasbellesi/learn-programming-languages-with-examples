#include <iostream>
using namespace std;

double safeDivide(double left, double right) {
    if (right == 0.0) {
        return 0.0;
    }
    return left / right;
}

double computeExpression(double a, double b, double c) { return safeDivide((a + b), c); }

int main() {
    double a = 0.0;
    double b = 0.0;
    double c = 0.0;

    cout << "Enter a b c: ";
    cin >> a >> b >> c;

    cout << "Result: " << computeExpression(a, b, c) << '\n';
    return 0;
}
