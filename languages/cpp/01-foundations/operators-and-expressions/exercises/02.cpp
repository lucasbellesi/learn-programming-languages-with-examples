#include <iostream>

int main() {
    double basePrice = 0.0;
    int hasDiscount = 0;
    double taxRatePercent = 0.0;

    std::cout << "Enter base price: ";
    std::cin >> basePrice;
    std::cout << "Has discount? (1=yes, 0=no): ";
    std::cin >> hasDiscount;
    std::cout << "Enter tax rate (%): ";
    std::cin >> taxRatePercent;

    const double discountRate = (hasDiscount == 1) ? 0.10 : 0.0;
    const double discountedPrice = basePrice * (1.0 - discountRate);
    const double taxAmount = discountedPrice * (taxRatePercent / 100.0);
    const double finalPrice = discountedPrice + taxAmount;

    std::cout << "Final price: " << finalPrice << '\n';
    return 0;
}
