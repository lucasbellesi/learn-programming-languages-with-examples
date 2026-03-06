#include <iostream>
using namespace std;


template <typename T>
void swapValues(T& left, T& right) {
    const T temp = left;
    left = right;
    right = temp;
}

int main() {
    int a = 0;
    int b = 0;

    cout << "Enter two integers: ";
    cin >> a >> b;

    cout << "Before swap: " << a << " " << b << '\n';
    swapValues(a, b);
    cout << "After swap: " << a << " " << b << '\n';

    return 0;
}
