// Module focus: Splitting responsibilities so entrypoints and helpers stay focused.
// Why it matters: practicing modularization and build structure patterns makes exercises and
// checkpoints easier to reason about.

#include <iostream>
using namespace std;

// Helper setup for modularization and build structure; this keeps the walkthrough readable.
int add(int left, int right) { return left + right; }

int multiply(int left, int right) { return left * right; }

void printReport(int a, int b) {
    // Report output values so learners can verify the modularization and build structure outcome.
    cout << "Add: " << add(a, b) << '\n';
    cout << "Multiply: " << multiply(a, b) << '\n';
}

// Walk through one fixed scenario so modularization and build structure behavior stays repeatable.
int main() {
    // Prepare sample inputs that exercise the key modularization and build structure path.
    printReport(3, 7);
    return 0;
}
