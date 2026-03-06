#include <iostream>
#include <thread>
#include <vector>

int main() {
    int n = 0;
    std::cout << "How many integers? ";
    std::cin >> n;

    if (n <= 0) {
        std::cout << "Please enter a positive count.\n";
        return 0;
    }

    std::vector<int> values;
    values.reserve(static_cast<std::size_t>(n));
    for (int i = 0; i < n; ++i) {
        int value = 0;
        std::cin >> value;
        values.push_back(value);
    }

    int workerCount = 0;
    std::cout << "How many worker threads? ";
    std::cin >> workerCount;

    if (workerCount <= 0) {
        std::cout << "Worker count must be positive.\n";
        return 0;
    }

    if (workerCount > n) {
        workerCount = n;
    }

    std::vector<long long> partialSums(static_cast<std::size_t>(workerCount), 0);
    std::vector<std::thread> workers;
    workers.reserve(static_cast<std::size_t>(workerCount));

    const int chunkSize = (n + workerCount - 1) / workerCount;

    for (int workerIndex = 0; workerIndex < workerCount; ++workerIndex) {
        workers.emplace_back([&values, &partialSums, workerIndex, chunkSize, n]() {
            const int start = workerIndex * chunkSize;
            const int end = (start + chunkSize < n) ? (start + chunkSize) : n;

            long long localSum = 0;
            for (int i = start; i < end; ++i) {
                localSum += values[static_cast<std::size_t>(i)];
            }

            partialSums[static_cast<std::size_t>(workerIndex)] = localSum;
        });
    }

    for (std::thread& worker : workers) {
        worker.join();
    }

    long long total = 0;
    for (std::size_t i = 0; i < partialSums.size(); ++i) {
        std::cout << "Thread " << i << " partial sum: " << partialSums[i] << '\n';
        total += partialSums[i];
    }

    std::cout << "Final total: " << total << '\n';
    return 0;
}
