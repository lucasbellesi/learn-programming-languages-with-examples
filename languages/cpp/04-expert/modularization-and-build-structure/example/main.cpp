// Module focus: Splitting responsibilities so entrypoints and helpers stay focused.
// Why it matters: the example makes it possible to separate public contracts from
// implementation details before the learner tackles the exercises.

#include <iostream>
using namespace std;

// Separate helpers keep the main path focused on how to separate public contracts from
// implementation details.
int add(int left, int right) { return left + right; }

int multiply(int left, int right) { return left * right; }

void printReport(int a, int b) {
    // The printed result shows whether the program can organize a multi-file program with an
    // explicit build boundary.
    cout << "Add: " << add(a, b) << '\n';
    cout << "Multiply: " << multiply(a, b) << '\n';
}

// Fixed inputs make the consequence of placing function definitions in multiple translation units
// visible and repeatable.
int main() {
    // These values exercise the normal path before the exercises vary the documented boundaries.
    printReport(3, 7);
    return 0;
}
