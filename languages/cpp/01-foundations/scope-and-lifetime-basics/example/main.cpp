// Module focus: How names stay visible only inside the blocks that own them.
// Why it matters: practicing scope and lifetime basics patterns makes exercises and checkpoints
// easier to reason about.

#include <iostream>
using namespace std;

// Helper setup for scope and lifetime basics; this keeps the walkthrough readable.
void printRangeSum(int from, int to) {
    int sum = 0;
    for (int value = from; value <= to; ++value) {
        sum += value;
    }
    cout << "Sum from " << from << " to " << to << " = " << sum << '\n';
}

// Walk through one fixed scenario so scope and lifetime basics behavior stays repeatable.
int main() {
    // Prepare sample inputs that exercise the key scope and lifetime basics path.
    int value = 10;
    // Report values so learners can verify the scope and lifetime basics outcome.
    cout << "Outer value: " << value << '\n';

    {
        int value = 20;
        cout << "Inner shadowed value: " << value << '\n';
    }

    cout << "Outer value again: " << value << '\n';

    printRangeSum(1, 5);
    return 0;
}
