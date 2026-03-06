#include <iostream>
#include <string>

int main() {
    std::string row;
    std::cout << "Enter row (name,age,city): ";
    std::getline(std::cin, row);

    const std::size_t firstComma = row.find(',');
    if (firstComma == std::string::npos) {
        std::cout << "Invalid format. Missing commas.\n";
        return 0;
    }

    const std::size_t secondComma = row.find(',', firstComma + 1);
    if (secondComma == std::string::npos) {
        std::cout << "Invalid format. Missing second comma.\n";
        return 0;
    }

    const std::string name = row.substr(0, firstComma);
    const std::string age = row.substr(firstComma + 1, secondComma - firstComma - 1);
    const std::string city = row.substr(secondComma + 1);

    if (name.empty() || age.empty() || city.empty()) {
        std::cout << "Invalid format. Empty field detected.\n";
        return 0;
    }

    std::cout << "Name: " << name << '\n';
    std::cout << "Age: " << age << '\n';
    std::cout << "City: " << city << '\n';

    return 0;
}
