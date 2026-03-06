#include <iomanip>
#include <iostream>
#include <string>

int main() {
    std::string name1, name2, name3;
    double price1 = 0.0, price2 = 0.0, price3 = 0.0;
    int qty1 = 0, qty2 = 0, qty3 = 0;

    std::cout << "Enter item1 (name price qty): ";
    std::cin >> name1 >> price1 >> qty1;
    std::cout << "Enter item2 (name price qty): ";
    std::cin >> name2 >> price2 >> qty2;
    std::cout << "Enter item3 (name price qty): ";
    std::cin >> name3 >> price3 >> qty3;

    const double total1 = price1 * qty1;
    const double total2 = price2 * qty2;
    const double total3 = price3 * qty3;
    const double grand = total1 + total2 + total3;

    std::cout << '\n' << std::left << std::setw(12) << "Item"
              << std::right << std::setw(10) << "Price"
              << std::setw(8) << "Qty"
              << std::setw(12) << "Total" << '\n';
    std::cout << "------------------------------------------\n";

    std::cout << std::left << std::setw(12) << name1
              << std::right << std::setw(10) << std::fixed << std::setprecision(2) << price1
              << std::setw(8) << qty1
              << std::setw(12) << total1 << '\n';
    std::cout << std::left << std::setw(12) << name2
              << std::right << std::setw(10) << std::fixed << std::setprecision(2) << price2
              << std::setw(8) << qty2
              << std::setw(12) << total2 << '\n';
    std::cout << std::left << std::setw(12) << name3
              << std::right << std::setw(10) << std::fixed << std::setprecision(2) << price3
              << std::setw(8) << qty3
              << std::setw(12) << total3 << '\n';

    std::cout << "Grand total: " << grand << '\n';
    return 0;
}
