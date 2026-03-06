/*
Exercise Guide: languages/cpp/01-foundations/operators-and-expressions/exercises/02.cpp
Goal: Solve the task defined in this module's README Exercise Specs.
Build: g++ -std=c++17 -Wall -Wextra -pedantic languages/cpp/01-foundations/operators-and-expressions/exercises/02.cpp -o 02_exercise
Run: ./02_exercise (Windows MSYS2: ./02_exercise.exe)
Sample Input: Use one of the sample cases from the module README Exercise Specs.
Expected Output: Follow the exact output rules described in the same exercise spec.
*/
#include <iostream>
using namespace std;


int main() {
    double basePrice = 0.0;
    int hasDiscount = 0;
    double taxRatePercent = 0.0;

    cout << "Enter base price: ";
    cin >> basePrice;
    cout << "Has discount? (1=yes, 0=no): ";
    cin >> hasDiscount;
    cout << "Enter tax rate (%): ";
    cin >> taxRatePercent;

    const double discountRate = (hasDiscount == 1) ? 0.10 : 0.0;
    const double discountedPrice = basePrice * (1.0 - discountRate);
    const double taxAmount = discountedPrice * (taxRatePercent / 100.0);
    const double finalPrice = discountedPrice + taxAmount;

    cout << "Final price: " << finalPrice << '\n';
    return 0;
}
