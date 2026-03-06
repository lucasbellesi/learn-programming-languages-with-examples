#include <iostream>
#include <string>

int add(int left, int right) {
    return left + right;
}

int subtract(int left, int right) {
    return left - right;
}

int main() {
    std::string op;
    int a = 0;
    int b = 0;

    std::cout << "Operation (add/sub): ";
    std::cin >> op;
    std::cout << "Enter two integers: ";
    std::cin >> a >> b;

    if (op == "add") {
        std::cout << "Result: " << add(a, b) << '\n';
    } else if (op == "sub") {
        std::cout << "Result: " << subtract(a, b) << '\n';
    } else {
        std::cout << "Unsupported operation.\n";
    }

    return 0;
}
