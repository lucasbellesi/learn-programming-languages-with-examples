/*
Exercise Guide: languages/cpp/01-foundations/formatted-output-and-iomanip/exercises/01.cpp
Goal:
 * Solve the task defined in this module's README Exercise Specs.
Build: g++ -std=c++17 -Wall
 * -Wextra -pedantic languages/cpp/01-foundations/formatted-output-and-iomanip/exercises/01.cpp -o
 * 01_exercise
Run: ./01_exercise (Windows MSYS2: ./01_exercise.exe)
Sample Input: Use one of the
 * sample cases from the module README Exercise Specs.
Expected Output: Follow the exact output
 * rules described in the same exercise spec.
*/
#include <iomanip>
#include <iostream>
#include <string>
using namespace std;

int main() {
    string name1, name2, name3;
    double price1 = 0.0, price2 = 0.0, price3 = 0.0;
    int qty1 = 0, qty2 = 0, qty3 = 0;

    cout << "Enter item1 (name price qty): ";
    cin >> name1 >> price1 >> qty1;
    cout << "Enter item2 (name price qty): ";
    cin >> name2 >> price2 >> qty2;
    cout << "Enter item3 (name price qty): ";
    cin >> name3 >> price3 >> qty3;

    const double total1 = price1 * qty1;
    const double total2 = price2 * qty2;
    const double total3 = price3 * qty3;
    const double grand = total1 + total2 + total3;

    cout << '\n'
         << left << setw(12) << "Item" << right << setw(10) << "Price" << setw(8) << "Qty"
         << setw(12) << "Total" << '\n';
    cout << "------------------------------------------\n";

    cout << left << setw(12) << name1 << right << setw(10) << fixed << setprecision(2) << price1
         << setw(8) << qty1 << setw(12) << total1 << '\n';
    cout << left << setw(12) << name2 << right << setw(10) << fixed << setprecision(2) << price2
         << setw(8) << qty2 << setw(12) << total2 << '\n';
    cout << left << setw(12) << name3 << right << setw(10) << fixed << setprecision(2) << price3
         << setw(8) << qty3 << setw(12) << total3 << '\n';

    cout << "Grand total: " << grand << '\n';
    return 0;
}
