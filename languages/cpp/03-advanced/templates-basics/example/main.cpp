// This example shows writing generic code that stays useful across multiple data types.
// In C++, the example keeps value flow, references, and explicit control visible.

#include <iostream>
#include <string>
using namespace std;

// Define the reusable pieces first so the main flow can focus on one observable scenario.
template <typename T> T maxValue(const T& left, const T& right) {
    return (left > right) ? left : right;
}

template <typename T> class Pair {
  public:
    Pair(const T& firstValue, const T& secondValue) : first(firstValue), second(secondValue) {}

    void print() const { cout << "(" << first << ", " << second << ")\n"; }

  private:
    T first;
    T second;
};

// Run one deterministic scenario so the console output makes writing generic code that stays useful
// across multiple data types easy to verify.
int main() {
    // Build the sample state first, then let the later output confirm the behavior step by step.
    // Print the observed state here so learners can connect the code path to a concrete result.
    cout << "maxValue(4, 7) = " << maxValue(4, 7) << '\n';
    cout << "maxValue(2.5, 1.2) = " << maxValue(2.5, 1.2) << '\n';

    Pair<string> p("left", "right");
    p.print();

    return 0;
}
