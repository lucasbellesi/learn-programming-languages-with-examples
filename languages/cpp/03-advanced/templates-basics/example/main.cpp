// This example demonstrates templates basics concepts.
// Example purpose: show the module flow with clear, beginner-friendly steps.

#include <iostream>
#include <string>
using namespace std;

template <typename T> T maxValue(const T& left, const T& right) {
    return (left > right) ? left : right;
}

template <typename T> class Pair {
  public:
    Pair(const T& firstValue, const T& secondValue) : first(firstValue), second(secondValue) {}

    void print() const {
        // Intent: print intermediate or final output for quick behavior verification.
        cout << "(" << first << ", " << second << ")\n";
    }

  private:
    T first;
    T second;
};

int main() {
    // Program flow: collect input, apply core logic, then print a verifiable result.
    cout << "maxValue(4, 7) = " << maxValue(4, 7) << '\n';
    cout << "maxValue(2.5, 1.2) = " << maxValue(2.5, 1.2) << '\n';

    Pair<string> p("left", "right");
    p.print();

    return 0;
}
