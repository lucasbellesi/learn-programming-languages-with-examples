#include <iostream>

namespace {
void runMemoryManagementRaiiExercise() {
    int depth = 0;
    std::cin >> depth;
    // TODO 1: Validate depth as a positive number of nested scopes.
    // TODO 2: Define a guard that increments on construction and decrements on destruction.
    // TODO 3: Enter depth scopes recursively and prove that the final counter returns to zero.
    (void)depth;
}
} // namespace

int main() {
    runMemoryManagementRaiiExercise();
    return 0;
}
