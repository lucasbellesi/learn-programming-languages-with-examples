#include <iomanip>
#include <iostream>

int main() {
    const char* item1 = "Notebook";
    const char* item2 = "Pen";
    const char* item3 = "Backpack";

    const double p1 = 2.5;
    const double p2 = 1.2;
    const double p3 = 30.0;

    std::cout << std::left << std::setw(12) << "Item"
              << std::right << std::setw(10) << "Price" << '\n';
    std::cout << "----------------------\n";

    std::cout << std::left << std::setw(12) << item1
              << std::right << std::setw(10) << std::fixed << std::setprecision(2) << p1 << '\n';
    std::cout << std::left << std::setw(12) << item2
              << std::right << std::setw(10) << std::fixed << std::setprecision(2) << p2 << '\n';
    std::cout << std::left << std::setw(12) << item3
              << std::right << std::setw(10) << std::fixed << std::setprecision(2) << p3 << '\n';

    return 0;
}
