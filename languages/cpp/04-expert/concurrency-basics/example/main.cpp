// This example demonstrates concurrency basics concepts.
// Example purpose: show the module flow with clear, beginner-friendly steps.

#include <iostream>
#include <mutex>
#include <thread>
#include <vector>
using namespace std;


int main() {
    // Program flow: collect input, apply core logic, then print a verifiable result.
    const int threadCount = 4;
    const int incrementsPerThread = 50000;

    int counter = 0;
    mutex counterMutex;

    auto worker = [&counter, &counterMutex, incrementsPerThread]() {
        // Intent: iterate through data in a clear and deterministic order.
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
    // Intent: print intermediate or final output for quick behavior verification.
    cout << "Expected: " << expected << '\n';
    cout << "Actual: " << counter << '\n';

    return 0;
}
