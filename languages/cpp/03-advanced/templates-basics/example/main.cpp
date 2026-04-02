// Module focus: Writing generic code that stays useful across multiple data types.
// Why it matters: practicing templates basics patterns makes exercises and checkpoints easier to
// reason about.

#include <iostream>
#include <string>
using namespace std;

// Helper setup for templates basics; this keeps the walkthrough readable.
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

// Walk through one fixed scenario so templates basics behavior stays repeatable.
int main() {
    // Prepare sample inputs that exercise the key templates basics path.
    // Report values so learners can verify the templates basics outcome.
    cout << "maxValue(4, 7) = " << maxValue(4, 7) << '\n';
    cout << "maxValue(2.5, 1.2) = " << maxValue(2.5, 1.2) << '\n';

    Pair<string> p("left", "right");
    p.print();

    return 0;
}
