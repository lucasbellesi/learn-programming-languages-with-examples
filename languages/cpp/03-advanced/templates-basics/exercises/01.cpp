#include <iostream>

template <typename T>
void swapValues(T& left, T& right) {
    const T temp = left;
    left = right;
    right = temp;
}

int main() {
    int a = 0;
    int b = 0;

    std::cout << "Enter two integers: ";
    std::cin >> a >> b;

    std::cout << "Before swap: " << a << " " << b << '\n';
    swapValues(a, b);
    std::cout << "After swap: " << a << " " << b << '\n';

    return 0;
}
