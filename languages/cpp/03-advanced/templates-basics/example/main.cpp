// Module focus: Writing generic code that stays useful across multiple data types.
// Why it matters: the example makes it possible to express reusable type-safe behavior with
// language generics before the learner tackles the exercises.

#include <iostream>
#include <string>
using namespace std;

// Separate helpers keep the main path focused on how to express reusable type-safe behavior with
// language generics.
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

// Fixed inputs make the consequence of defining template implementations only in `.cpp` files
// visible and repeatable.
int main() {
    // These values exercise the normal path before the exercises vary the documented boundaries.
    // The printed result shows whether the program can apply constraints when an operation
    // requires specific capabilities.
    cout << "maxValue(4, 7) = " << maxValue(4, 7) << '\n';
    cout << "maxValue(2.5, 1.2) = " << maxValue(2.5, 1.2) << '\n';

    Pair<string> p("left", "right");
    p.print();

    return 0;
}
