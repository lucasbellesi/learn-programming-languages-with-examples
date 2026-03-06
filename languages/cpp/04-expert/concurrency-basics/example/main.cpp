#include <iostream>
#include <mutex>
#include <thread>
#include <vector>
using namespace std;


int main() {
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
    cout << "Expected: " << expected << '\n';
    cout << "Actual: " << counter << '\n';

    return 0;
}
