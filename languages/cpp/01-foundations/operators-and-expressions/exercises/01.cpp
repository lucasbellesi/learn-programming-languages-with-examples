#include <iostream>

int main() {
    int totalSeconds = 0;
    std::cout << "Enter total seconds: ";
    std::cin >> totalSeconds;

    if (totalSeconds < 0) {
        std::cout << "Please enter a non-negative value.\n";
        return 0;
    }

    const int hours = totalSeconds / 3600;
    const int minutes = (totalSeconds % 3600) / 60;
    const int seconds = totalSeconds % 60;

    std::cout << "Converted time: " << hours << ":" << minutes << ":" << seconds << '\n';
    return 0;
}
