#include <chrono>
#include <iostream>
#include <memory>
#include <string>
#include <vector>

class Step {
public:
    explicit Step(const std::string& nameValue) : name(nameValue), processedCount(0) {}

    void run() {
        ++processedCount;
    }

    const std::string& getName() const {
        return name;
    }

    int getProcessedCount() const {
        return processedCount;
    }

private:
    std::string name;
    int processedCount;
};

int main() {
    const int jobCount = 3;

    std::vector<std::unique_ptr<Step>> steps;
    steps.push_back(std::unique_ptr<Step>(new Step("load")));
    steps.push_back(std::unique_ptr<Step>(new Step("transform")));

    const auto start = std::chrono::high_resolution_clock::now();

    for (int job = 0; job < jobCount; ++job) {
        (void)job;
        for (auto& step : steps) {
            step->run();
        }
    }

    const auto end = std::chrono::high_resolution_clock::now();
    const auto elapsed = std::chrono::duration_cast<std::chrono::microseconds>(end - start).count();

    std::cout << "Running " << jobCount << " jobs through " << steps.size() << " steps...\n";
    for (const auto& step : steps) {
        std::cout << "Step " << step->getName() << " processed " << step->getProcessedCount() << " jobs\n";
    }
    std::cout << "Elapsed (microseconds): " << elapsed << '\n';

    return 0;
}
