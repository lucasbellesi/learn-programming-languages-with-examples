// This example shows starting multiple units of work and combining their results safely.
// In C++, the example keeps value flow, references, and explicit control visible.

#include <iostream>
#include <mutex>
#include <thread>
#include <vector>
using namespace std;

// Run one deterministic scenario so the console output makes starting multiple units of work and
// combining their results safely easy to verify.
int main() {
    // Build the sample state first, then let the later output confirm the behavior step by step.
    const int threadCount = 4;
    const int incrementsPerThread = 50000;

    int counter = 0;
    mutex counterMutex;

    auto worker = [&counter, &counterMutex, incrementsPerThread]() {
        for (int i = 0; i < incrementsPerThread; ++i) {
            lock_guard<mutex> lock(counterMutex);
            ++counter;
        }
    };

    vector<thread> threads;
    threads.reserve(static_cast<size_t>(threadCount));

    for (int i = 0; i < threadCount; ++i) {
        threads.emplace_back(worker);
    }

    for (thread& thread : threads) {
        thread.join();
    }

    const int expected = threadCount * incrementsPerThread;
    // Print the observed state here so learners can connect the code path to a concrete result.
    cout << "Expected: " << expected << '\n';
    cout << "Actual: " << counter << '\n';

    return 0;
}
