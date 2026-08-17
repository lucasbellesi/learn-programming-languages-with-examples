// Module focus: Starting multiple units of work and combining their results safely.
// Why it matters: the example makes it possible to coordinate concurrent work without data races
// or lost results before the learner tackles the exercises.

#include <iostream>
#include <mutex>
#include <thread>
#include <vector>
using namespace std;

// Fixed inputs make the consequence of reading/writing shared state without synchronization
// visible and repeatable.
int main() {
    // These values exercise the normal path before the exercises vary the documented boundaries.
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
    // The printed result shows whether the program can define completion, cancellation, and error
    // propagation behavior.
    cout << "Expected: " << expected << '\n';
    cout << "Actual: " << counter << '\n';

    return 0;
}
