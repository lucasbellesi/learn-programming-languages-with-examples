#include <iostream>
#include <string>

namespace {
void runSmartPointersInDepthExercise() {
    std::string scenario;
    std::cin >> scenario;
    // TODO 1: Accept `alive`, `expired`, or `missing` as the observation scenario.
    // TODO 2: Model the child-to-parent link with `std::weak_ptr`.
    // TODO 3: Report whether locking the weak reference succeeds in each state.
    (void)scenario;
}
} // namespace

int main() {
    runSmartPointersInDepthExercise();
    return 0;
}
