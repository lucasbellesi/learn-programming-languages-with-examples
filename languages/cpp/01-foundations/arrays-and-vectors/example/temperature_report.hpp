// Module focus: Keep array and vector reporting code separate from input handling.
// Why it matters: small helper functions make collection loops easier to read.

#ifndef TEMPERATURE_REPORT_HPP
#define TEMPERATURE_REPORT_HPP

#include <cstddef>
#include <iostream>
#include <vector>

inline void print_fixed_scores(const int scores[], std::size_t count) {
    std::cout << "Fixed array values: ";
    for (std::size_t i = 0; i < count; ++i) {
        std::cout << scores[i];
        if (i + 1 < count) {
            std::cout << ", ";
        }
    }
    std::cout << '\n';
}

inline double average_temperature(const std::vector<double>& temperatures) {
    double sum = 0.0;
    for (double value : temperatures) {
        sum += value;
    }

    return sum / temperatures.size();
}

inline void print_temperature_report(const std::vector<double>& temperatures) {
    std::cout << "\nYou entered: ";
    for (std::size_t i = 0; i < temperatures.size(); ++i) {
        std::cout << temperatures[i];
        if (i + 1 < temperatures.size()) {
            std::cout << ", ";
        }
    }
    std::cout << '\n';
    std::cout << "Average temperature: " << average_temperature(temperatures) << '\n';
}

#endif
