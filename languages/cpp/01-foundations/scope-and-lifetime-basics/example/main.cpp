// This example shows how names stay visible only inside the blocks that own them.
// In C++, the example keeps value flow, references, and explicit control visible.

#include <iostream>
using namespace std;

// Define the reusable pieces first so the main flow can focus on one observable scenario.
void printRangeSum(int from, int to) {
    int sum = 0;
    for (int value = from; value <= to; ++value) {
        sum += value;
    }
    cout << "Sum from " << from << " to " << to << " = " << sum << '\n';
}

// Run one deterministic scenario so the console output makes how names stay visible only inside the
// blocks that own them easy to verify.
int main() {
    // Build the sample state first, then let the later output confirm the behavior step by step.
    int value = 10;
    // Print the observed state here so learners can connect the code path to a concrete result.
    cout << "Outer value: " << value << '\n';

    {
        int value = 20;
        cout << "Inner shadowed value: " << value << '\n';
    }

    cout << "Outer value again: " << value << '\n';

    printRangeSum(1, 5);
    return 0;
}
