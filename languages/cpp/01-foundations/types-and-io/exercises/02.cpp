/*
Exercise Guide: languages/cpp/01-foundations/types-and-io/exercises/02.cpp
Goal: Solve the task defined in this module's README Exercise Specs.
Build: g++ -std=c++17 -Wall -Wextra -pedantic languages/cpp/01-foundations/types-and-io/exercises/02.cpp -o 02_exercise
Run: ./02_exercise (Windows MSYS2: ./02_exercise.exe)
Sample Input: Use one of the sample cases from the module README Exercise Specs.
Expected Output: Follow the exact output rules described in the same exercise spec.
*/
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
