#include <iostream>
#include <vector>

int main() {
    int sharedCounter = 0;

    std::cout << "Simulated interleaving of two tasks:\n";

    std::cout << "Task A reads " << sharedCounter << '\n';
    int taskATemp = sharedCounter;

    std::cout << "Task B reads " << sharedCounter << '\n';
    int taskBTemp = sharedCounter;

    ++taskATemp;
    ++taskBTemp;

    sharedCounter = taskATemp;
    std::cout << "Task A writes " << sharedCounter << '\n';

    sharedCounter = taskBTemp;
    std::cout << "Task B writes " << sharedCounter << '\n';

    std::cout << "Final counter: " << sharedCounter << " (expected 2 in synchronized execution)\n";

    return 0;
}
