#include <iostream>
#include <thread>
#include <vector>
using namespace std;

int main() {
    int n = 0;
    cout << "How many integers? ";
    cin >> n;

    if (n <= 0) {
        cout << "Please enter a positive count.\n";
        return 0;
    }

    vector<int> values;
    values.reserve(static_cast<size_t>(n));
    for (int i = 0; i < n; ++i) {
        int value = 0;
        cin >> value;
        values.push_back(value);
    }

    int workerCount = 0;
    cout << "How many worker threads? ";
    cin >> workerCount;

    if (workerCount <= 0) {
        cout << "Worker count must be positive.\n";
        return 0;
    }

    if (workerCount > n) {
        workerCount = n;
    }

    vector<long long> partialSums(static_cast<size_t>(workerCount), 0);
    vector<thread> workers;
    workers.reserve(static_cast<size_t>(workerCount));

    const int chunkSize = (n + workerCount - 1) / workerCount;

    for (int workerIndex = 0; workerIndex < workerCount; ++workerIndex) {
        workers.emplace_back([&values, &partialSums, workerIndex, chunkSize, n]() {
            const int start = workerIndex * chunkSize;
            const int end = (start + chunkSize < n) ? (start + chunkSize) : n;

            long long localSum = 0;
            for (int i = start; i < end; ++i) {
                localSum += values[static_cast<size_t>(i)];
            }

            partialSums[static_cast<size_t>(workerIndex)] = localSum;
        });
    }

    for (thread& worker : workers) {
        worker.join();
    }

    long long total = 0;
    for (size_t i = 0; i < partialSums.size(); ++i) {
        cout << "Thread " << i << " partial sum: " << partialSums[i] << '\n';
        total += partialSums[i];
    }

    cout << "Final total: " << total << '\n';
    return 0;
}
