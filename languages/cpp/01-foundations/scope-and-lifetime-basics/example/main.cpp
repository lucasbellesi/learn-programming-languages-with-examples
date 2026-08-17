// Module focus: How names stay visible only inside the blocks that own them.
// Why it matters: the example makes it possible to predict name visibility across nested
// scopes before the learner tackles the exercises.

#include <iostream>
using namespace std;

// Separate helpers keep the main path focused on how to predict name visibility across nested
// scopes.
void printRangeSum(int from, int to) {
    int sum = 0;
    for (int value = from; value <= to; ++value) {
        sum += value;
    }
    cout << "Sum from " << from << " to " << to << " = " << sum << '\n';
}

// Fixed inputs make the consequence of using variables outside their scope visible and
// repeatable.
int main() {
    // These values exercise the normal path before the exercises vary the documented boundaries.
    int value = 10;
    // The printed result shows whether the program can explain when values and resources cease to
    // be usable.
    cout << "Outer value: " << value << '\n';

    {
        int value = 20;
        cout << "Inner shadowed value: " << value << '\n';
    }

    cout << "Outer value again: " << value << '\n';

    printRangeSum(1, 5);
    return 0;
}
