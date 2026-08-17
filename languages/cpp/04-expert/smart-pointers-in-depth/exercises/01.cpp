#include <iostream>
#include <string>

namespace {
void runSmartPointersInDepthExercise() {
    std::string sourceName;
    std::string destinationName;
    std::getline(std::cin, sourceName);
    std::getline(std::cin, destinationName);
    // TODO 1: Convert `empty` to a null owner and other lines to owned resources.
    // TODO 2: Transfer with `std::move` only when the source exists and destination is empty.
    // TODO 3: Print both holders before and after the attempted transfer.
    (void)sourceName;
    (void)destinationName;
}
} // namespace

int main() {
    runSmartPointersInDepthExercise();
    return 0;
}
