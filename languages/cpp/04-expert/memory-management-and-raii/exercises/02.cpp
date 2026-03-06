#include <iostream>
#include <string>

class CounterGuard {
public:
    explicit CounterGuard(int& sharedCounterRef, const std::string& labelText)
        : sharedCounter(sharedCounterRef), label(labelText) {
        ++sharedCounter;
        std::cout << "[enter] " << label << " | active guards: " << sharedCounter << '\n';
    }

    ~CounterGuard() {
        --sharedCounter;
        std::cout << "[exit]  " << label << " | active guards: " << sharedCounter << '\n';
    }

private:
    int& sharedCounter;
    std::string label;
};

int main() {
    int activeGuards = 0;

    std::cout << "Starting scope demo.\n";
    {
        CounterGuard first(activeGuards, "first scope");
        {
            CounterGuard second(activeGuards, "nested scope");
            std::cout << "Inside nested scope.\n";
        }
        std::cout << "Back to first scope.\n";
    }

    std::cout << "Final active guards: " << activeGuards << '\n';
    return 0;
}
