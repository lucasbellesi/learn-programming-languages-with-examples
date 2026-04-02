// Module focus: Starting multiple units of work and combining their results safely.
// Why it matters: practicing concurrency basics patterns makes exercises and checkpoints easier to
// reason about.

#include <iostream>
#include <mutex>
#include <thread>
#include <vector>
using namespace std;

// Walk through one fixed scenario so concurrency basics behavior stays repeatable.
int main() {
    // Prepare sample inputs that exercise the key concurrency basics path.
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
    // Report values so learners can verify the concurrency basics outcome.
    cout << "Expected: " << expected << '\n';
    cout << "Actual: " << counter << '\n';

    return 0;
}
