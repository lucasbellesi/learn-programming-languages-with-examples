#include <iostream>
#include <mutex>
#include <thread>
#include <vector>

int main() {
    const int threadCount = 4;
    const int incrementsPerThread = 50000;

    int counter = 0;
    std::mutex counterMutex;

    auto worker = [&counter, &counterMutex, incrementsPerThread]() {
        for (int i = 0; i < incrementsPerThread; ++i) {
            std::lock_guard<std::mutex> lock(counterMutex);
            ++counter;
        }
    };

    std::vector<std::thread> threads;
    threads.reserve(static_cast<std::size_t>(threadCount));

    for (int i = 0; i < threadCount; ++i) {
        threads.emplace_back(worker);
    }

    for (std::thread& thread : threads) {
        thread.join();
    }

    const int expected = threadCount * incrementsPerThread;
    std::cout << "Expected: " << expected << '\n';
    std::cout << "Actual: " << counter << '\n';

    return 0;
}
