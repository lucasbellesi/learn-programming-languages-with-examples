#include <iostream>
#include <vector>

template <typename T>
double averageOf(const std::vector<T>& values) {
    if (values.empty()) {
        return 0.0;
    }

    double sum = 0.0;
    for (const T& value : values) {
        sum += static_cast<double>(value);
    }

    return sum / values.size();
}

int main() {
    int n = 0;
    std::cout << "How many numbers? ";
    std::cin >> n;

    if (n <= 0) {
        std::cout << "Please enter a positive count.\n";
        return 0;
    }

    std::vector<double> values;
    values.reserve(static_cast<std::size_t>(n));

    for (int i = 0; i < n; ++i) {
        double value = 0.0;
        std::cin >> value;
        values.push_back(value);
    }

    std::cout << "Average: " << averageOf(values) << '\n';
    return 0;
}
