#include <iostream>
#include <string>

int main() {
    std::string product;
    double price = 0.0;
    int quantity = 0;

    std::cout << "Enter product price quantity (example: notebook 2.50 4): ";
    std::cin >> product >> price >> quantity;

    const double totalPrice = price * quantity;

    std::cout << "Product: " << product << '\n';
    std::cout << "Unit price: " << price << '\n';
    std::cout << "Quantity: " << quantity << '\n';
    std::cout << "Total price: " << totalPrice << '\n';

    return 0;
}
