#include <iostream>
#include <string>
using namespace std;


int main() {
    string product;
    double price = 0.0;
    int quantity = 0;

    cout << "Enter product price quantity (example: notebook 2.50 4): ";
    cin >> product >> price >> quantity;

    const double totalPrice = price * quantity;

    cout << "Product: " << product << '\n';
    cout << "Unit price: " << price << '\n';
    cout << "Quantity: " << quantity << '\n';
    cout << "Total price: " << totalPrice << '\n';

    return 0;
}
